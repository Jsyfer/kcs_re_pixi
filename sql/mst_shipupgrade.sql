CREATE TABLE IF NOT EXISTS mst_shipupgrade (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    api_id INTEGER,
    api_arms_mat_count INTEGER,
    api_aviation_mat_count INTEGER,
    api_catapult_count INTEGER,
    api_current_ship_id INTEGER,
    api_drawing_count INTEGER,
    api_original_ship_id INTEGER,
    api_report_count INTEGER,
    api_sortno INTEGER,
    api_tech_count INTEGER,
    api_upgrade_level INTEGER,
    api_upgrade_type INTEGER
);