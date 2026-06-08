import json
import sqlite3

table_name = "mst_furniture"

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

conn = sqlite3.connect("../kcs_api.sqlite3")
cursor = conn.cursor()

columns = data[0].keys()

sql = f"""
INSERT INTO {table_name} ({','.join(columns)})
VALUES ({','.join(['?'] * len(columns))})
"""

cursor.executemany(sql, [tuple(item[col] for col in columns) for item in data])

conn.commit()
conn.close()
