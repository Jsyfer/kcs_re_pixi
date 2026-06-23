from django.forms.models import model_to_dict
from django.db.models import Q
from ..models.SlotItem import SlotItem
from .ShipService import ShipService
from .MstService import MstService
from .AirBaseService import AirBaseService
from django.conf import settings
import json


class SlotItemService:

    @staticmethod
    def get_slot_items():
        slot_items = SlotItem.objects.using(settings.KCS_DB).all()
        return [{k: v for k, v in model_to_dict(item).items() if v is not None} for item in slot_items]

    @staticmethod
    def get_slot_item_by_id(item_id):
        slot_item = SlotItem.objects.using(settings.KCS_DB).get(api_id=item_id)
        return slot_item

    @staticmethod
    def get_unset_slot_item_by_id(mst_item_id):
        unset_slot_item = (
            SlotItem.objects.using(settings.KCS_DB)
            .filter(
                (Q(api_used_ship__isnull=True) | Q(api_used_ship=-1)),
                (Q(api_used_air_base__isnull=True) | Q(api_used_air_base=-1)),
                api_slotitem_id=mst_item_id,
            )
            .order_by("-api_level", "-api_alv")
            .first()
        )
        return unset_slot_item

    @staticmethod
    def create_slot_item_by_id(mst_item_id):
        slot_item = SlotItem.objects.using(settings.KCS_DB).create(
            api_slotitem_id=mst_item_id, api_locked=0, api_level=0
        )
        return slot_item.api_id

    @staticmethod
    def get_unset_slots():
        unset_slot_items = {}
        slot_items = SlotItem.objects.using(settings.KCS_DB).all()
        ship_list = ShipService.get_ship()
        air_base_list = AirBaseService.get_air_base()
        # 获取所有舰娘装载的装备
        items_on_ship = [
            slot
            for ship in ship_list
            for slot in (ship.get("api_slot", []) + [ship.get("api_slot_ex", -1)])
            if slot != -1
        ]
        # 获取所有陆航舰装载的装备
        # TODO 获取活动海域陆航装备
        items_air_base = [
            api_plane.get("api_slotid")
            for air_base in air_base_list
            for api_plane in (air_base.get("api_plane_info", []))
            if api_plane.get("api_slotid") != -1
        ]
        for item in slot_items:
            # 仅当该装备未被任何舰娘装载时，才将其加入结果
            if item.api_id not in (items_on_ship + items_air_base):
                # 结果设置
                mst_slot_item = MstService.get_mst_slotitem_by_id(item.api_slotitem_id)
                if mst_slot_item.api_id in [128, 281]:
                    # 試製51cm連装砲, 51cm連装砲
                    slot_key = "api_slottype38"
                elif mst_slot_item.api_id == 142:
                    # 15m二重測距儀+21号電探改二
                    slot_key = "api_slottype93"
                elif mst_slot_item.api_id == 151:
                    # 試製景雲(艦偵型)
                    slot_key = "api_slottype94"
                else:
                    slot_key = "api_slottype" + str((mst_slot_item.api_type or [])[2])

                unset_slot_items.setdefault(slot_key, []).append(item.api_id)

        return unset_slot_items

    @staticmethod
    def del_slot_item_by_id(item_id):
        SlotItem.objects.using(settings.KCS_DB).get(api_id=item_id).delete()
