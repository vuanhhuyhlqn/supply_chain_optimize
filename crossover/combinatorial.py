from .abstract import AbstractCrossover
import numpy as np
from indi import Individual

class CombinatorialCrossover(AbstractCrossover):
    def __init__(self, pc=0.5):
        super().__init__()
        self.pc = pc
    
    def crossover(self, pa:Individual, pb:Individual) -> Individual:
        gene_a, gene_b = pa.gene, pb.gene
        gene_o = gene_a.copy()
        deli_types_o = pa.deli_types.copy()

        for cid in range(pa.task.num_customers):
            if np.random.uniform() < self.pc:
                deli_types_o[cid] = pb.deli_types[cid]
                gene_o[cid * 3 : (cid * 3 + 3)] = gene_b[cid * 3 : (cid * 3 + 3)]

        off =  Individual(task=pa.task, gene=gene_o, deli_types=deli_types_o)
        while off.check_valid() == False:
            off.fix()
        off.fitness = off.eval()
        return off
    
    def __call__(self, pa:Individual, pb:Individual) -> Individual:
        return self.crossover(pa, pb)