import numpy as np
from entity import Entity

class DC(Entity):
    def __init__(self, coord_x, coord_y, capacity):
        super().__init__(coord_x, coord_y)
        self.capacity = capacity