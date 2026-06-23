import time
from datetime import datetime
from zoneinfo import ZoneInfo


class Utils:

    # 将毫秒级timestamp转换为东京时间 2026-06-21 21:58:54
    @staticmethod
    def convert_readable_time(ms_timestamp):
        dt = datetime.fromtimestamp(ms_timestamp / 1000, tz=ZoneInfo("Asia/Tokyo")).replace(tzinfo=None)
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    # 检查是否到达给定的毫秒级timestamp，距离1分钟以内即视为到达
    @staticmethod
    def check_if_time_passed(ms_timestamp):
        current_ms = time.time() * 1000
        return ms_timestamp <= current_ms + 60000

    # 获取当前timestamp
    @staticmethod
    def get_current_timestamp():
        return int(time.time() * 1000)
