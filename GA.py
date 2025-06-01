import numpy as np
from typing import List
from math import isclose
from task import Task
from plant import Plant
from dc import DC
from retailer import Retailer
from customer import Customer
from indi import Individual
from crossover import *
from mutation import *
from local_search import *

class Model:
    def __init__(self, pop_size, 
                 task : Task, 
                 crossover: AbstractCrossover, 
                 mutation: AbstractMutation,
                 localsearch: AbstractLocalSearch):
        self.pop_size = pop_size
        self.task = Task
        self.crossover = crossover
        self.mutation = mutation
        self.localsearch = localsearch
        self.pop : List[Individual] = []

        #History
        self.bfs : List[float] = []

        while len(self.pop) < self.pop_size:
            indi = Individual(task)
            
            while indi.check_valid() == False:
                # If an invalid individual is generated, we go fix it
                indi.fix()
            
            indi.fitness = indi.eval()
            self.pop.append(indi)

    def fit(self, num_gen, num_crossover, num_mutation, numls, monitor=True, monitor_rate=5):
        for gen in range(num_gen + 1):
            #crossover
            off_cr : List[Individual] = []
            while len(off_cr) < num_crossover:
                pa = self.get_random_indi()
                pb = self.get_random_indi()
                oc = self.crossover(pa, pb) #crossover offspring
                while oc.check_valid() == False:
                    oc.fix()
                oc.fitness = oc.eval()
                off_cr.append(oc)
            
            #mutation
            off_mut : List[Individual] = []
            while len(off_mut) < num_mutation:
                p = self.get_random_indi()
                om = self.mutation(p)
                while om.check_valid() == False:
                    om.fix()
                om.fitness = om.eval()
                off_mut.append(om)
            
            self.pop += off_cr
            self.pop += off_mut
            self.pop = sorted(self.pop)

            off_ls : List[Individual] = []
            while len(off_ls) < numls:
                p = self.get_random_indi(range=numls * 2)
                ols = self.localsearch(p)
                while ols.check_valid == False:
                    ols.fix()
                ols.fitness = ols.eval()
                off_ls.append(ols)
            
            self.pop += off_ls

            self.pop = sorted(self.pop)[:self.pop_size]
            
            best_fitness = self.pop[0].fitness

            if len(self.bfs) > 10:
                if isclose(best_fitness, self.bfs[-10]):
                    print("EARLY STOP")
                    # print("Best found solution:")
                    # print(self.pop[0])

                    return self.bfs, self.pop[0]

            self.bfs.append(best_fitness)
            if gen % monitor_rate == 0:
                print(f"Gen {gen}: best fitness {best_fitness}")

        # print("Best found solution:")
        # print(self.pop[0])

        return self.bfs, self.pop[0]

    def get_random_indi(self, range=None) -> Individual:
        if range is None:
            id = np.random.randint(0, self.pop_size)
        else:
            id = np.random.randint(0, range)
        return self.pop[id]