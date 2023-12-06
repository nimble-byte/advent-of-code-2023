from math import ceil
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


lines = []
with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()

time = int(lines[0].replace(" ", "").split(":")[1])
distance = int(lines[1].replace(" ", "").split(":")[1])

race = Race(time, distance)
solutions = race.solutions()

print(f"Number of solutions: {len(solutions)}")
