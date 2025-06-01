from .abstract import AbstractCrossover
import numpy as np
from indi import Individual
from numba import jit

class TwoCutCrossover(AbstractCrossover):
    def __init__(self):
        super().__init__()
        
    @jit(nopython=True)
    def crossover(self, pa:Individual, pb:Individual) -> Individual:
        gene_a, gene_b = pa.gene, pb.gene
        gene_o = gene_a.copy()

        deli_types_o = pa.deli_types.copy()
        rnd = np.random.uniform(size=deli_types_o.shape)
        deli_types_o[rnd < 0.5] = pb.deli_types[rnd < 0.5]

        fi_cut : int = np.random.randint(0, pa.task.num_customers) * 3
        se_cut : int = np.random.randint(0, pa.task.num_customers) * 3

        if fi_cut > se_cut:
            fi_cut, se_cut = se_cut, fi_cut #swap
            assert(fi_cut <= se_cut)

        gene_o[fi_cut : se_cut] = gene_b[fi_cut : se_cut]
        off =  Individual(task=pa.task, gene=gene_o, deli_types=deli_types_o)
        if off.check_valid() == False:
            off.fix()
        off.fitness = off.eval()
        return off

    def __call__(self, pa:Individual, pb:Individual) -> Individual:
        return self.crossover(pa, pb)