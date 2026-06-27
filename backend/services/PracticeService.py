import json


class PracticeService:

    @staticmethod
    def get_practice_list():
        return json.load(open("backend/mock/practice_list.json", encoding="utf-8"))

    @staticmethod
    def get_practice_enemyinfo_by_id(api_member_id):
        return json.load(open(f"backend/mock/practice_{api_member_id}.json", encoding="utf-8"))
