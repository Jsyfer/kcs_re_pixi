import json
import os
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_DIR = BASE_DIR / "instance"
DB_PATH = DB_DIR / "kcs_api.db"
SCHEMA_PATH = BASE_DIR / "db_schema.sql"


def get_connection(db_path: str | Path | None = None) -> sqlite3.Connection:
    path = Path(db_path or DB_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def initialize_database(db_path: str | Path | None = None) -> sqlite3.Connection:
    conn = get_connection(db_path)
    with open(SCHEMA_PATH, encoding="utf-8") as schema_file:
        conn.executescript(schema_file.read())
    conn.commit()
    return conn


def json_dumps(value):
    return json.dumps(value, ensure_ascii=False) if value is not None else None


def normalize_value(value):
    if isinstance(value, (dict, list)):
        return json_dumps(value)
    return value


def insert_rows(conn, table: str, columns: list[str], rows: list[dict]):
    if not rows:
        return
    placeholders = ",".join("?" for _ in columns)
    sql = (
        f"INSERT OR REPLACE INTO {table} ({','.join(columns)}) VALUES ({placeholders})"
    )
    values = []
    for item in rows:
        row = []
        for col in columns:
            if col == "raw_json":
                row.append(json_dumps(item))
            else:
                row.append(normalize_value(item.get(col)))
        values.append(row)
    conn.executemany(sql, values)
    conn.commit()


def load_master_data(conn, getdata_path: str | Path):
    with open(getdata_path, encoding="utf-8") as fp:
        api_data = json.load(fp)["api_data"]

    insert_rows(
        conn,
        "master_ship",
        [
            "api_id",
            "api_sortno",
            "api_sort_id",
            "api_name",
            "api_yomi",
            "api_stype",
            "api_ctype",
            "api_afterlv",
            "api_aftershipid",
            "api_soku",
            "api_leng",
            "api_slot_num",
            "api_buildtime",
            "api_backs",
            "api_afterfuel",
            "api_afterbull",
            "api_fuel_max",
            "api_bull_max",
            "raw_json",
        ],
        api_data.get("api_mst_ship", []),
    )

    insert_rows(
        conn,
        "master_slotitem",
        [
            "api_id",
            "api_sortno",
            "api_name",
            "api_type",
            "api_leng",
            "api_rare",
            "api_usebull",
            "api_version",
            "raw_json",
        ],
        api_data.get("api_mst_slotitem", []),
    )

    insert_rows(
        conn,
        "master_stype",
        [
            "api_id",
            "api_sortno",
            "api_name",
            "api_scnt",
            "api_kcnt",
            "api_equip_type",
            "raw_json",
        ],
        api_data.get("api_mst_stype", []),
    )

    insert_rows(
        conn,
        "master_useitem",
        [
            "api_id",
            "api_usetype",
            "api_category",
            "api_name",
            "api_description",
            "api_price",
            "raw_json",
        ],
        api_data.get("api_mst_useitem", []),
    )

    insert_rows(
        conn,
        "master_furniture",
        [
            "api_id",
            "api_furniture_type",
            "api_furniture_no",
            "api_furniture_id",
            "api_title",
            "api_description",
            "api_price",
            "api_rarity",
            "api_version",
            "raw_json",
        ],
        api_data.get("api_mst_furniture", []),
    )

    insert_rows(
        conn,
        "master_maparea",
        ["api_id", "api_name", "api_type", "raw_json"],
        api_data.get("api_mst_maparea", []),
    )

    insert_rows(
        conn,
        "master_mapinfo",
        [
            "api_id",
            "api_name",
            "api_maparea_id",
            "api_no",
            "api_level",
            "api_max_maphp",
            "api_required_defeat_count",
            "api_sally_flag",
            "raw_json",
        ],
        api_data.get("api_mst_mapinfo", []),
    )

    insert_rows(
        conn,
        "master_mission",
        [
            "api_id",
            "api_name",
            "api_maparea_id",
            "api_deck_num",
            "api_time",
            "api_use_fuel",
            "api_use_bull",
            "raw_json",
        ],
        api_data.get("api_mst_mission", []),
    )

    insert_rows(
        conn,
        "master_shipgraph",
        ["api_id", "api_filename", "api_version", "raw_json"],
        api_data.get("api_mst_shipgraph", []),
    )

    exslot_ship = api_data.get("api_mst_equip_exslot_ship", {})
    if exslot_ship:
        rows = [
            {
                "api_ship_id": int(ship_id),
                "exslot_json": json_dumps(value),
                "raw_json": json_dumps({ship_id: value}),
            }
            for ship_id, value in exslot_ship.items()
        ]
        insert_rows(
            conn,
            "master_equip_exslot_ship",
            ["api_ship_id", "exslot_json", "raw_json"],
            rows,
        )

    conn.commit()


def load_require_info(conn, require_info_path: str | Path):
    with open(require_info_path, encoding="utf-8") as fp:
        api_data = json.load(fp)["api_data"]

    basic = api_data.get("api_basic", {})
    member_id = basic.get("api_member_id")
    admiral_row = {
        "member_id": member_id,
        "api_member_id": member_id,
        "api_firstflag": basic.get("api_firstflag"),
        "raw_json": json_dumps(api_data),
    }
    insert_rows(conn, "admiral", list(admiral_row.keys()), [admiral_row])

    admiral_require_info_row = {
        "member_id": member_id,
        "api_unsetslot_json": json_dumps(api_data.get("api_unsetslot")),
        "api_extra_supply_json": json_dumps(api_data.get("api_extra_supply")),
        "api_oss_setting_json": json_dumps(api_data.get("api_oss_setting")),
        "api_skin_id": api_data.get("api_skin_id"),
        "api_position_id": api_data.get("api_position_id"),
        "raw_json": json_dumps(api_data),
    }
    insert_rows(
        conn,
        "admiral_require_info",
        list(admiral_require_info_row.keys()),
        [admiral_require_info_row],
    )

    insert_rows(
        conn,
        "slot_item",
        ["api_id", "api_slotitem_id", "api_locked", "api_level", "api_alv", "raw_json"],
        api_data.get("api_slot_item", []),
    )

    insert_rows(
        conn,
        "ndock",
        [
            "member_id",
            "api_id",
            "api_state",
            "api_ship_id",
            "api_complete_time",
            "api_complete_time_str",
            "api_item1",
            "api_item2",
            "api_item3",
            "api_item4",
            "api_item5",
            "raw_json",
        ],
        api_data.get("api_kdock", []),
    )

    insert_rows(
        conn,
        "require_info_meta",
        [
            "member_id",
            "api_unsetslot_json",
            "api_extra_supply_json",
            "api_oss_setting_json",
            "api_skin_id",
            "api_position_id",
            "raw_json",
        ],
        [
            {
                "member_id": basic.get("api_member_id"),
                "api_unsetslot_json": json_dumps(api_data.get("api_unsetslot")),
                "api_extra_supply_json": json_dumps(api_data.get("api_extra_supply")),
                "api_oss_setting_json": json_dumps(api_data.get("api_oss_setting")),
                "api_skin_id": api_data.get("api_skin_id"),
                "api_position_id": api_data.get("api_position_id"),
                "raw_json": json_dumps(api_data),
            }
        ],
    )

    insert_rows(
        conn,
        "useitem",
        ["member_id", "api_id", "api_count", "raw_json"],
        [
            {
                "member_id": basic.get("api_member_id"),
                "api_id": item.get("api_id"),
                "api_count": item.get("api_count"),
                "raw_json": item,
            }
            for item in api_data.get("api_useitem", [])
        ],
    )

    insert_rows(
        conn,
        "furniture",
        [
            "member_id",
            "api_id",
            "api_furniture_type",
            "api_furniture_no",
            "api_furniture_id",
            "raw_json",
        ],
        [
            {
                "member_id": basic.get("api_member_id"),
                "api_id": item.get("api_id"),
                "api_furniture_type": item.get("api_furniture_type"),
                "api_furniture_no": item.get("api_furniture_no"),
                "api_furniture_id": item.get("api_furniture_id"),
                "raw_json": item,
            }
            for item in api_data.get("api_furniture", [])
        ],
    )
    conn.commit()


def load_port_data(conn, port_path: str | Path):
    with open(port_path, encoding="utf-8") as fp:
        api_data = json.load(fp)["api_data"]

    basic = api_data.get("api_basic", {})
    member_id = basic.get("api_member_id")
    admiral_row = {
        "member_id": member_id,
        "api_member_id": member_id,
        "api_firstflag": basic.get("api_firstflag"),
        "api_nickname": basic.get("api_nickname"),
        "api_nickname_id": basic.get("api_nickname_id"),
        "api_level": basic.get("api_level"),
        "api_experience": basic.get("api_experience"),
        "api_playtime": basic.get("api_playtime"),
        "api_fcoin": basic.get("api_fcoin"),
        "api_medals": basic.get("api_medals"),
        "api_fleetname": basic.get("api_fleetname"),
        "api_active_flag": basic.get("api_active_flag"),
        "api_tutorial": basic.get("api_tutorial"),
        "api_tutorial_progress": basic.get("api_tutorial_progress"),
        "api_max_chara": basic.get("api_max_chara"),
        "api_max_slotitem": basic.get("api_max_slotitem"),
        "api_max_kagu": basic.get("api_max_kagu"),
        "api_count_deck": basic.get("api_count_deck"),
        "api_count_kdock": basic.get("api_count_kdock"),
        "api_count_ndock": basic.get("api_count_ndock"),
        "api_pvp": basic.get("api_pvp"),
        "api_rank": basic.get("api_rank"),
        "api_st_win": basic.get("api_st_win"),
        "api_st_lose": basic.get("api_st_lose"),
        "api_pt_win": basic.get("api_pt_win"),
        "api_pt_lose": basic.get("api_pt_lose"),
        "api_pt_challenged": basic.get("api_pt_challenged"),
        "api_pt_challenged_win": basic.get("api_pt_challenged_win"),
        "api_starttime": basic.get("api_starttime"),
        "api_comment": basic.get("api_comment"),
        "api_comment_id": basic.get("api_comment_id"),
        "raw_json": json_dumps(api_data),
    }
    insert_rows(conn, "admiral", list(admiral_row.keys()), [admiral_row])

    admiral_port_row = {
        "member_id": member_id,
        "api_p_bgm_id": api_data.get("api_p_bgm_id"),
        "api_parallel_quest_count": api_data.get("api_parallel_quest_count"),
        "api_dest_ship_slot": api_data.get("api_dest_ship_slot"),
        "api_log_json": json_dumps(api_data.get("api_log")),
        "api_furniture_affect_items_json": json_dumps(
            api_data.get("api_furniture_affect_items")
        ),
        "raw_json": json_dumps(api_data),
    }
    insert_rows(
        conn,
        "admiral_port",
        list(admiral_port_row.keys()),
        [admiral_port_row],
    )

    insert_rows(
        conn,
        "material",
        ["member_id", "api_id", "api_value", "raw_json"],
        api_data.get("api_material", []),
    )

    deck_rows = api_data.get("api_deck_port", [])
    insert_rows(
        conn,
        "deck_port",
        [
            "member_id",
            "api_id",
            "api_name",
            "api_name_id",
            "api_mission",
            "api_flagship",
            "api_ship",
            "raw_json",
        ],
        deck_rows,
    )

    deck_ship_rows = []
    deck_mission_rows = []
    for deck in deck_rows:
        deck_id = deck.get("api_id")
        for position, ship_id in enumerate(deck.get("api_ship", []) or [], start=1):
            deck_ship_rows.append(
                {
                    "member_id": member_id,
                    "deck_id": deck_id,
                    "position": position,
                    "api_ship_id": ship_id,
                }
            )
        for mission_index, mission_id in enumerate(
            deck.get("api_mission", []) or [], start=1
        ):
            deck_mission_rows.append(
                {
                    "member_id": member_id,
                    "deck_id": deck_id,
                    "mission_index": mission_index,
                    "api_mission_id": mission_id,
                }
            )
    insert_rows(
        conn,
        "deck_ship",
        ["member_id", "deck_id", "position", "api_ship_id"],
        deck_ship_rows,
    )
    insert_rows(
        conn,
        "deck_mission",
        ["member_id", "deck_id", "mission_index", "api_mission_id"],
        deck_mission_rows,
    )

    insert_rows(
        conn,
        "ndock",
        [
            "member_id",
            "api_id",
            "api_state",
            "api_ship_id",
            "api_complete_time",
            "api_complete_time_str",
            "api_item1",
            "api_item2",
            "api_item3",
            "api_item4",
            "raw_json",
        ],
        api_data.get("api_ndock", []),
    )

    ship_rows = api_data.get("api_ship", [])
    insert_rows(
        conn,
        "owned_ship",
        [
            "api_id",
            "api_ship_id",
            "api_sortno",
            "api_lv",
            "api_exp",
            "api_nowhp",
            "api_maxhp",
            "api_soku",
            "api_leng",
            "api_slot",
            "api_onslot",
            "api_slot_ex",
            "api_kyouka",
            "api_backs",
            "api_fuel",
            "api_bull",
            "api_slotnum",
            "api_ndock_time",
            "api_ndock_item",
            "api_srate",
            "api_cond",
            "api_karyoku",
            "api_raisou",
            "api_taiku",
            "api_soukou",
            "api_kaihi",
            "api_taisen",
            "api_sakuteki",
            "api_lucky",
            "api_locked",
            "api_locked_equip",
            "raw_json",
        ],
        ship_rows,
    )

    ship_slot_rows = []
    ship_kyouka_rows = []
    for ship in ship_rows:
        ship_id = ship.get("api_id")
        slot_items = ship.get("api_slot", []) or []
        onslot_values = ship.get("api_onslot", []) or []
        for slot_index, api_slotitem_id in enumerate(slot_items, start=1):
            ship_slot_rows.append(
                {
                    "member_id": member_id,
                    "api_id": ship_id,
                    "slot_index": slot_index,
                    "api_slotitem_id": api_slotitem_id,
                    "api_onslot": (
                        onslot_values[slot_index - 1]
                        if slot_index - 1 < len(onslot_values)
                        else None
                    ),
                }
            )
        for kyouka_index, kyouka_value in enumerate(
            ship.get("api_kyouka", []) or [], start=1
        ):
            ship_kyouka_rows.append(
                {
                    "member_id": member_id,
                    "api_id": ship_id,
                    "kyouka_index": kyouka_index,
                    "kyouka_value": kyouka_value,
                }
            )
    insert_rows(
        conn,
        "ship_slot",
        ["member_id", "api_id", "slot_index", "api_slotitem_id", "api_onslot"],
        ship_slot_rows,
    )
    insert_rows(
        conn,
        "ship_kyouka",
        ["member_id", "api_id", "kyouka_index", "kyouka_value"],
        ship_kyouka_rows,
    )

    insert_rows(
        conn,
        "player_port",
        [
            "member_id",
            "api_p_bgm_id",
            "api_parallel_quest_count",
            "api_dest_ship_slot",
            "log_json",
            "furniture_affect_items_json",
            "raw_json",
        ],
        [
            {
                "member_id": basic.get("api_member_id"),
                "api_p_bgm_id": api_data.get("api_p_bgm_id"),
                "api_parallel_quest_count": api_data.get("api_parallel_quest_count"),
                "api_dest_ship_slot": api_data.get("api_dest_ship_slot"),
                "log_json": json_dumps(api_data.get("api_log")),
                "furniture_affect_items_json": json_dumps(
                    api_data.get("api_furniture_affect_items")
                ),
                "raw_json": json_dumps(api_data),
            }
        ],
    )
    conn.commit()


def initialize_and_load_data(
    getdata_path: str | Path,
    require_info_path: str | Path,
    port_path: str | Path,
    db_path: str | Path | None = None,
) -> sqlite3.Connection:
    conn = initialize_database(db_path)
    load_master_data(conn, getdata_path)
    load_require_info(conn, require_info_path)
    load_port_data(conn, port_path)
    return conn


def query_rows(conn, sql: str, params: tuple = ()) -> list[dict]:
    cursor = conn.execute(sql, params)
    rows = [dict(row) for row in cursor.fetchall()]
    return rows
