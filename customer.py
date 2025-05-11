import numpy as np
from entity import Entity

class Customer(Entity):
    def __init__(self, coord_x, coord_y, demand):
        super().__init__(coord_x, coord_y)
        self.demand = demand