from abc import ABC, abstractmethod


class Ship(ABC):
    """舰船类"""

    ship_id = 0
    mst_ship_id = 0
    ship_idx = 0
    now_hp = 0
    max_hp = 0
    now_fuel = 0
    max_fuel = 0
    now_bull = 0
    max_bull = 0
    karyoku = 0
    raisou = 0
    taiku = 0
    soukou = 0
    kaihi = 0
    taisen = 0
    sakuteki = 0
    lucky = 0
    now_lv = 0
    max_lv = 0
    now_exp = 0
    next_exp = 0

    def __init__(
        self,
        ship_id,
        ship_idx=0,
        now_hp=0,
        max_hp=0,
        now_fuel=0,
        max_fuel=0,
        now_bull=0,
        max_bull=0,
        karyoku=0,
        raisou=0,
        taiku=0,
        soukou=0,
        kaihi=0,
        taisen=0,
        sakuteki=0,
        lucky=0,
        now_lv=0,
        max_lv=0,
        now_exp=0,
        next_exp=0,
    ):
        """Constructor method to initialize instance attributes"""
        self.ship_id = ship_id
        self.ship_idx = ship_idx
        self.now_hp = now_hp
        self.max_hp = max_hp
        self.now_fuel = now_fuel
        self.max_fuel = max_fuel
        self.now_bull = now_bull
        self.max_bull = max_bull
        self.karyoku = karyoku
        self.raisou = raisou
        self.taiku = taiku
        self.soukou = soukou
        self.kaihi = kaihi
        self.taisen = taisen
        self.sakuteki = sakuteki
        self.lucky = lucky
        self.now_lv = now_lv
        self.max_lv = max_lv
        self.now_exp = now_exp
        self.next_exp = next_exp

    def __str__(self):
        return str(self.ship_id)

    @abstractmethod
    def get_ship_id(self): ...
