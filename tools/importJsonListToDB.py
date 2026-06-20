import json
import sqlite3

table_name = "preset_items"

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

conn = sqlite3.connect("../kcs_api.sqlite3")
cursor = conn.cursor()

# Find the dictionary with the most keys
max_dict = max(data, key=len, default={})
columns = list(max_dict.keys())

sql = f"""
INSERT INTO {table_name} ({','.join(columns)})
VALUES ({','.join(['?'] * len(columns))})
"""

rows = []
for item in data:
    row = []
    for col in columns:
        value = item.get(col)
        if isinstance(value, list) or isinstance(value, dict):
            value = json.dumps(value)
        row.append(value)
    rows.append(tuple(row))

cursor.executemany(sql, rows)

conn.commit()
conn.close()
