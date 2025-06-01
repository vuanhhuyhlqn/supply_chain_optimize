import numpy as np
from typing import List
from plant import Plant
from dc import DC
from retailer import Retailer
from customer import Customer
import pickle

class Task:
	def __init__(self, num_entities, num_plants, num_dcs, num_retailers, num_customers):
		self.num_entities = num_entities
		self.num_plants = num_plants
		self.num_dcs = num_dcs
		self.num_retailers = num_retailers
		self.num_customers = num_customers

		self.lst_plants : List[Plant] = []
		self.lst_dcs : List[DC] = []
		self.lst_retailers : List[Retailer] = []
		self.lst_customers : List[Customer] = []
		
		self.a = np.random.uniform(0.8, 1.5, size=4)
		b_max = np.random.uniform(0, 1000)
		self.b = np.random.uniform(0, b_max, size=4)
	
	def check_condition(self) -> bool:
		total_demand = 0
		for customer in self.lst_customers:
			total_demand += customer.demand
		
		total_plant_output = 0
		for plant in self.lst_plants:
			total_plant_output += plant.output
		
		# total_dc_cap = 0
		# for dc in self.lst_dcs:
		# 	total_dc_cap += dc.capacity

		# total_retailer_cap = 0
		# for retailer in self.lst_retailers:
		# 	total_retailer_cap += retailer.capacity

		if total_demand > total_plant_output:
			return False
		# if total_demand > total_dc_cap:
		# 	return False
		# if total_demand > total_retailer_cap:
		# 	return False
		return True

	def add_plant(self, plant: Plant):
		self.lst_plants.append(plant)
	
	def add_dc(self, dc: DC):
		self.lst_dcs.append(dc)
	
	def add_retailer(self, retailer: Retailer):
		self.lst_retailers.append(retailer)
	
	def add_customer(self, customer: Customer):
		self.lst_customers.append(customer)
		
def pickle_task(task: Task, file_path):
	with open(file_path, 'wb') as f:  # open a text file
		pickle.dump(task, f) # serialize the list

