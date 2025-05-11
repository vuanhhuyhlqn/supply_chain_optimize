import numpy as np
from entity import Entity
from math import sqrt

def dist(entity_a: Entity, entity_b: Entity):
    return sqrt((entity_a.coord_x - entity_b.coord_x) ** 2 + (entity_a.coord_y - entity_b.coord_y) ** 2) 

