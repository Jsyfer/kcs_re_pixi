import json
import os
import re

ROOT_PATH = "../assets/kcs2/resources/ship"
CATEGORY_LIST = ["full", "banner", "supply_character", "card"]

resources_mapping = {
    "ship": [],
    "furniture": [
        {"api_id": 494, "furniture": "494_1648.png"},
        {"api_id": 502, "furniture": "502_8118.png"},
        {"api_id": 491, "furniture": "491_9688.png"},
        {"api_id": 499, "furniture": "499_8458.png"},
        {"api_id": 458, "furniture": "458_3958.png"},
        {"api_id": 498, "furniture": "498_8534.png"},
    ],
}


def set_ship_info(api_id, category, value):
    for ship in resources_mapping["ship"]:
        if ship["api_id"] == api_id:
            ship[category] = value
            return
    ship = {"api_id": api_id, category: value}
    resources_mapping["ship"].append(ship)


# iterate root path
for category in CATEGORY_LIST:
    for file in os.listdir(os.path.join(ROOT_PATH, category)):
        filename = os.fsdecode(file)
        # generate api_id from file name
        api_id = int(re.search(r"(\d+)_", filename)[1])
        # set filename identifier by category
        identifier = filename
        if category == "full":
            # print(filename)
            identifier = re.search(r"\d+_(d?_?\d+)_?", filename)[1]
        set_ship_info(api_id, category, identifier)

# dump result file
with open("../src/resources_mapping.json", "w") as f:
    json.dump(resources_mapping, f, indent=4)
