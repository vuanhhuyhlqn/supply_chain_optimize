import numpy as np
from entity import Entity

class DC(Entity):
	def __init__(self, entity_id, coord_x, coord_y, capacity, lease_cost, open_cost):
		super().__init__(entity_id, coord_x, coord_y)
		self.capacity = capacity
		self.lease_cost = lease_cost
		self.open_cost = open_cost
	def __str__(self):
		return "({0}, {1})\ncapacity: {2}\nlease cost: {3}\nopen cost: {4}".format(self.coord_x, self.coord_y, self.capacity, self.lease_cost, self.open_cost)