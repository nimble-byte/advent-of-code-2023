from math import ceil, floor, sqrt
from os import path


class Race:
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance

    def __str__(self):
        return f"Time: {self.time}, Distance: {self.distance}"

    def solutions(self):
        # print(f"Time: {self.time}, Distance: {self.distance}")
        solutions = []
        for i in range(0, self.time + 1):
            # print(
            #     f"  tHolding: {i}, tTravel: {self.time - i}, distance: {(self.time - i) * i}"
            # )
            distance = (self.time - i) * i
            if distance > self.distance:
                solutions.append(distance)
        return solutions

    def solutions_smart(self):
        # calculate the number of solutions directly by calculating minimum and maximum holding time
        # distance travelled = d
        # time holding = h
        # overall time = t
        # d = (t - h) * h => 0 = h^2 - th + d
        # use quadratic formula to solve for roots
        # lb = (t - sqrt(t^2 - 4d)) / 2
        # ub = (t + sqrt(t^2 - 4d)) / 2
        print(f"Time: {self.time}, Distance: {self.distance}")
        lb = ceil((self.time - sqrt(self.time ** 2 - 4 * self.distance + 1)) / 2)
        ub = floor((self.time + sqrt(self.time ** 2 - 4 * self.distance + 1)) / 2)

        return ub - lb + 1



lines = []
with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()

time = int(lines[0].replace(" ", "").split(":")[1])
distance = int(lines[1].replace(" ", "").split(":")[1])

race = Race(time, distance)
# solutions = race.solutions()

# print(f"Number of solutions: {len(solutions)}")
solutions = race.solutions_smart()
print(f"Number of solutions: {solutions}")

