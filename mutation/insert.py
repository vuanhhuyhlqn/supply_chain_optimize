from .abstract import AbstractMutation
import numpy as np
from indi import Individual

class InsertionMutation:
	def __init__(self):
		super().__init__()
	
	def mutation(self, p:Individual) -> Individual:
		off : Individual = p.copy()

		pos1 : int = np.random.randint(0, off.task.num_customers) * 3
		pos2 : int = np.random.randint(0, off.task.num_customers) * 3
		if pos1 > pos2:
			pos1, pos2 = pos2, pos1 #swap
			assert(pos1 <= pos2)
		
		insert_unit = off.gene[pos2 : (pos2 + 3)].copy()
		off.gene[(pos1 + 3) : (pos2 + 3)] = off.gene[pos1 : pos2]
		off.gene[pos1 : (pos1 + 3)] = insert_unit

		if off.check_valid() == False:
			off.fix()
		return off

	def __call__(self, p:Individual) -> Individual:
		return self.mutation(p)