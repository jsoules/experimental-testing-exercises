### TODO: Identify properties that are worth testing,
# and implement tests for them.
#
# Suggested properties to test:
#  - Average is correctly calculated for a small list
#  - Item count is correct before/after adding items

class RunningAverage():
    def __init__(self):
        self.item_count = 0
        self.average = 0.0


    def current_average(self):
        return self.average


    def current_item_count(self):
        return self.item_count


    def add_item(self, item: float):
        total = self.item_count * self.average
        new_total = total + item
        self.item_count += 1
        self.average = new_total / self.item_count
