from math import prod
from os import path
import re


class Race:
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance

    def __str__(self):
        return f"Time: {self.time}, Distance: {self.distance}"

    def solutions(self):
        print(f"Time: {self.time}, Distance: {self.distance}")
        solutions = []
        for i in range(0, self.time + 1):
            print(
                f"  tHolding: {i}, tTravel: {self.time - i}, distance: {(self.time - i) * i}"
            )
            distance = (self.time - i) * i
            if distance > self.distance:
                solutions.append(distance)
        return solutions


lines = []
with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()

times = list(map(int, re.findall(r"\d+", lines[0])))
distances = list(map(int, re.findall(r"\d+", lines[1])))

races = []

for time, distance in zip(times, distances):
    races.append(Race(time, distance))

for race in races:
    print(race.solutions())

result = prod(map(len, [race.solutions() for race in races]))
print(f"The result for part 1 is {result}")
