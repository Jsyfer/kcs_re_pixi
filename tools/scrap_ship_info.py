from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import logging
import json
import time
from pathlib import Path

logging.basicConfig(
    filename="./tools/scrap_ship_info.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    level=logging.DEBUG,
)


def merge_json_files(input_dir, output_file_path):
    combined_list = []
    path = Path(input_dir)

    # Loop through all files ending with .json in the directory
    for file_path in path.glob("*.json"):
        # Skip the output file if it happens to be in the same folder
        if file_path.resolve() == Path(output_file_path).resolve():
            continue

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                combined_list.append(data)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Skipping {file_path.name} due to an error: {e}")

    # Save the accumulated list to the new JSON file
    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(combined_list, f, indent=4)

    print(f"Successfully saved {len(combined_list)} files into {output_file_path}")


url = "https://wikiwiki.jp/kancolle/%E8%89%A6%E8%88%B9"

ship_link_list = []

retry_strategy = Retry(
    total=5,
    status_forcelist=[429, 500, 502, 503, 504],
    backoff_factor=1,  # 重试间隔：1s, 2s, 4s, 8s... 避免持续冲击服务器
    respect_retry_after_header=True,  # 遵守服务器 429 响应中的 Retry-After 头
)

# 2. 挂载到 Session
adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)

# 取得网页数据
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:136.0) Gecko/20100101 Firefox/136.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://wikiwiki.jp",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Referer": url,
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i",
    "TE": "trailers",
}

response = requests.get(url, headers=headers)

# 获取shiplist
table = (
    BeautifulSoup(response.text, "html.parser")
    .find("div", {"class": "h-scrollable"})
    .find("table")
    .find("tbody")
    .find_all("tr")
)

for row in table:
    row_obj = row.find_all()
    third_item_text = row_obj[2].text.strip()
    if (
        third_item_text is None
        or third_item_text == ""
        or third_item_text == "艦名"
        or third_item_text == "レア"
    ):
        continue
    link = row_obj[2].find("a")["href"]
    ship_link_list.append("https://wikiwiki.jp" + link)


with open(
    "./tools/scrapped_link_list.txt", "a+", encoding="utf-8"
) as scrapped_link_list_file:
    scrapped_link_list = scrapped_link_list_file.read().splitlines()
    # scrape for each ship
    ship_result_list = []
    for ship_link in ship_link_list:
        ship_result_dict = {}
        logging.info(ship_link)
        if ship_link in scrapped_link_list:
            logging.info("Already scraped, skip")
            continue
        else:
            scrapped_link_list_file.write(ship_link + "\n")

        time.sleep(2)  # 避免频繁请求被服务器封禁
        try:
            # 使用配置好重试策略的 http 替代原来的 requests
            ship_response = http.get(ship_link, headers=headers)
            ship_response.raise_for_status()  # 确保非200状态码抛出异常触发重试
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch {ship_link}: {e}")
            continue  # 若重试耗尽仍失败，跳过该舰娘继续下一个

        ship_table = (
            BeautifulSoup(ship_response.text, "html.parser")
            .find("div", {"class": "h-scrollable"})
            .find("table")
            .find("tbody")
            .find_all("tr")
        )

        sort_id = "0"
        for status_row in ship_table:
            row_obj = status_row.find_all()
            first_item_text = row_obj[0].text.strip()
            if first_item_text.startswith("No."):
                sort_id = first_item_text.replace("No.", "")
                ship_result_dict["api_sortno"] = sort_id
            elif first_item_text == "回避":
                kaihi = row_obj[1].text.strip().split("/")
                ship_result_dict["min_kaihi"] = kaihi[0].strip()
                ship_result_dict["max_kaihi"] = kaihi[1].strip()
            elif first_item_text == "搭載" and row_obj[1].text.strip() != "装備":
                if row_obj[3].text.strip() == "0":
                    ship_result_dict["min_taisen"] = 0
                    ship_result_dict["max_taisen"] = 0
                else:
                    taisen = row_obj[3].text.strip().split("/")
                    ship_result_dict["min_taisen"] = taisen[0].strip()
                    ship_result_dict["max_taisen"] = taisen[1].strip()
            elif first_item_text == "速力":
                sakuteki = row_obj[3].text.strip().split("/")
                ship_result_dict["min_sakuteki"] = sakuteki[0].strip()
                ship_result_dict["max_sakuteki"] = sakuteki[1].strip()
            else:
                continue
        with open(f"./tools/ship_result_temp/{sort_id}.json", "w") as json_file:
            json.dump(ship_result_dict, json_file)
        ship_result_list.append(ship_result_dict)


merge_json_files("./tools/ship_result_temp", "./ship_result_list.json")
