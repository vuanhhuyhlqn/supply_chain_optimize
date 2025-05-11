import numpy as np
import os
import math
import sys
from typing import List
from plant import Plant
from dc import DC
from retailer import Retailer
from customer import Customer


class Task:
	def __init__(self, num_plants, num_dcs, num_retailers, num_customers):
		self.num_plants = num_plants
		self.num_dcs = num_dcs
		self.num_retailers = num_retailers
		self.num_customers = num_customers

		self.lst_plants : List[Plant] = []
		self.lst_dcs : List[DC] = []
		self.lst_retailers : List[Retailer] = []
		self.lst_customers : List[Customer] = []

        