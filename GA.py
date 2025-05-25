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

class Model:
    def __init__(self, pop_size, 
                 task : Task, 
                 crossover: AbstractCrossover, 
                 mutation: AbstractMutation):
        self.pop_size = pop_size
        self.task = Task
        self.crossover = crossover
        self.mutation = mutation
        self.pop : List[Individual] = []
        while len(self.pop) < self.pop_size:
            indi = Individual(task)
            
            if indi.check_valid() == False:
                # If an invalid individual is generated, we go fix it
                indi.fix()
            
            indi.fitness = indi.eval()
            self.pop.append(indi)

    def fit(self, num_gen, num_crossover, num_mutation, monitor=True, monitor_rate=5):
        for gen in range(num_gen):
            #crossover
            off_cr : List[Individual] = []
            while len(off_cr) < num_crossover:
                pa = self.get_random_indi()
                pb = self.get_random_indi()
                oc = self.crossover(pa, pb) #crossover offspring
                if oc.check_valid() == False:
                    oc.fix()
                oc.fitness = oc.eval()
                off_cr.append(oc)
            
            #mutation
            off_mut : List[Individual] = []
            while len(off_mut) < num_mutation:
                p = self.get_random_indi()
                om = self.mutation(p)
                if om.check_valid() == False:
                    om.fix()
                om.fitness = om.eval()
                off_mut.append(om)
            
            self.pop += off_cr
            self.pop += off_mut
            self.pop = sorted(self.pop)[:self.pop_size]

            best_fitness = self.pop[0].fitness

            if gen % monitor_rate == 0:
                print(f"Gen {gen}: best fitness {best_fitness}")

        print("Best found solution:")
        print(self.pop[0])
    
    def get_random_indi(self) -> Individual:
        id = np.random.randint(0, self.pop_size)
        return self.pop[id]