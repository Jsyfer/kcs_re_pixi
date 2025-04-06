import json
import os
import shutil
from PIL import Image, ImageDraw
import cv2
import numpy as np

base_path = "/Users/jsyfer/GitHub/kcs_re_pixi/"
spritesheet_json = base_path + "assets/kcs2/img/arsenal/arsenal_main.json"

spritesheet_image = spritesheet_json.replace(".json", ".png")
refer_image = "/Users/jsyfer/Downloads/kcs_re/Arsenal4.png"
samples = 5
name_list = [
    "arsenal_main_89",
    "arsenal_main_91",
    "arsenal_main_93",
    "arsenal_main_95",
]


def load_spritesheet(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)
    return data


def get_images_in_json(name_list):
    json_data = load_spritesheet(spritesheet_json)
    spritesheet = Image.open(spritesheet_image)
    result_images = []
    for name, data in json_data["frames"].items():
        x, y = data["frame"]["x"], data["frame"]["y"]
        width, height = data["frame"]["w"], data["frame"]["h"]
        sprite = spritesheet.crop((x, y, x + width, y + height))
        if name in name_list:
            result_images.append({"name": name, "image": sprite})
    return result_images


def find_subimage_position(a_path, b_path):
    # 读取a.png和b.png，包括透明通道（alpha通道）
    a_img = cv2.imread(a_path, cv2.IMREAD_UNCHANGED)
    b_img = cv2.imread(b_path, cv2.IMREAD_UNCHANGED)  # b.png (with alpha)

    # 将透明通道和RGB通道分离开
    a_alpha = a_img[:, :, 3]  # a.png的透明通道
    a_rgb = a_img[:, :, :3]  # a.png的RGB通道
    b_rgb = b_img[:, :, :3]  # b.png的RGB通道

    # 创建掩码，只匹配a.png中不透明的区域
    mask = a_alpha > 0

    # 用模板匹配来找到a.png在b.png中的位置
    result = cv2.matchTemplate(
        b_rgb, a_rgb, cv2.TM_CCORR_NORMED, mask=mask.astype(np.uint8)
    )

    # 找到最大匹配值及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 返回找到的坐标
    return max_loc


refer = Image.open(refer_image)
temp_dir = "temp_coordinate_refer"
os.makedirs(temp_dir)

for item in get_images_in_json(name_list):
    spriteName = item["name"]
    sprite = item["image"]
    sprite_save_path = f"{temp_dir}/{spriteName}.png"
    sprite.save(sprite_save_path)
    position = find_subimage_position(sprite_save_path, refer_image)

    draw = ImageDraw.Draw(refer)
    x = position[0]
    y = position[1]
    coordinate_info = f"{spriteName}: {x},{y}"
    print(coordinate_info)
    draw.rectangle((x, y, x + sprite.size[0], y + sprite.size[1]), outline="red")
    draw.text(
        (x + 5, y + 5),
        f"{x},{y}",
        fill="yellow",
        font_size=15,
        stroke_width=2,
        stroke_fill="black",
    )

refer.save("result.png")
shutil.rmtree(temp_dir)
