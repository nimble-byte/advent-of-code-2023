from os import path
import re

INSTRUCT_L = "L"
INSTRUCT_R = "R"

input = open(path.join(path.dirname(__file__), "../inputs/08.txt"), "r").read()

instructions, lines = input.split("\n\n")
lines = lines.splitlines()


class Path:
    def __init__(self, line):
        left, right = re.search(r"(\w{3}), (\w{3})", line).groups()
        self.left = left
        self.right = right

    def get_next(self, instruction):
        if instruction == INSTRUCT_L:
            return self.left
        elif instruction == INSTRUCT_R:
            return self.right


map = {}

for line in lines:
    name = line.split("=")[0].strip()
    map[name] = Path(line)

nodes = list(filter(lambda node: node[-1] == "A", map.keys()))
solution = 0

while any(node[-1] != "Z" for node in nodes):
    instruction = instructions[solution % len(instructions)]
    for idx, node in enumerate(nodes):
        nodes[idx] = map[node].get_next(instruction)

    solution += 1

print(f"The solution for 07-2 is: {solution}")
