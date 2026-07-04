CREATE TABLE IF NOT EXISTS map_point_info (
    id INTEGER PRIMARY KEY,
    maparea_id INTEGER,
    mapinfo_no INTEGER,
    point_no INTEGER,
    passed INTEGER,
    color_no INTEGER,
    event_id INTEGER,
    event_kind INTEGER,
    rashin_flg INTEGER,
    rashin_id INTEGER,
    next_points TEXT
);