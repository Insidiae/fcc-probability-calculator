import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
    def __init__(self, **contents):
        self.contents = []
        for item, qty in contents.items():
            for i in range(0, qty):
                self.contents.append(item)

    def draw(self, qty):
        if qty >= len(self.contents):
            return copy.copy(self.contents)

        res = []
        for i in range(0, qty):
            res.append(self.contents.pop(random.randint(0, len(self.contents) - 1)))
        return res

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    actual_counts = Counter(expected_balls)
    hit_count = 0
    
    for i in range(0, num_experiments):
        test_hat = copy.deepcopy(hat)
        exp_contents = test_hat.draw(num_balls_drawn)
        exp_counts = Counter(exp_contents)
        if len(actual_counts - exp_counts) == 0:
            hit_count += 1

    return hit_count / num_experiments
