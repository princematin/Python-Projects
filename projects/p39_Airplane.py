from p39_FlyingVehicle import FlyingVehicle
from p39_GroundVehicle import GroundVehicle

class Airplane(GroundVehicle, FlyingVehicle):
    def __init__(self, airline: str, number_of_crew: int, captain: str, **kwargs):
        super().__init__(**kwargs)
        self.airline = airline
        self.number_of_crew = number_of_crew
        self.captain = captain


class B707(Airplane):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
