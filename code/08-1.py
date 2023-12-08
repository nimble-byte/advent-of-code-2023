from os import path
import re

STARTING_NODE = "AAA"
END_NODE = "ZZZ"
INSTRUCT_L = "L"
INSTRUCT_R = "R"

input = open(path.join(path.dirname(__file__), "../inputs/08.txt"), "r").read()

instructions, lines = input.split("\n\n")
lines = lines.splitlines()


class Node:
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
    map[name] = Node(line)

node = STARTING_NODE
solution = 0 # can reuse this to determine next instruction...
while node != END_NODE:
    instruction = instructions[solution % len(instructions)]
    node = map[node].get_next(instruction)
    solution += 1

print(f"The solution for 07-1 is: {solution}")
