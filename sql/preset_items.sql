CREATE TABLE IF NOT EXISTS preset_items (
    api_preset_no INTEGER PRIMARY KEY,
    api_name TEXT,
    api_selected_mode INTEGER,
    api_lock_flag INTEGER,
    api_slot_ex_flag INTEGER,
    api_slot_item TEXT,
    api_slot_item_ex TEXT
);