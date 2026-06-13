import math

AIRCRAFT_EXP_TABLE = [
    0,
    10,
    25,
    40,
    55,
    70,
    85,
    100,
    121,
]

AIRCRAFT_LEVEL_BONUS = {
    6: [0, 0, 2, 5, 9, 14, 14, 22, 22],
    7: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    8: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    11: [0, 1, 1, 1, 1, 3, 3, 6, 6],
    26: [0, 0, 2, 5, 9, 14, 14, 22, 22],
    45: [0, 0, 2, 5, 9, 14, 14, 22, 22],
    47: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    48: [0, 0, 2, 5, 9, 14, 14, 22, 22],
    56: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    57: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    58: [0, 0, 0, 0, 0, 0, 0, 0, 0],
}

TP_SHIP_TYPE_BONUS = {
    2: [5.0, 3.5, 2.0],  # 駆逐艦
    3: [2.0, 1.4, 0.8],  # 軽巡洋艦
    6: [4.0, 2.8, 1.6],  # 航空巡洋艦
    10: [7.0, 4.9, 2.8],  # 航空戦艦
    16: [9.0, 6.3, 3.6],  # 水上機母艦
    17: [12.0, 8.4, 4.8],  # 揚陸艦
    20: [7.0, 4.9, 2.8],  # 潜水母艦
    21: [6.0, 4.2, 2.4],  # 練習巡洋艦
    22: [15.0, 10.5, 6.0],  # 補給艦
    14: [1.0, 0.7, 0.4],  # 潜水空母
    # 4: [1.0, 0.7, 0.4],  # 重雷装巡洋艦 TODO 效果量不明
    # 5: [1.0, 0.7, 0.4],  # 重巡洋艦 TODO 效果量不明
    # 7: [1.0, 0.7, 0.4],  # 軽空母 TODO 效果量不明
    # 8: [1.0, 0.7, 0.4],  # 戦艦 TODO 效果量不明
    # 11: [1.0, 0.7, 0.4],  # 正規空母 TODO 效果量不明
    # 13: [1.0, 0.7, 0.4],  # 潜水艦 TODO 效果量不明
    # 18: [1.0, 0.7, 0.4],  # 装甲空母 TODO 效果量不明
    # 19: [1.0, 0.7, 0.4],  # 工作艦 TODO 效果量不明
}

TP_EQUIP_TYPE_BONUS = {
    167: [2.0, 1.4, 0.8],  # 特二式内火艇
    75: [5.0, 3.5, 2.0],  # ドラム缶(輸送用)
    166: [8.0, 5.6, 3.2],  # 大発動艇(八九式中戦車&陸戦隊)
    436: [8.0, 5.6, 3.2],  # 大発動艇(II号戦車/北アフリカ仕様) TODO 效果量不明
    68: [8.0, 5.6, 3.2],  # 大発動艇
    230: [8.0, 5.6, 3.2],  # 特大発動艇+戦車第11連隊
    449: [8.0, 5.6, 3.2],  # 特大発動艇+一式砲戦車 TODO 效果量不明
    482: [8.0, 5.6, 3.2],  # 特大発動艇+Ⅲ号戦車(北アフリカ仕様) TODO 效果量不明
    494: [8.0, 5.6, 3.2],  # 特大発動艇+チハ TODO 效果量不明
    495: [8.0, 5.6, 3.2],  # 特大発動艇+チハ改 TODO 效果量不明
    514: [8.0, 5.6, 3.2],  # 特大発動艇+Ⅲ号戦車J型 TODO 效果量不明
    193: [8.0, 5.6, 3.2],  # 特大発動艇
    145: [1.0, 0.7, 0.3],  # 戦闘糧食 TODO 效果量不明
    241: [1.0, 0.7, 0.3],  # 戦闘糧食(特別なおにぎり) TODO 效果量不明
    150: [1.0, 0.7, 0.3],  # 秋刀魚の缶詰 TODO 效果量不明
}


# 获取制空值
def get_tyku(
    equips_data,
    landbase_status=0,
):
    min_tyku = 0
    max_tyku = 0
    basic_tyku = 0
    recon_bonus = 1.0

    for equip_group in equips_data:
        if not equip_group:
            continue

        for equip_data in equip_group:
            if not equip_data:
                continue

            _equip, equip, onslot = equip_data

            if onslot is None or onslot < 1:
                continue

            temp_tyku = 0.0
            temp_alv = _equip.api_alv

            level_factor = (
                0.25
                if equip.api_tyku > 3 and equip.api_baku > 0
                else 0.2 if equip.api_tyku > 3 else 0
            )

            equip_type = equip.api_type[2]

            # 艦上機、水戦、水爆等
            if equip_type in [6, 7, 45, 47, 57] or (
                equip_type == 26 and equip.api_tyku > 0
            ):
                temp_tyku += math.sqrt(onslot) * (
                    equip.api_tyku + _equip.api_level * level_factor
                )
                temp_tyku += AIRCRAFT_LEVEL_BONUS[equip_type][temp_alv]

                basic_tyku += math.floor(math.sqrt(onslot) * equip.api_tyku)

                min_tyku += math.floor(
                    temp_tyku + math.sqrt(AIRCRAFT_EXP_TABLE[temp_alv] / 10)
                )

                max_tyku += math.floor(
                    temp_tyku + math.sqrt((AIRCRAFT_EXP_TABLE[temp_alv + 1] - 1) / 10)
                )

            # 水爆、飛行艇
            elif equip_type in [8, 11]:
                temp_tyku += math.sqrt(onslot) * equip.api_tyku
                temp_tyku += AIRCRAFT_LEVEL_BONUS[equip_type][temp_alv]

                basic_tyku += math.floor(math.sqrt(onslot) * equip.api_tyku)

                min_tyku += math.floor(
                    temp_tyku + math.sqrt(AIRCRAFT_EXP_TABLE[temp_alv] / 10)
                )

                max_tyku += math.floor(
                    temp_tyku + math.sqrt((AIRCRAFT_EXP_TABLE[temp_alv + 1] - 1) / 10)
                )

            # 陸戦
            elif equip_type == 48:
                landbase_bonus = 0

                if landbase_status == 1:
                    landbase_bonus = 1.5 * equip.api_houk
                elif landbase_status == 2:
                    landbase_bonus = equip.api_houk + 2 * equip.api_houm

                temp_tyku += math.sqrt(onslot) * (
                    equip.api_tyku + landbase_bonus + _equip.api_level * level_factor
                )

                temp_tyku += AIRCRAFT_LEVEL_BONUS[equip_type][temp_alv]

                basic_tyku += math.floor(math.sqrt(onslot) * equip.api_tyku)

                min_tyku += math.floor(
                    temp_tyku + math.sqrt(AIRCRAFT_EXP_TABLE[temp_alv] / 10)
                )

                max_tyku += math.floor(
                    temp_tyku + math.sqrt((AIRCRAFT_EXP_TABLE[temp_alv + 1] - 1) / 10)
                )

            # 偵察機
            elif equip_type in [10, 41]:
                if landbase_status == 2:
                    saku = equip.api_saku

                    if saku >= 9:
                        recon_bonus = max(recon_bonus, 1.16)
                    elif saku == 8:
                        recon_bonus = max(recon_bonus, 1.13)
                    else:
                        recon_bonus = max(recon_bonus, 1.10)

                elif landbase_status == 1:
                    temp_tyku += math.sqrt(onslot) * equip.api_tyku

                    min_tyku += math.floor(
                        temp_tyku + math.sqrt(AIRCRAFT_EXP_TABLE[temp_alv] / 10)
                    )

                    max_tyku += math.floor(
                        temp_tyku
                        + math.sqrt((AIRCRAFT_EXP_TABLE[temp_alv + 1] - 1) / 10)
                    )

            # 大型飛行艇
            elif equip_type == 9 and landbase_status == 2:
                if equip.api_saku >= 9:
                    recon_bonus = max(recon_bonus, 1.3)
                else:
                    recon_bonus = max(recon_bonus, 1.2)

            # 陸上偵察機
            elif equip_type == 49:
                if landbase_status == 1:
                    temp_tyku += math.sqrt(onslot) * (
                        equip.api_tyku + _equip.api_level * level_factor
                    )

                    basic_tyku += math.floor(math.sqrt(onslot) * equip.api_tyku)

                    min_tyku += math.floor(
                        temp_tyku + math.sqrt(AIRCRAFT_EXP_TABLE[temp_alv] / 10)
                    )

                    max_tyku += math.floor(
                        temp_tyku
                        + math.sqrt((AIRCRAFT_EXP_TABLE[temp_alv + 1] - 1) / 10)
                    )

                    if equip.api_saku >= 9:
                        recon_bonus = max(recon_bonus, 1.18)
                    else:
                        recon_bonus = max(recon_bonus, 1.15)

                elif landbase_status == 2:
                    if equip.api_saku >= 9:
                        recon_bonus = max(recon_bonus, 1.23)
                    else:
                        recon_bonus = max(recon_bonus, 1.18)

    return {
        "basic": math.floor(basic_tyku * recon_bonus),
        "min": math.floor(min_tyku * recon_bonus),
        "max": math.floor(max_tyku * recon_bonus),
    }


# 获取TP运输点数
def get_tp(ship_data, equips_data):
    # 战斗S评价点数
    s = 0.0
    # 战斗A评价点数
    a = 0.0
    # 战斗B评价点数
    b = 0.0
    for index, (ship, mst_ship) in enumerate(ship_data):
        # 仅当符合对应舰种时计算TP
        if mst_ship.api_stype in TP_SHIP_TYPE_BONUS:
            # 仅计算非大破时的TP
            if ship.api_nowhp / ship.api_maxhp > 0.25:
                # 计算舰种加成
                s += TP_SHIP_TYPE_BONUS[mst_ship.api_stype][0]
                a += TP_SHIP_TYPE_BONUS[mst_ship.api_stype][1]
                b += TP_SHIP_TYPE_BONUS[mst_ship.api_stype][2]
                # 计算对应装备加成
                for equip_data in equips_data[index]:
                    _equip, equip, onslot = equip_data
                    if onslot is None:
                        continue
                    if equip.api_id in TP_EQUIP_TYPE_BONUS:
                        s += TP_EQUIP_TYPE_BONUS[equip.api_id][0]
                        a += TP_EQUIP_TYPE_BONUS[equip.api_id][1]
                        b += TP_EQUIP_TYPE_BONUS[equip.api_id][2]
    return {"s": s, "a": a, "b": b}
