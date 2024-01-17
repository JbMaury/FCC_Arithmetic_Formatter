import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, number):
        list_of_balls = []
        if number > len(self.contents):
            list_of_balls = self.contents.copy()
        else:
            for i in range(0, number):
                r = random.randrange(0, len(self.contents))
                list_of_balls.append(self.contents[r])
                self.contents.pop(r)
        return list_of_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for i in range(0, num_experiments):
        copy_hat = copy.deepcopy(hat)
        actual_list = copy_hat.draw(num_balls_drawn)
        has_balls = all(actual_list.count(color) >= count for color, count in expected_balls.items())
        if has_balls:

            success_count += 1

    probability = (success_count / num_experiments)

    return round(probability, 3)



