import json
import sqlite3

table_name = "mst_ship"

with open("./tools/ship_result_list.json", encoding="utf-8") as f:
    data = json.load(f)

conn = sqlite3.connect("./kcs_api.sqlite3")
cursor = conn.cursor()

# Find the dictionary with the most keys
max_dict = max(data, key=len, default={})
columns = list(max_dict.keys())

condition_col = "api_sortno"
update_columns = [col for col in columns if col != condition_col]


rows = []
for ship in data:
    sql = f"UPDATE {table_name} SET min_kaihi = {ship['min_kaihi']},max_kaihi = {ship['max_kaihi']},min_taisen = {ship['min_taisen']},max_taisen = {ship['max_taisen']},min_sakuteki = {ship['min_sakuteki']},max_sakuteki = {ship['max_sakuteki']} WHERE api_sortno = {ship['api_sortno']};"
    print(sql)
    cursor.execute(sql)

conn.commit()
conn.close()
