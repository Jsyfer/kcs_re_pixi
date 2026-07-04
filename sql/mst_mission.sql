CREATE TABLE IF NOT EXISTS mst_mission (
    api_id INTEGER PRIMARY KEY,
    api_disp_no TEXT,
    api_maparea_id INTEGER,
    api_name TEXT,
    api_details TEXT,
    api_reset_type INTEGER,
    api_damage_type INTEGER,
    api_time INTEGER,
    api_deck_num INTEGER,
    api_difficulty INTEGER,
    api_use_fuel REAL,
    api_use_bull INTEGER,
    api_win_item1 TEXT,
    api_win_item2 TEXT,
    api_win_mat_level TEXT,
    api_return_flag INTEGER,
    api_sample_fleet TEXT
);