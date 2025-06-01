from task import Task
import numpy as np
from typing import List
from plant import Plant
from dc import DC
from retailer import Retailer
from customer import Customer

class TaskGenerator:
    def __init__(self, num_tasks):
        self.num_tasks = num_tasks
    
    def compile(self, 
                num_plants: int, 
                num_dcs: int, 
                num_retailers: int, 
                num_customers: int,
                coord_bounds: List[int],
                plant_output_bounds: List[int],
                dc_cap_bounds: List[int],
                retailer_cap_bounds: List[int],
                dc_lease_cost_bounds: List[int],
                dc_open_cost_bounds: List[int], 
                retailer_lease_cost_bounds: List[int],
                retailer_open_cost_bounds: List[int],
                customer_demand_bounds: List[int]):
        
        self.num_plants = num_plants
        self.num_dcs = num_dcs
        self.num_retailers = num_retailers
        self.num_customers = num_customers
        self.num_entities = self.num_plants + self.num_dcs + self.num_retailers + self.num_customers

        self.coord_bounds = coord_bounds
        
        self.plant_output_bounds = plant_output_bounds
        self.dc_cap_bounds = dc_cap_bounds
        self.retailer_cap_bounds = retailer_cap_bounds
        
        self.dc_lease_cost_bounds = dc_lease_cost_bounds
        self.dc_open_cost_bounds = dc_open_cost_bounds
        
        self.retailer_lease_cost_bounds = retailer_lease_cost_bounds
        self.retailer_open_cost_bounds = retailer_open_cost_bounds
        
        self.customer_demand_bounds = customer_demand_bounds

    def gen(self):
        lst_tasks : List[Task] = []

        coord_lb = self.coord_bounds[0]
        coord_ub = self.coord_bounds[1]

        for i in range(self.num_tasks):
            task = Task(num_entities=self.num_entities,
                        num_plants=self.num_plants,
                        num_dcs=self.num_dcs,
                        num_retailers=self.num_retailers,
                        num_customers=self.num_customers)
            entity_cnt = 0
            for plant_id in range(self.num_plants):
                entity_cnt += 1

                # Plant output bounds
                plant_output_lb = self.plant_output_bounds[0]
                plant_output_ub = self.plant_output_bounds[1]

                coord_x = np.random.uniform(coord_lb, coord_ub)
                coord_y = np.random.uniform(coord_lb, coord_ub)
                output = np.random.uniform(plant_output_lb, plant_output_ub)
                plant = Plant(entity_id=entity_cnt, coord_x=coord_x, coord_y=coord_y, output=output)
                
                task.add_plant(plant)

            
            
