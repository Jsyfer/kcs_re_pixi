DROP TABLE IF EXISTS quest;

CREATE TABLE IF NOT EXISTS quest (
    api_no INTEGER PRIMARY KEY,
    api_category INTEGER,
    api_type INTEGER,
    api_label_type INTEGER,
    api_state INTEGER,
    api_title TEXT,
    api_detail TEXT,
    api_voice_id INTEGER,
    api_lost_badges INTEGER,
    api_get_material TEXT,
    api_bonus_flag INTEGER,
    api_progress_flag INTEGER,
    api_invalid_flag INTEGER
);