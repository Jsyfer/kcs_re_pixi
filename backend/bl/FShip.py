from backend.bl.Ship import Ship


class FShip(Ship):
    """我方舰船"""

    def get_ship_id(self):
        return 1
