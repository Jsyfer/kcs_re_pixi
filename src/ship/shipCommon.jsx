export const getShipType = (typeNumber) => {
    switch (typeNumber) {
        case 1:
            return "海防艦";
        case 2:
            return "駆逐艦";
        case 3:
            return "軽巡洋艦";
        case 4:
            return "重雷装巡洋艦";
        case 5:
            return "重巡洋艦";
        case 6:
            return "航空巡洋艦";
        case 7:
            return "軽空母";
        case 8:
            return "戦艦";
        case 9:
            return "戦艦";
        case 10:
            return "航空戦艦";
        case 11:
            return "正規空母";
        case 13:
            return "潜水艦";
        case 14:
            return "潜水空母";
        case 16:
            return "水上機母艦";
        case 17:
            return "揚陸艦";
        case 18:
            return "装甲空母";
        case 19:
            return "工作艦";
        case 20:
            return "潜水空母";
        case 21:
            return "練習巡洋艦";
        case 22:
            return "補給艦";
        default:
            return "Unknown";
    }
}

// get Sprite number of ship speed based on soku number
export const getShipSpeed = (sokuNumber) => {
    switch (sokuNumber) {
        case 20:
            // 最速
            return 62
        case 15:
            // 高速+
            return 57
        case 10:
            // 高速
            return 56
        default:
            // 低速
            return 59
    }
}

// get Sprite number of ship speed based on soku number
export const getShipHpColor = (nowHp, maxHp) => {
    const hpRatio = nowHp / maxHp;
    if (hpRatio > 0.75) {
        return 0x00ff00;
    } else if (hpRatio > 0.6) {
        return 0xe0fe52;
    } else if (hpRatio > 0.5) {
        return 0xf9d949;
    } else if (hpRatio > 0.25) {
        return 0xef8f35;
    } else {
        return 0xec622b;
    }
}
