from person import Consts, Person
import math

class Worker(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.job = "worker"

    def get_price(self) -> int:
        price = math.floor(Consts.BASE_PRICE[self.job] * (Consts.MIN_AGE / self.age))
        return price
    
    def calc_life_cost(self) -> int:
        costs = math.floor(Consts.BASE_COST[self.job] * (self.age / Consts.MIN_AGE))
        return costs

    def calc_income(self) -> int:
        income = math.floor(Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] * Consts.MIN_AGE / self.age)
        return income