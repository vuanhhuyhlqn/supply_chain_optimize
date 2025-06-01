from task import Task
from typing import List

class TaskGenerator:
    def __init__(self, num_tasks):
        self.num_tasks = num_tasks
    
    def compile(self, 
                num_plants : int, 
                num_dcs : int, 
                num_retailers : int, 
                num_customers : int,
                coord_bounds: List[int],
                plant_output_bounds: List[int],
                dc_cap_bounds: List[int],
                retailer_cap_bounds: List[int],
                dc_lease_cost_bounds: List[int],
                dc_open_cost_bounds: List[int], 
                retailer_lease_cost_bounds: List[int],
                retailer_open_cost_bounds: List[int]):
        self.num_plants = num_plants
        self.num_dcs = num_dcs
        self.num_retailers = num_retailers
        self.num_customers = num_customers
        self.coord_bounds = coord_bounds
        self.plant_output_bounds = plant_output_bounds
        self.dc_cap_bounds = dc_cap_bounds
        self.retailer_cap_bounds = retailer_cap_bounds

    def gen(self):
        lst_tasks : List[Task] = []
        for i in range(self.num_tasks):
            task = Task(num_plants=self.num_plants,
                        num_dcs=self.num_dcs,
                        num_retailers=self.num_retailers,
                        num_customers=self.num_customers)
            
