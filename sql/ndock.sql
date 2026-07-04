CREATE TABLE IF NOT EXISTS ndock (
    member_id INTEGER,
    api_id INTEGER PRIMARY KEY,
    api_state INTEGER,
    api_ship_id INTEGER,
    api_complete_time INTEGER,
    api_complete_time_str TEXT,
    api_item1 INTEGER,
    api_item2 INTEGER,
    api_item3 INTEGER,
    api_item4 INTEGER
);