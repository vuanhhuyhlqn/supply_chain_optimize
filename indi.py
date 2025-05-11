import numpy as np
from task import Task

class Individual:
    def __init__(self, task: Task):
        self.task = task
    
    def check_valid(self):
        pass

    def fix(self):
        pass

    def eval(self):
        pass
