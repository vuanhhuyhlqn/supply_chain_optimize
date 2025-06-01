import numpy as np
from entity import Entity

class Plant(Entity):
    def __init__(self, entity_id, coord_x, coord_y, output):
        super().__init__(entity_id, coord_x, coord_y)
        self.output = output

    def __str__(self):
        return "({0}, {1})\noutput: {2}".format(self.coord_x, self.coord_y, self.output)