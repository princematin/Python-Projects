class WorkPlaceIsFull(Exception):
    def __str__(self):
        return "work place is full!"


class Consts:
    BASE_PRICE = {'mine': 150, 'school': 100, 'company': 90}
    BASE_PLACE_COST = 2500
    LEVEL_MUL = 50


class WorkPlace:
    def __init__(self, name: str) -> None:
        ...

    def get_price(self) -> int:
        ...

    def calc_costs(self):
        pass

    def calc_capacity(self):
        pass

    def upgrade(self) -> None:
        ...

    def hire(self, person) -> None:
        ...

    def get_expertise(self) -> str:
        ...

    def calc(self) -> int:
        ...

    @staticmethod
    def calc_all() -> int:
        ...

