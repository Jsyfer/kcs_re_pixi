CREATE TABLE IF NOT EXISTS mst_mapinfo (
    api_id INTEGER PRIMARY KEY,
    api_maparea_id INTEGER,
    api_no INTEGER,
    api_name TEXT,
    api_level INTEGER,
    api_opetext TEXT,
    api_infotext TEXT,
    api_item TEXT,
    api_max_maphp INTEGER,
    api_required_defeat_count INTEGER,
    api_sally_flag TEXT,
    admiral_exp INTEGER,
    admiral_exp_boss INTEGER
);