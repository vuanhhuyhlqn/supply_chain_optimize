import numpy as np
from typing import List, Tuple
from math import sqrt
from entity import Entity
from task import Task
from plant import Plant
from dc import DC
from retailer import Retailer
from customer import Customer

def dist(entity_a: Entity, entity_b: Entity):
    return sqrt((entity_a.coord_x - entity_b.coord_x) ** 2 + (entity_a.coord_y - entity_b.coord_y) ** 2) 

def get_route_entities(task:Task, plant_id:int, dc_id:int, retailer_id:int, customer_id:int) -> Tuple[Plant, DC, Retailer, Customer]:
    plant = task.lst_plants[plant_id]
    dc = task.lst_dcs[dc_id]
    retailer = task.lst_retailers[retailer_id]
    customer = task.lst_customers[customer_id]
    return plant, dc, retailer, customer
