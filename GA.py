import numpy as np
from typing import List
from task import Task
from plant import Plant
from dc import DC
from retailer import Retailer
from customer import Customer
from indi import Individual
from crossover import *
from mutation import *

class model:
    def __init__(self, pop_size, task : Task):
        self.pop_size = pop_size
        self.task = Task
        self.pop : List[Individual] = []
        while len(self.pop) < self.pop_size:
            self.pop.append(Individual(task))
        