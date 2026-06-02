from flask import Flask, Response, render_template, request, send_from_directory
import time
import json
import os
import requests
from pathlib import Path

from database import (
    DB_PATH,
    fetch_row,
    fetch_rows,
    get_connection,
    initialize_database,
)

app = Flask(__name__, template_folder="dist", static_folder="dist/static")

KCS2_BASE_URL = "https://w02k.kancolle-server.com/kcs2/"
KCS_BASE_URL = "https://w02k.kancolle-server.com/kcs/"
KCS2_ASSETS_DIR = "assets/kcs2/"

initialize_database(DB_PATH)


def query_db(sql, params=()):
    with get_connection(DB_PATH) as conn:
        cursor = conn.execute(sql, params)
        return [dict(row) for row in cursor.fetchall()]


def download_file(url, path):
    target_directory = os.path.dirname(os.path.join(KCS2_ASSETS_DIR, path))
    # Ensure the directory exists
    os.makedirs(target_directory, exist_ok=True)

    # Extract filename and combine with path
    filename = url.split("/")[-1]
    file_path = os.path.join(target_directory, filename)

    # Stream the file download to handle large files efficiently
    with requests.get(url, stream=True) as response:
        response.raise_for_status()  # Raise error for bad responses
        with open(file_path, "wb") as file:  # Write-binary mode
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
    print(f"File saved to: {file_path}")


# 渲染主页
@app.route("/")
def index():
    return render_template("index.html")


# 提供静态文件
@app.route("/kcs2/<path:path>")
def send_assets(path):
    if not os.path.isfile(os.path.join(KCS2_ASSETS_DIR, path)):
        if "resources/voice/kc" in path:
            real_path = path.replace("resources/voice", "sound")
            download_file(KCS_BASE_URL + real_path, path)
        else:
            download_file(KCS2_BASE_URL + path, path)
    return send_from_directory(KCS2_ASSETS_DIR, path)


# 提供mock静态文件
@app.route("/api/<path:path>")
def send_kcsapi(path):
    return send_from_directory("api", path)


# 初始化加载信息
@app.route("/initial_loading")
def send_initial_loading():
    time.sleep(2.5)
    return {"status": 200}


@app.route("/favicon.ico")
def favicon():
    # Return empty response to avoid 404 noise in browser console
    return "", 204


# kcsapi
def create_response_from_file(filepath):
    with open(filepath, encoding="utf-8") as f:
        body = f.read().strip()

    if not body.startswith("svdata="):
        body = "svdata=" + body

    response = Response(body, mimetype="text/plain")
    return response


def create_response_from_data(data):
    body = json.dumps(data, ensure_ascii=False)
    if not body.startswith("svdata="):
        body = "svdata=" + body
    return Response(body, mimetype="text/plain")


def build_getdata_api_data(conn):
    return {
        "api_mst_ship": fetch_rows(
            conn,
            "SELECT * FROM master_ship ORDER BY api_id",
            [
                "api_taik",
                "api_souk",
                "api_houg",
                "api_raig",
                "api_tyku",
                "api_luck",
                "api_maxeq",
                "api_broken",
                "api_powup",
            ],
        ),
        "api_mst_slotitem": fetch_rows(
            conn,
            "SELECT * FROM master_slotitem ORDER BY api_id",
            ["api_type", "api_broken"],
        ),
        "api_mst_stype": fetch_rows(
            conn,
            "SELECT * FROM master_stype ORDER BY api_id",
            ["api_equip_type"],
        ),
        "api_mst_useitem": fetch_rows(
            conn,
            "SELECT * FROM master_useitem ORDER BY api_id",
        ),
        "api_mst_furniture": fetch_rows(
            conn,
            "SELECT * FROM master_furniture ORDER BY api_id",
        ),
        "api_mst_maparea": fetch_rows(
            conn,
            "SELECT * FROM master_maparea ORDER BY api_id",
        ),
        "api_mst_mapinfo": fetch_rows(
            conn,
            "SELECT * FROM master_mapinfo ORDER BY api_id",
            ["api_item", "api_sally_flag"],
        ),
        "api_mst_mission": fetch_rows(
            conn,
            "SELECT * FROM master_mission ORDER BY api_id",
            ["api_win_item1", "api_win_item2", "api_win_mat_level", "api_sample_fleet"],
        ),
        "api_mst_shipgraph": fetch_rows(
            conn,
            "SELECT * FROM master_shipgraph ORDER BY api_id",
        ),
        "api_mst_equip_exslot_ship": {
            row["api_ship_id"]: row["exslot_json"]
            for row in fetch_rows(
                conn,
                "SELECT * FROM master_equip_exslot_ship ORDER BY api_ship_id",
                ["exslot_json"],
            )
        },
    }


def get_data_response_from_db():
    with get_connection(DB_PATH) as conn:
        api_data = build_getdata_api_data(conn)
    return create_response_from_data(
        {"api_result": 1, "api_result_msg": "成功", "api_data": api_data}
    )


def get_require_info_response_from_db():
    with get_connection(DB_PATH) as conn:
        admiral_basic = fetch_row(
            conn,
            "SELECT api_member_id, api_firstflag FROM admiral LIMIT 1",
        )
        require_info = fetch_row(
            conn,
            "SELECT * FROM admiral_require_info LIMIT 1",
            ["api_unsetslot_json", "api_extra_supply_json", "api_oss_setting_json"],
        )
        if admiral_basic is None or require_info is None:
            return None

        api_data = {
            "api_basic": {
                "api_member_id": admiral_basic["api_member_id"],
                "api_firstflag": admiral_basic["api_firstflag"],
            },
            "api_slot_item": fetch_rows(
                conn, "SELECT * FROM slot_item ORDER BY api_id"
            ),
            "api_unsetslot": require_info["api_unsetslot_json"],
            "api_kdock": [
                {key: value for key, value in row.items() if key != "member_id"}
                for row in fetch_rows(conn, "SELECT * FROM kdock ORDER BY api_id")
            ],
            "api_useitem": [
                {"api_id": row["api_id"], "api_count": row["api_count"]}
                for row in fetch_rows(conn, "SELECT * FROM useitem ORDER BY api_id")
            ],
            "api_furniture": [
                {key: value for key, value in row.items() if key != "member_id"}
                for row in fetch_rows(conn, "SELECT * FROM furniture ORDER BY api_id")
            ],
            "api_extra_supply": require_info["api_extra_supply_json"],
            "api_oss_setting": require_info["api_oss_setting_json"],
            "api_skin_id": require_info["api_skin_id"],
            "api_position_id": require_info["api_position_id"],
        }
    return create_response_from_data(
        {"api_result": 1, "api_result_msg": "成功", "api_data": api_data}
    )


def get_port_response_from_db():
    with get_connection(DB_PATH) as conn:
        admiral_basic = fetch_row(
            conn,
            "SELECT * FROM admiral LIMIT 1",
            ["api_furniture", "api_pvp"],
        )
        port_state = fetch_row(
            conn,
            "SELECT * FROM admiral_port LIMIT 1",
            ["api_log_json", "api_furniture_affect_items_json"],
        )
        if admiral_basic is None or port_state is None:
            return None

        def strip_member_id(row):
            return {k: v for k, v in row.items() if k != "member_id"}

        api_data = {
            "api_material": [
                strip_member_id(row)
                for row in fetch_rows(conn, "SELECT * FROM material ORDER BY api_id")
            ],
            "api_deck_port": [
                strip_member_id(row)
                for row in fetch_rows(
                    conn,
                    "SELECT * FROM deck_port ORDER BY api_id",
                    ["api_mission", "api_ship"],
                )
            ],
            "api_ndock": [
                {
                    "api_member_id": row["member_id"],
                    "api_id": row["api_id"],
                    "api_state": row["api_state"],
                    "api_ship_id": row["api_ship_id"],
                    "api_complete_time": row["api_complete_time"],
                    "api_complete_time_str": row["api_complete_time_str"],
                    "api_item1": row["api_item1"],
                    "api_item2": row["api_item2"],
                    "api_item3": row["api_item3"],
                    "api_item4": row["api_item4"],
                }
                for row in fetch_rows(conn, "SELECT * FROM ndock ORDER BY api_id")
            ],
            "api_ship": fetch_rows(
                conn,
                "SELECT * FROM owned_ship ORDER BY api_id",
                ["api_slot", "api_onslot", "api_kyouka"],
            ),
            "api_basic": {
                "api_member_id": admiral_basic["api_member_id"],
                "api_nickname": admiral_basic["api_nickname"],
                "api_nickname_id": admiral_basic["api_nickname_id"],
                "api_active_flag": admiral_basic["api_active_flag"],
                "api_starttime": admiral_basic["api_starttime"],
                "api_level": admiral_basic["api_level"],
                "api_rank": admiral_basic["api_rank"],
                "api_experience": admiral_basic["api_experience"],
                "api_fleetname": admiral_basic["api_fleetname"],
                "api_comment": admiral_basic["api_comment"],
                "api_comment_id": admiral_basic["api_comment_id"],
                "api_max_chara": admiral_basic["api_max_chara"],
                "api_max_slotitem": admiral_basic["api_max_slotitem"],
                "api_max_kagu": admiral_basic["api_max_kagu"],
                "api_playtime": admiral_basic["api_playtime"],
                "api_tutorial": admiral_basic["api_tutorial"],
                "api_tutorial_progress": admiral_basic["api_tutorial_progress"],
                "api_furniture": admiral_basic["api_furniture"],
                "api_count_deck": admiral_basic["api_count_deck"],
                "api_count_kdock": admiral_basic["api_count_kdock"],
                "api_count_ndock": admiral_basic["api_count_ndock"],
                "api_pvp": admiral_basic["api_pvp"],
                "api_medals": admiral_basic["api_medals"],
                "api_fcoin": admiral_basic["api_fcoin"],
                "api_st_win": admiral_basic["api_st_win"],
                "api_st_lose": admiral_basic["api_st_lose"],
                "api_pt_win": admiral_basic["api_pt_win"],
                "api_pt_lose": admiral_basic["api_pt_lose"],
                "api_pt_challenged": admiral_basic["api_pt_challenged"],
                "api_pt_challenged_win": admiral_basic["api_pt_challenged_win"],
                "api_firstflag": admiral_basic["api_firstflag"],
                "api_large_dock": admiral_basic["api_large_dock"],
                "api_ms_count": admiral_basic["api_ms_count"],
                "api_ms_success": admiral_basic["api_ms_success"],
            },
            "api_log": port_state["api_log_json"],
            "api_p_bgm_id": port_state["api_p_bgm_id"],
            "api_furniture_affect_items": port_state["api_furniture_affect_items_json"],
            "api_parallel_quest_count": port_state["api_parallel_quest_count"],
            "api_dest_ship_slot": port_state["api_dest_ship_slot"],
        }
    return create_response_from_data(
        {"api_result": 1, "api_result_msg": "成功", "api_data": api_data}
    )


def get_ndock_response_from_db():
    with get_connection(DB_PATH) as conn:
        rows = fetch_rows(conn, "SELECT * FROM ndock ORDER BY api_id")
    api_data = [
        {
            "api_member_id": row["member_id"],
            "api_id": row["api_id"],
            "api_state": row["api_state"],
            "api_ship_id": row["api_ship_id"],
            "api_complete_time": row["api_complete_time"],
            "api_complete_time_str": row["api_complete_time_str"],
            "api_item1": row["api_item1"],
            "api_item2": row["api_item2"],
            "api_item3": row["api_item3"],
            "api_item4": row["api_item4"],
        }
        for row in rows
    ]
    return create_response_from_data(
        {"api_result": 1, "api_result_msg": "成功", "api_data": api_data}
    )


# TODO API设置相关接口
@app.route("/kcsapi/api_start2/get_option_setting", methods=["GET", "POST", "OPTIONS"])
def api_start2_get_option_setting():
    if request.method == "OPTIONS":
        return Response("", status=204)
    return create_response_from_file("api/kcsapi/api_start2/get_option_setting.json")


# TODO API设置相关接口
@app.route("/kcsapi/api_req_member/get_incentive", methods=["GET", "POST", "OPTIONS"])
def api_req_member_get_incentive():
    if request.method == "OPTIONS":
        return Response("", status=204)

    return create_response_from_file("api/kcsapi/api_req_member/get_incentive.json")


# TODO API设置相关接口（改装界面会被概率调用，调用条件不明）
@app.route(
    "/kcsapi/api_req_kaisou/can_preset_slot_select", methods=["GET", "POST", "OPTIONS"]
)
def api_req_kaisou_can_preset_slot_select():
    if request.method == "OPTIONS":
        return Response("", status=204)
    return create_response_from_file(
        "api/kcsapi/api_req_kaisou/can_preset_slot_select.json"
    )


# TODO API设置相关接口 （工廠界面调用）
@app.route(
    "/kcsapi/api_get_member/preset_dev_items", methods=["GET", "POST", "OPTIONS"]
)
def api_get_member_preset_dev_items():
    if request.method == "OPTIONS":
        return Response("", status=204)
    return create_response_from_file("api/kcsapi/api_get_member/preset_dev_items.json")


# 获取全体信息
@app.route("/kcsapi/api_start2/getData", methods=["GET", "POST", "OPTIONS"])
def api_start2_get_data():
    if request.method == "OPTIONS":
        return Response("", status=204)
    response = get_data_response_from_db()
    return (
        response
        if response is not None
        else create_response_from_file("api/kcsapi/api_start2/getData.json")
    )


# 全体信息2
@app.route("/kcsapi/api_get_member/require_info", methods=["GET", "POST", "OPTIONS"])
def api_get_member_require_info():
    if request.method == "OPTIONS":
        return Response("", status=204)
    response = get_require_info_response_from_db()
    return (
        response
        if response is not None
        else create_response_from_file("api/kcsapi/api_get_member/require_info.json")
    )


# 获取母港信息
@app.route("/kcsapi/api_port/port", methods=["GET", "POST", "OPTIONS"])
def api_port_port():
    if request.method == "OPTIONS":
        return Response("", status=204)
    response = get_port_response_from_db()
    return (
        response
        if response is not None
        else create_response_from_file("api/kcsapi/api_port/port.json")
    )


# 预设编成信息
@app.route("/kcsapi/api_get_member/preset_deck", methods=["GET", "POST", "OPTIONS"])
def api_get_member_preset_deck():
    if request.method == "OPTIONS":
        return Response("", status=204)
    return create_response_from_file("api/kcsapi/api_get_member/preset_deck.json")


# 補給
@app.route(
    "/kcsapi/api_req_member/set_oss_condition", methods=["GET", "POST", "OPTIONS"]
)
def api_req_member_set_oss_condition():
    if request.method == "OPTIONS":
        return Response("", status=204)
    return create_response_from_file("api/kcsapi/api_req_member/set_oss_condition.json")


# 装備展開
@app.route("/kcsapi/api_get_member/preset_slot", methods=["GET", "POST", "OPTIONS"])
def api_get_member_preset_slot():
    if request.method == "OPTIONS":
        return Response("", status=204)
    return create_response_from_file("api/kcsapi/api_get_member/preset_slot.json")


# 入渠
@app.route("/kcsapi/api_get_member/ndock", methods=["GET", "POST", "OPTIONS"])
def api_get_member_ndock():
    if request.method == "OPTIONS":
        return Response("", status=204)
    return get_ndock_response_from_db()


# 出撃相关接口
@app.route(
    "/kcsapi/api_get_member/chart_additional_info", methods=["GET", "POST", "OPTIONS"]
)
def api_get_member_chart_additional_info():
    if request.method == "OPTIONS":
        return Response("", status=204)
    return create_response_from_file(
        "api/kcsapi/api_get_member/chart_additional_info.json"
    )


@app.route("/db/admirals")
def db_admirals():
    return {"admirals": query_db("SELECT * FROM admiral")}


@app.route("/db/deck_ships")
def db_deck_ships():
    return {"deck_ships": query_db("SELECT * FROM deck_ship")}


@app.route("/db/owned_ships")
def db_owned_ships():
    return {"owned_ships": query_db("SELECT * FROM owned_ship")}


@app.route("/db/deck_port")
def db_deck_port():
    return {"deck_port": query_db("SELECT * FROM deck_port")}


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8000)
