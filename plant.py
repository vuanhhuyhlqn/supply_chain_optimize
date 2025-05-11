import numpy as np
from entity import Entity

class Plant(Entity):
    def __init__(self, coord_x, coord_y, ouput):
        super().__init__(coord_x, coord_y)
        self.output = ouput