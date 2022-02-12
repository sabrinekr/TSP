class City():
    """This class represents the cities"""


    def __init__(self, city_id: str, x_coord: str, y_coord: str) -> None:
        self.city_id = int(city_id)
        self.x_coord = float(x_coord)
        self.y_coord = float(y_coord)