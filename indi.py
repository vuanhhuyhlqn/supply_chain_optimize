import numpy as np
from task import Task
from plant import Plant
from dc import DC
from retailer import Retailer
from customer import Customer
from utils import dist

class Individual:
    def __init__(self, task: Task, gene=None):
        self.task = task
        if gene is None:
            #random gene
            self.gene = np.zeros(shape=3*task.num_customers, dtype=int)
            for i in range(task.num_customers):
                self.gene[i * 3] = np.random.randint(0, self.task.num_plants)
                self.gene[i * 3 + 1] = np.random.randint(0, self.task.num_dcs)
                self.gene[i * 3 + 2] = np.random.randint(0, self.task.num_retailers)
        else:
            self.gene = gene
    
    def check_valid(self):
        pass

    def fix(self):
        pass

    def eval(self):
        pass
    
    def __str__(self):
        res = ""
        for cid in range(self.task.num_customers):
            res += "Customer {0}:\n".format(cid)
            res += "Plant {0} -> DC {1} -> Retailer {2}".format(self.gene[cid * 3], self.gene[cid * 3 + 1], self.gene[cid * 3 + 2])
            res += "\n"
        return res