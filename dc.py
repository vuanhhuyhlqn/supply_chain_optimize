import numpy as np
from entity import Entity

class DC(Entity):
    def __init__(self, coord_x, coord_y, capacity, lease_cost, open_cost):
        super().__init__(coord_x, coord_y)
        self.capacity = capacity
        self.lease_cost = lease_cost
        self.open_cost = open_cost
    def __str__(self):
        return "({0}, {1})\ncapacity: {2}".format(self.coord_x, self.coord_y, self.capacity)