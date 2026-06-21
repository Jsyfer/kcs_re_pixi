import math
from ..services.MstService import MstService
from ..services.SlotItemService import SlotItemService
from django.db.models.expressions import Combinable
from typing import cast

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

            level_factor = 0.25 if equip.api_tyku > 3 and equip.api_baku > 0 else 0.2 if equip.api_tyku > 3 else 0

            equip_type = equip.api_type[2]

            # 艦上機、水戦、水爆等
            if equip_type in [6, 7, 45, 47, 57] or (equip_type == 26 and equip.api_tyku > 0):
                temp_tyku += math.sqrt(onslot) * (equip.api_tyku + _equip.api_level * level_factor)
                temp_tyku += AIRCRAFT_LEVEL_BONUS[equip_type][temp_alv]

                basic_tyku += math.floor(math.sqrt(onslot) * equip.api_tyku)

                min_tyku += math.floor(temp_tyku + math.sqrt(AIRCRAFT_EXP_TABLE[temp_alv] / 10))

                max_tyku += math.floor(temp_tyku + math.sqrt((AIRCRAFT_EXP_TABLE[temp_alv + 1] - 1) / 10))

            # 水爆、飛行艇
            elif equip_type in [8, 11]:
                temp_tyku += math.sqrt(onslot) * equip.api_tyku
                temp_tyku += AIRCRAFT_LEVEL_BONUS[equip_type][temp_alv]

                basic_tyku += math.floor(math.sqrt(onslot) * equip.api_tyku)

                min_tyku += math.floor(temp_tyku + math.sqrt(AIRCRAFT_EXP_TABLE[temp_alv] / 10))

                max_tyku += math.floor(temp_tyku + math.sqrt((AIRCRAFT_EXP_TABLE[temp_alv + 1] - 1) / 10))

            # 陸戦
            elif equip_type == 48:
                landbase_bonus = 0

                if landbase_status == 1:
                    landbase_bonus = 1.5 * equip.api_houk
                elif landbase_status == 2:
                    landbase_bonus = equip.api_houk + 2 * equip.api_houm

                temp_tyku += math.sqrt(onslot) * (equip.api_tyku + landbase_bonus + _equip.api_level * level_factor)

                temp_tyku += AIRCRAFT_LEVEL_BONUS[equip_type][temp_alv]

                basic_tyku += math.floor(math.sqrt(onslot) * equip.api_tyku)

                min_tyku += math.floor(temp_tyku + math.sqrt(AIRCRAFT_EXP_TABLE[temp_alv] / 10))

                max_tyku += math.floor(temp_tyku + math.sqrt((AIRCRAFT_EXP_TABLE[temp_alv + 1] - 1) / 10))

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

                    min_tyku += math.floor(temp_tyku + math.sqrt(AIRCRAFT_EXP_TABLE[temp_alv] / 10))

                    max_tyku += math.floor(temp_tyku + math.sqrt((AIRCRAFT_EXP_TABLE[temp_alv + 1] - 1) / 10))

            # 大型飛行艇
            elif equip_type == 9 and landbase_status == 2:
                if equip.api_saku >= 9:
                    recon_bonus = max(recon_bonus, 1.3)
                else:
                    recon_bonus = max(recon_bonus, 1.2)

            # 陸上偵察機
            elif equip_type == 49:
                if landbase_status == 1:
                    temp_tyku += math.sqrt(onslot) * (equip.api_tyku + _equip.api_level * level_factor)

                    basic_tyku += math.floor(math.sqrt(onslot) * equip.api_tyku)

                    min_tyku += math.floor(temp_tyku + math.sqrt(AIRCRAFT_EXP_TABLE[temp_alv] / 10))

                    max_tyku += math.floor(temp_tyku + math.sqrt((AIRCRAFT_EXP_TABLE[temp_alv + 1] - 1) / 10))

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


# 根据等级计算舰船基础索敌
def get_ship_base_sakuteki(ship_id, ship_lv):
    mst_ship = MstService.get_mst_ship_by_id(ship_id)
    if mst_ship.min_sakuteki is None or mst_ship.max_sakuteki is None:
        return 0
    return int(mst_ship.min_sakuteki + (ship_lv - 1) * (mst_ship.max_sakuteki - mst_ship.min_sakuteki) / 98)


# 根据等级计算舰船基础回避
def get_ship_base_kaihi(ship_id, ship_lv):
    mst_ship = MstService.get_mst_ship_by_id(ship_id)
    if mst_ship.min_kaihi is None or mst_ship.max_kaihi is None:
        return 0
    return int(mst_ship.min_kaihi + (ship_lv - 1) * (mst_ship.max_kaihi - mst_ship.min_kaihi) / 98)


# 根据等级计算舰船基础对潜
def get_ship_base_taisen(ship_id, ship_lv):
    mst_ship = MstService.get_mst_ship_by_id(ship_id)
    if (
        mst_ship.min_taisen is None
        or mst_ship.max_taisen is None
        or mst_ship.min_taisen == 0
        or mst_ship.max_taisen == 0
    ):
        return 0
    return int(mst_ship.min_taisen + (ship_lv - 1) * (mst_ship.max_taisen - mst_ship.min_taisen) / 98)


# 根据装备改装等级获取加成属性
def get_bonus_setting_by_slotitem_level(bonus_setting, slotitem_level):
    if slotitem_level == 0:
        return bonus_setting["bonus"]
    if "bonus" + str(slotitem_level) in bonus_setting:
        return bonus_setting["bonus" + str(slotitem_level)]
    else:
        return bonus_setting["bonus"]


# 根据舰船装备更新舰船属性
def update_ship_status_with_slot_items(ship):
    mst_ship = MstService.get_mst_ship_by_id(ship.api_ship_id)
    # 获取舰娘基础属性
    # 火力
    new_karyoku = mst_ship.api_houg[0] + ship.api_kyouka[0]  # type: ignore
    # 雷装
    new_raisou = mst_ship.api_raig[0] + ship.api_kyouka[1]  # type: ignore
    # 对空
    new_taiku = mst_ship.api_tyku[0] + ship.api_kyouka[2]  # type: ignore
    # 装甲
    new_soukou = mst_ship.api_souk[0] + ship.api_kyouka[3]  # type: ignore
    # 射程
    new_leng = mst_ship.api_leng
    # 速力
    new_soku = mst_ship.api_soku
    # 索敌
    new_sakuteki = get_ship_base_sakuteki(ship.api_ship_id, ship.api_lv)
    # 回避
    new_kaihi = get_ship_base_kaihi(ship.api_ship_id, ship.api_lv)
    # 对潜
    new_taisen = get_ship_base_taisen(ship.api_ship_id, ship.api_lv)
    # 计算每个装备的加成
    caculated_cross_synergy_bonus_items = []
    ship_item_list = ship.api_slot + [ship.api_slot_ex]
    for item_id in ship_item_list:
        if item_id == -1 or item_id == 0:
            continue
        # 获取装备
        item = SlotItemService.get_slot_item_by_id(item_id)
        mst_item = MstService.get_mst_slotitem_by_id(item.api_slotitem_id)
        # 计算装备基础属性加成
        new_karyoku += mst_item.api_houg
        new_raisou += mst_item.api_raig
        new_taiku += mst_item.api_tyku
        new_soukou += mst_item.api_souk
        # TODO 射程计算
        if mst_item.api_leng != 0:
            new_leng = mst_item.api_leng  # type: ignore
        new_soku += mst_item.api_soku  # type: ignore
        new_sakuteki += mst_item.api_saku  # type: ignore
        new_kaihi += mst_item.api_houk  # type: ignore
        new_taisen += mst_item.api_tais  # type: ignore
        # 计算装备属性加成
        item_bonus = MstService.get_mst_equip_bonus_by_id(item.api_slotitem_id)
        for bonus_setting in item_bonus:
            if ship.api_ship_id in bonus_setting["ship_id"]:
                bonus = get_bonus_setting_by_slotitem_level(bonus_setting, item.api_level)
                new_karyoku += bonus["karyoku"]
                new_raisou += bonus["raisou"]
                new_taiku += bonus["taiku"]
                new_soukou += bonus["soukou"]
                new_leng += bonus["leng"]
                new_soku += bonus["soku"]
                new_sakuteki += bonus["sakuteki"]
                new_kaihi += bonus["kaihi"]
                new_taisen += bonus["taisen"]
                break

        # 计算装备属性相互加成
        # TODO exslot装备对速率的影响
        # 跳过已计算的装备
        if item.api_slotitem_id in caculated_cross_synergy_bonus_items:
            continue
        item_cross_synergy_bonus = MstService.get_mst_equip_cross_synergy_bonus_by_id(item.api_slotitem_id)
        for bonus_setting in item_cross_synergy_bonus:
            # check舰娘的其它装备是否与该装备有相互加成
            for ship_item_id in ship_item_list:
                # 跳过空装备以及当前装备
                if ship_item_id == -1 or ship_item_id == 0 or ship_item_id == item_id:
                    continue
                # 存在与之有相互加成的装备
                ship_mst_slotitem_id = SlotItemService.get_slot_item_by_id(ship_item_id).api_slotitem_id
                if ship_mst_slotitem_id in bonus_setting["item_id"]:
                    # 进一步check当前舰娘是否为符合条件的装备加成舰娘
                    for target_bonus_setting in bonus_setting["target"]:
                        if ship.api_ship_id in target_bonus_setting["ship_id"]:
                            # 添加比较元装备到除外列表
                            caculated_cross_synergy_bonus_items.append(item.api_slotitem_id)
                            # 添加被比较装备到除外列表
                            caculated_cross_synergy_bonus_items.append(ship_mst_slotitem_id)
                            bonus = get_bonus_setting_by_slotitem_level(target_bonus_setting, item.api_level)
                            new_karyoku += bonus["karyoku"]
                            new_raisou += bonus["raisou"]
                            new_taiku += bonus["taiku"]
                            new_soukou += bonus["soukou"]
                            new_leng += bonus["leng"]
                            new_soku += bonus["soku"]
                            new_sakuteki += bonus["sakuteki"]
                            new_kaihi += bonus["kaihi"]
                            new_taisen += bonus["taisen"]
                            break

    # 更新舰娘属性
    ship.api_karyoku = [new_karyoku, ship.api_karyoku[1]]
    ship.api_raisou = [new_raisou, ship.api_raisou[1]]
    ship.api_taiku = [new_taiku, ship.api_taiku[1]]
    ship.api_soukou = [new_soukou, ship.api_soukou[1]]
    ship.api_taisen = [new_taisen, ship.api_taisen[1]]
    ship.api_kaihi = [new_kaihi, ship.api_kaihi[1]]
    ship.api_leng = new_leng
    ship.api_soku = new_soku
    ship.api_sakuteki = [new_sakuteki, ship.api_sakuteki[1]]


# 更新装备被使用状况
def update_slotitem_used_by_ship(item_id_list, ship_id):
    for item_id in item_id_list:
        if item_id == -1 or item_id == 0:
            continue
        item = SlotItemService.get_slot_item_by_id(item_id)
        item.api_used_ship = ship_id
        item.save()


# 修复舰娘状态
def fix_ship_status(ship):
    ship.api_nowhp = ship.api_maxhp
    ship.api_ndock_time = 0
    ship.api_ndock_item = cast(Combinable, [0, 0])
    ship.save()
