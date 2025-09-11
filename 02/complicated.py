import math

# I should note that this is intentionally poorly documented!
# We can make it easier by providing some hint what is going on...

# Alternatively: We could do something like Jacquard distance

class Complicated():

    def __init__(self, points, weights):
        # NOTE: There's a vague idea here that the "points" are actually defining the x & y values
        # of a point grid.
        self.points = points
        self.sqrt_weights = [math.sqrt(x) for x in weights]
        self.attenuation_rate = 0.5

    
    def set_left_comparator(self, points, point_values):
        point_distances = []
        for (i, point) in enumerate(points):
            dist = math.hypot(self.points[i][0] - point[0], self.points[i][1] - point[1])
            point_distances.append(dist)
        
        effective_point_values = []
        for (i, d) in point_distances:
            weighted_value = point_values[i] - self.attenuation_rate * d
            effective_point_values.append(weighted_value * self.sqrt_weights[i])
        
        self.left_val = effective_point_values


    def compare(self, right_point_values):
        # we just assume the right points are all on-grid
        weighted_right_points = [x[0] * x[1] for x in zip(right_point_values, self.sqrt_weights)]
        prods = [x[0] * x[1] for x in zip(weighted_right_points, self.left_val)]
        return sum(prods)
