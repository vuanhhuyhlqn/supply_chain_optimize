import numpy as np
from entity import Entity

class DC(Entity):
    def __init__(self, coord_x, coord_y, capacity):
        super().__init__(coord_x, coord_y)
        self.capacity = capacity
    def __str__(self):
        return "({0}, {1})\ncapacity: {2}".format(self.coord_x, self.coord_y, self.capacity)