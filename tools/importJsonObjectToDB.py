import json
import sqlite3
from typing import Any

table_name = "deck"

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

conn = sqlite3.connect("../kcs_api.sqlite3")
cursor = conn.cursor()

first_item = next(iter(data.values()))
columns = ["id"] + list(first_item.keys())

sql = f"""
INSERT INTO {table_name} ({','.join(columns)})
VALUES ({','.join(['?'] * len(columns))})
"""

rows = []
for key, item in data.items():
    row: list[Any] = [int(key)]

    for col in columns[1:]:
        value = item.get(col)
        if isinstance(value, (list, dict)):
            value = json.dumps(value)
        row.append(value)

    rows.append(tuple(row))

cursor.executemany(sql, rows)

conn.commit()
conn.close()
