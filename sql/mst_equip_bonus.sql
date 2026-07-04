CREATE TABLE IF NOT EXISTS mst_equip_bonus (
    id INTEGER PRIMARY KEY,
    item_id INTEGER,
    ship_id TEXT,
    ship_class TEXT,
    item_lv INTEGER,
    karyoku INTEGER,
    raisou INTEGER,
    taiku INTEGER,
    soukou INTEGER,
    leng INTEGER,
    soku INTEGER,
    sakuteki INTEGER,
    kaihi INTEGER,
    taisen INTEGER,
    not_duplicate INTEGER
);