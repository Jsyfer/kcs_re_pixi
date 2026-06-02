from flask import Flask, Response, render_template, request, send_from_directory
import time
import json
import os
import requests
from pathlib import Path

from database import DB_PATH, get_connection, initialize_database

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
    return create_response_from_file("api/kcsapi/api_start2/getData.json")


# 全体信息2
@app.route("/kcsapi/api_get_member/require_info", methods=["GET", "POST", "OPTIONS"])
def api_get_member_require_info():
    if request.method == "OPTIONS":
        return Response("", status=204)
    return create_response_from_file("api/kcsapi/api_get_member/require_info.json")


# 获取母港信息
@app.route("/kcsapi/api_port/port", methods=["GET", "POST", "OPTIONS"])
def api_port_port():
    if request.method == "OPTIONS":
        return Response("", status=204)
    return create_response_from_file("api/kcsapi/api_port/port.json")


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
    return create_response_from_file("api/kcsapi/api_get_member/ndock.json")


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
