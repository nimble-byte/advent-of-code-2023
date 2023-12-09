from os import path

input = open(path.join(path.dirname(__file__), "../inputs/09.txt"), "r").read()

lines = [list(map(int, line.split())) for line in input.splitlines()]


def extrapolate(value_history):
    differences = []
    for i in range(len(value_history) - 1):
        differences.append(value_history[i + 1] - value_history[i])

    if all(difference == 0 for difference in differences):
        return value_history[-1]
    else:
        return value_history[-1] + extrapolate(differences)


result = sum(map(extrapolate, lines))
print(f"The solution for 09-1 is: {result}")
