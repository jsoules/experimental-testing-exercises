

class RunningAverage():
    
    def __init__(self):
        self.item_count = 0
        self.average = 0.0


    def report_average(self):
        print(f"Average: {self.average} over {self.item_count} items")


    def add_item(self, item: float):
        total = self.item_count * self.average
        new_total = total + item
        self.item_count += 1
        self.average = new_total / self.item_count

    # BRIAN -- note we can make it more complicated by implementing smarter algorithms/approximations, Kahan summation, ...
    # Note, I'm BY NO MEANS married to an object-oriented implementation of this

