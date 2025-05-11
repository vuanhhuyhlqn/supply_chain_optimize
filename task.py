import numpy as np
import os
import math
import sys
from indi import Individual

class Task:
	def __init__(self, num_plants, num_dcs, num_retailers, num_customers, coord_bound=1000):
		self.num_plants = num_plants
		self.num_dcs = num_dcs
		self.num_retailers = num_retailers
		self.num_customers = num_customers

		#site coordinates
		self.plant_coords = np.random.uniform(-coord_bound, coord_bound, size=(self.num_plants, 2))
		self.dc_coords = np.random.uniform(-coord_bound, coord_bound, size=(self.num_dcs, 2))
		self.retailer_coords = np.random.uniform(-coord_bound, coord_bound, size=(self.num_retailers, 2))
		self.customer_coords = np.random.uniform(-coord_bound, coord_bound, size=(self.num_customers, 2))

		#shipping cost
		self.x1 = np.zeros((self.num_plants, self.num_dcs))
		self.x2 = np.zeros((self.num_dcs, self.num_retailers))
		self.x3 = np.zeros((self.num_retailers, self.num_customers))
		self.x4 = np.zeros((self.num_plants, self.num_customers))
		self.x5 = np.zeros((self.num_dcs, self.num_customers))
		self.x6 = np.zeros((self.num_plants, self.num_retailers))

		self.gen_cost()
		self.gen_output()
		self.gen_capacity()
		self.gen_demand()
    
	def gen_output(self, output_bound=1000):
		self.plant_outputs = np.random.randint(0, output_bound, size=self.num_plants)

	def gen_capacity(self, capacity_bound=1000):
		self.dc_capacities = np.random.randint(0, capacity_bound, size=self.num_dcs)
		self.retailer_capacities = np.random.randint(0, capacity_bound, size=self.num_retailers)

	def gen_demand(self, demand_bound=200):
		self.customer_demands = np.random.randint(0, demand_bound, size=self.num_customers)
		pass

	def gen_cost(self, b_bound=10.0):
		self.x1 = self.dist(self.plant_coords, self.dc_coords)
		self.x2 = self.dist(self.dc_coords, self.retailer_coords)
		self.x3 = self.dist(self.retailer_coords, self.customer_coords)
		self.x4 = self.dist(self.plant_coords, self.customer_coords)
		self.x5 = self.dist(self.dc_coords, self.customer_coords)
		self.x6 = self.dist(self.plant_coords, self.retailer_coords)

		#normal delivery
		a = np.random.uniform(1.0, 1.2, size=len(self.x1))
		a_ = np.lib.stride_tricks.as_strided(a, self.x1.shape, (a.strides[0], 0))
		b = np.random.uniform(-b_bound, b_bound, size=self.x1.shape)
		self.x1 = self.x1 * a_ + b

		a = np.random.uniform(1.0, 1.2, size=len(self.x2))
		a_ = np.lib.stride_tricks.as_strided(a, self.x2.shape, (a.strides[0], 0))
		b = np.random.uniform(-b_bound, b_bound, size=self.x2.shape)
		self.x2 = self.x2 * a_ + b

		a = np.random.uniform(1.0, 1.2, size=len(self.x3))
		a_ = np.lib.stride_tricks.as_strided(a, self.x3.shape, (a.strides[0], 0))
		b = np.random.uniform(-b_bound, b_bound, size=self.x3.shape)
		self.x3 = self.x3 * a_ + b

		#direct shipment
		a = np.random.uniform(1.2, 1.4, size=len(self.x4))
		a_ = np.lib.stride_tricks.as_strided(a, self.x4.shape, (a.strides[0], 0))
		b = np.random.uniform(-b_bound, b_bound, size=self.x4.shape)
		self.x4 = self.x4 * a_ + b

		a = np.random.uniform(1.2, 1.4, size=len(self.x6))
		a_ = np.lib.stride_tricks.as_strided(a, self.x6.shape, (a.strides[0], 0))
		b = np.random.uniform(-b_bound, b_bound, size=self.x6.shape)
		self.x6 = self.x6 * a_ + b

		#direct delivery
		a = np.random.uniform(1.4, 1.6, size=len(self.x5))
		a_ = np.lib.stride_tricks.as_strided(a, self.x5.shape, (a.strides[0], 0))
		b = np.random.uniform(-b_bound, b_bound, size=self.x5.shape)
		self.x5 = self.x5 * a_ + b

	def dist(self, site_a_coords, site_b_coords):
		site_a_coords_x = site_a_coords[:, 0]
		site_a_coords_y = site_a_coords[:, 1]

		site_b_coords_x = site_b_coords[:, 0]
		site_b_coords_y = site_b_coords[:, 1]

		dist_mat_shape = (site_a_coords.shape[0], site_b_coords.shape[0])

		site_a_coords_x_ = np.lib.stride_tricks.as_strided(site_a_coords_x, dist_mat_shape, (16, 0))
		site_b_coords_x_ = np.lib.stride_tricks.as_strided(site_b_coords_x, dist_mat_shape, (0, 16))
		x_diffs = (site_a_coords_x_ - site_b_coords_x) ** 2

		site_a_coords_y_ = np.lib.stride_tricks.as_strided(site_a_coords_y, dist_mat_shape, (16, 0))
		site_b_coords_y_ = np.lib.stride_tricks.as_strided(site_b_coords_y, dist_mat_shape, (0, 16))
		y_diffs = (site_a_coords_y_ - site_b_coords_y) ** 2

		dist_mat = np.sqrt(x_diffs + y_diffs)
		return dist_mat

	def single_unit_cost(self, indi):
		assert(len(indi) == self.num_customers * 3)
		print(indi.strides)
		new_shape = (self.num_customers, 3)
		new_strides = (indi.strides[0] * 3, indi.strides[0])
		indi_ = np.lib.stride_tricks.as_strided(indi, new_shape, new_strides)
		print(indi_)

	def unit_cost(self, p):
		new_shape = (len(p), self.num_customers, 3)
		strides = p.strides
		new_strides = (strides[0], strides[1] * 3, strides[1])
		p_ = np.lib.stride_tricks.as_strided(p, new_shape, new_strides)
		print(p_)
                
        