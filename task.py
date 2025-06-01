import numpy as np
from typing import List
from plant import Plant
from dc import DC
from retailer import Retailer
from customer import Customer


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
		
		self.a = np.zeros(4)
		self.b = np.zeros(4)
		
	def add_plant(self, plant: Plant):
		self.lst_plants.append(plant)
	
	def add_dc(self, dc: DC):
		self.lst_dcs.append(dc)
	
	def add_retailer(self, retailer: Retailer):
		self.lst_retailers.append(retailer)
	
	def add_customer(self, customer: Customer):
		self.lst_customers.append(customer)