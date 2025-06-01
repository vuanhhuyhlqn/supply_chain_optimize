from .abstract import AbstractLocalSearch
from indi import Individual

class SimpleLocalSearch(AbstractLocalSearch):
	def __init__(self):
		super().__init__()
	
	def localsearch(self, p: Individual) -> Individual:
		gene_p = p.gene
		deli_types_p = p.deli_types
		
		gene_x = gene_p.copy()
		deli_types_x = deli_types_p.copy()
		task = p.task

		best_gene_x = gene_x.copy()
		best_deli_types_x = deli_types_x.copy()
		best_fitness = p.fitness

		for cid in range(p.task.num_customers):
			for new_deli_type in range(4):
				deli_types_x[cid] = new_deli_type
				x = Individual(task=task, gene=gene_x, deli_types=deli_types_x)
				
				while x.check_valid == False:
					x.fix()
					gene_x = x.gene.copy()
					deli_types_x = x.deli_types.copy()

				x.fitness = x.eval()

				if x.fitness < best_fitness:
					best_fitness = x.fitness
					best_gene_x = x.gene.copy()
					best_deli_types_x = x.deli_types.copy()
		
		return Individual(task=task, gene=best_gene_x, deli_types=best_deli_types_x)


	def __call__(self, p: Individual) -> Individual:
		return self.localsearch(p)