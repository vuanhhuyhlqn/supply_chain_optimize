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
            for i in range(self.num_plants):
                entity_cnt += 1

                # Plant output bounds
                plant_output_lb = self.plant_output_bounds[0]
                plant_output_ub = self.plant_output_bounds[1]

                coord_x = np.random.uniform(coord_lb, coord_ub)
                coord_y = np.random.uniform(coord_lb, coord_ub)
                output = np.random.randint(plant_output_lb, plant_output_ub)
                plant = Plant(entity_id=entity_cnt, coord_x=coord_x, coord_y=coord_y, output=output)
                
                task.add_plant(plant)

            for i in range(self.num_dcs):
                entity_cnt += 1

                # DC capacity bounds
                dc_cap_lb = self.dc_cap_bounds[0]
                dc_cap_ub = self.dc_cap_bounds[1]

                # DC lease cost bounds
                dc_lease_cost_lb = self.dc_lease_cost_bounds[0]
                dc_lease_cost_ub = self.dc_lease_cost_bounds[1]

                # DC lease cost bounds
                dc_open_cost_lb = self.dc_open_cost_bounds[0]
                dc_open_cost_ub = self.dc_open_cost_bounds[1]
                
                coord_x = np.random.uniform(coord_lb, coord_ub)
                coord_y = np.random.uniform(coord_lb, coord_ub)
                dc_cap = np.random.randint(dc_cap_lb, dc_cap_ub)
                dc_lease_cost = np.random.uniform(dc_lease_cost_lb, dc_lease_cost_ub)
                dc_open_cost = np.random.uniform(dc_open_cost_lb, dc_open_cost_ub)

                dc = DC(entity_id=entity_cnt, 
                        coord_x=coord_x, 
                        coord_y=coord_y, 
                        capacity=dc_cap, 
                        lease_cost=dc_lease_cost, 
                        open_cost=dc_open_cost)
                
                task.add_dc(dc)

            for i in range(self.num_retailers):
                entity_cnt += 1

                # Retailer capacity bounds
                retailer_cap_lb = self.retailer_cap_bounds[0]
                retailer_cap_ub = self.retailer_cap_bounds[1]

                # Retailer lease cost bounds
                retailer_lease_cost_lb = self.retailer_lease_cost_bounds[0]
                retailer_lease_cost_ub = self.retailer_lease_cost_bounds[1]

                # Retailer lease cost bounds
                retailer_open_cost_lb = self.retailer_open_cost_bounds[0]
                retailer_open_cost_ub = self.retailer_open_cost_bounds[1]
                
                coord_x = np.random.uniform(coord_lb, coord_ub)
                coord_y = np.random.uniform(coord_lb, coord_ub)
                retailer_cap = np.random.randint(retailer_cap_lb, retailer_cap_ub)
                retailer_lease_cost = np.random.uniform(retailer_lease_cost_lb, retailer_lease_cost_ub)
                retailer_open_cost = np.random.uniform(retailer_open_cost_lb, retailer_open_cost_ub)

                retailer = Retailer(entity_id=entity_cnt, 
                        coord_x=coord_x, 
                        coord_y=coord_y, 
                        capacity=retailer_cap, 
                        lease_cost=retailer_lease_cost, 
                        open_cost=retailer_open_cost)
                
                task.add_retailer(retailer)
           
            for i in range(self.num_customers):
                entity_cnt += 1

                coord_x = np.random.uniform(coord_lb, coord_ub)
                coord_y = np.random.uniform(coord_lb, coord_ub)

                customer_demand_lb = self.customer_demand_bounds[0]
                customer_demand_ub = self.customer_demand_bounds[1]

                customer_demand = np.random.randint(customer_demand_lb, customer_demand_ub)

                customer = Customer(entity_id=entity_cnt,
                                    coord_x=coord_x,
                                    coord_y=coord_y,
                                    demand=customer_demand)

                task.add_customer(customer)
            
            lst_tasks.append(task)
        return lst_tasks