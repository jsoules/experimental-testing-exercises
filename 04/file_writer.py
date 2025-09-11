import random
from pathlib import Path

class FileInteractionManager():
    def __init__(self, root_dir="output"):
        self.root_dir = Path(root_dir)


    def save_1(self, v):
        with open(self.root_dir / 'out1.txt', "w") as f:
            f.write(v)

    
    def save_2(self, v):
        with open(self.root_dir / 'out2.csv', "w") as f:
            f.write(v)


    def save_3(self, v):
        with open(self.root_dir / "out3.txt", "a") as f:
            f.write(v)


class DataProcessor():

    def __init__(self):
        self.options = ["option 1", "option 2", "option 3", "option 4"]
        self.result_1 = None
        self.result_2 = None
        self.result_3 = None


    def compute_value_1(self):
        self.result_1 = random.random()


    def compute_value_2(self, draws = 3):
        self.result_2 = random.choices(self.options, k=draws)


    def compute_value_3(self, n=3, p=0.5):
        self.result_3 = random.binomialvariate(n, p)


    def write_files(self, file_mgr):
        if self.result_1 is not None:
            file_mgr.save_1(self.result_1)
        if self.result_2 is not None:
            file_mgr.save_2(self.result_2)
        if self.result_3 is not None:
            file_mgr.save_3(self.result_3)
