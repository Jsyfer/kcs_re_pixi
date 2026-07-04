CREATE TABLE IF NOT EXISTS current_battle_info (
    id INTEGER PRIMARY KEY,
    maparea_id INTEGER,
    mapinfo_no INTEGER,
    current_point INTEGER,
    deck_id INTEGER,
    enemy_info_id INTEGER
);