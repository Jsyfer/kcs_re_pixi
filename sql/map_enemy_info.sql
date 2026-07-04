CREATE TABLE IF NOT EXISTS map_enemy_info (
    id INTEGER PRIMARY KEY,
    maparea_id INTEGER,
    mapinfo_no INTEGER,
    point_no INTEGER,
    pattern TEXT,
    enemy TEXT,
    equip TEXT,
    exp INTEGER,
    formation INTEGER
);