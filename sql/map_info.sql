DROP TABLE IF EXISTS map_info;

CREATE TABLE IF NOT EXISTS map_info (
    api_id INTEGER PRIMARY KEY,
    api_cleared INTEGER,
    api_defeat_count INTEGER,
    api_required_defeat_count INTEGER,
    api_gauge_type INTEGER,
    api_gauge_num INTEGER,
    api_air_base_decks INTEGER,
    api_eventmap TEXT,
    api_sally_flag TEXT,
    api_s_no INTEGER
);