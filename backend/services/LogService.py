import json


class LogService:

    @staticmethod
    def get_log():
        return json.load(open("backend/temp/api_log.json", encoding="utf-8"))
