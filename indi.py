import numpy as np
from typing import List
from task import Task
from plant import Plant
from dc import DC
from retailer import Retailer
from customer import Customer
from utils import dist, get_route_entities

class Individual:
	def __init__(self, task: Task, gene=None, deli_types:List[int]=None):
		self.task = task
		if gene is None:
			#random gene
			self.gene = np.zeros(shape=3*task.num_customers, dtype=int)
			for cid in range(self.task.num_customers):
				self.gene[cid * 3] = np.random.randint(0, self.task.num_plants)
				self.gene[cid * 3 + 1] = np.random.randint(0, self.task.num_dcs)
				self.gene[cid * 3 + 2] = np.random.randint(0, self.task.num_retailers)
		else:
			self.gene = gene

		# Delivery type:
		# 0: nomarl delivery (Plant -> DC -> Retailer -> Customer)
		# 1: direct shipment (Plant -> Customer)
		# 2: direct delivery type 1 (Plant -> DC -> Customer)
		# 3: direct delivery type 2 (Plant -> Retailer -> Customer)
		if deli_types is None:
			self.deli_types = np.random.randint(0, 3, size=self.task.num_customers)
		else:
			self.deli_types = deli_types

		self.fitness = None

	def check_valid(self) -> bool:
		for plant_id in range(self.task.num_plants):
			if self.get_plant_demand(plant_id) > self.task.lst_plants[plant_id].output:
				print("Plant {0} output capacity violated!".format(plant_id))
				return False
		for dc_id in range(self.task.num_dcs):
			if self.get_dc_stock(dc_id) > self.task.lst_dcs[dc_id].capacity:
				print("DC {0} capacity violated!".format(dc_id))
				return False
		for retailer_id in range(self.task.num_retailers):
			if self.get_retailer_stock(retailer_id) > self.task.lst_retailers[retailer_id].capacity:
				print("Retailer {0} capacity violated!".format(retailer_id))
				return False
		return True

	def fix(self):
		pass

	def eval(self) -> float:
		cost = 0
		for dc_id in range(self.task.num_dcs):
			stock = self.get_dc_stock(dc_id)
			if stock > 0:
				cost += self.task.lst_dcs[dc_id].open_cost
				cost += self.task.lst_dcs[dc_id].lease_cost * stock

		for retailer_id in range(self.task.num_retailers):
			stock = self.get_retailer_stock(retailer_id)
			if stock > 0:
				cost += self.task.lst_retailers[retailer_id].open_cost
				cost += self.task.lst_retailers[retailer_id].lease_cost * stock

		for customer_id in range(self.task.num_customers):
			plant_id = self.gene[customer_id * 3]
			dc_id = self.gene[customer_id * 3 + 1]
			retailer_id = self.gene[customer_id * 3 + 2]

			if self.deli_types[customer_id] == 0:
				cost += self.normal_deli_cost(plant_id, dc_id, retailer_id, customer_id)
			if self.deli_types[customer_id] == 1:
				cost += self.direct_ship_cost(plant_id, dc_id, retailer_id, customer_id)
			if self.deli_types[customer_id] == 2:
				cost += self.direct_deli_t1_cost(plant_id, dc_id, retailer_id, customer_id)
			if self.deli_types[customer_id] == 3:
				cost += self.direct_deli_t2_cost(plant_id, dc_id, retailer_id, customer_id)
		return cost

	def normal_deli_cost(self, plant_id:int, dc_id:int, retailer_id:int, customer_id:int) -> float:
		plant, dc, retailer, customer = get_route_entities(self.task, plant_id, dc_id, retailer_id, customer_id)
		load = customer.demand
		return load * (dist(plant, dc) + dist(dc, retailer) + dist(retailer, customer))

	def direct_deli_t1_cost(self, plant_id:int, dc_id:int, retailer_id:int, customer_id:int) -> float:
		plant, dc, retailer, customer = get_route_entities(self.task, plant_id, dc_id, retailer_id, customer_id)
		load = customer.demand
		return load * (dist(plant, dc) + dist(dc, customer))

	def direct_deli_t2_cost(self, plant_id:int, dc_id:int, retailer_id:int, customer_id:int) -> float:
		plant, dc, retailer, customer = get_route_entities(self.task, plant_id, dc_id, retailer_id, customer_id)
		load = customer.demand
		return load * (dist(plant, retailer) + dist(retailer, customer))

	def direct_ship_cost(self, plant_id:int, dc_id:int, retailer_id:int, customer_id:int) -> float:
		plant, dc, retailer, customer = get_route_entities(self.task, plant_id, dc_id, retailer_id, customer_id)
		load = customer.demand
		return load * dist(plant, customer)

	def __str__(self):
		res = ""
		for cid in range(self.task.num_customers):
			res += "Customer {0}:\n".format(cid)
			res += "Plant {0} -> DC {1} -> Retailer {2}".format(self.gene[cid * 3], self.gene[cid * 3 + 1], self.gene[cid * 3 + 2])
			res += "\n"
		return res
    
	def get_plant_demand(self, plant_id) -> int:
		res = 0
		for cid in range(self.task.num_customers):
			if self.gene[cid * 3] == plant_id:
				res += self.task.lst_customers[cid].demand
		return res
    
	def get_dc_stock(self, dc_id) -> int:
		res = 0
		for cid in range(self.task.num_customers):
			if self.gene[cid * 3 + 1] == dc_id:
				res += self.task.lst_customers[cid].demand
		return res
    
	def get_retailer_stock(self, retailer_id) -> int:
		res = 0
		for cid in range(self.task.num_customers):
			if self.gene[cid * 3 + 2] == retailer_id:
				res += self.task.lst_customers[cid].demand
		return res

	def __lt__(self, other):
		return self.fitness < other.fitness