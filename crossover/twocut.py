from .abstract import AbstractCrossover
import numpy as np
from indi import Individual

class TwoCutCrossover(AbstractCrossover):
    def __init__(self):
        super().__init__()
    
    def crossover(self, pa:Individual, pb:Individual) -> Individual:
        gene_a, gene_b = pa.gene, pb.gene
        gene_o = gene_a.copy()
        deli_types_o = pa.deli_types.copy()

        fi_cut : int = np.random.randint(0, pa.task.num_customers) * 3
        se_cut : int = np.random.randint(0, pa.task.num_customers) * 3

        if fi_cut > se_cut:
            fi_cut, se_cut = se_cut, fi_cut #swap
            assert(fi_cut <= se_cut)

        gene_o[fi_cut : se_cut] = gene_b[fi_cut : se_cut]
        off =  Individual(task=pa.task, gene=gene_o, deli_types=deli_types_o)
        if off.check_valid() == False:
            off.fix()
        return off

    def __call__(self, pa:Individual, pb:Individual) -> Individual:
        return self.crossover(pa, pb)