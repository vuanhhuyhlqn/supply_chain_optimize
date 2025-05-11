import numpy as np
from entity import Entity

class Plant(Entity):
    def __init__(self, coord_x, coord_y, ouput):
        super().__init__(coord_x, coord_y)
        self.output = ouput

    def __str__(self):
        return "({0}, {1})\noutput: {2}".format(self.coord_x, self.coord_y, self.output)