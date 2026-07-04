CREATE TABLE IF NOT EXISTS mst_useitem (
    api_id INTEGER PRIMARY KEY,
    api_usetype INTEGER,
    api_category INTEGER,
    api_name TEXT,
    api_description TEXT,
    api_price INTEGER
);