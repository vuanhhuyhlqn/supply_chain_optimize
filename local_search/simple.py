from .abstract import AbstractLocalSearch
from indi import Individual

class SimpleLocalSearch(AbstractLocalSearch):
    def __init__(self):
        super().__init__()
    def __call__(self, indi: Individual) -> Individual:
        pass