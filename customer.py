import numpy as np
from entity import Entity

class Customer(Entity):
    def __init__(self, coord_x, coord_y, demand):
        super().__init__(coord_x, coord_y)
        self.demand = demand
    def __str__(self):
        return "({0}, {1})\ndemand: {2}".format(self.coord_x, self.coord_y, self.demand)