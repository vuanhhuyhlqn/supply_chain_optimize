import numpy as np
import os
import math
import sys

class Task:
	def __init__(self, num_plants, num_dcs, num_retailers, num_customers):
		self.num_plants = num_plants
		self.num_dcs = num_dcs
		self.num_retailers = num_retailers
		self.num_customers = num_customers

		self.lst_plants = []
		self.lst_dcs = []
		self.lst_retailers = []
		self.lst_customers = []

        