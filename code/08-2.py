from os import path
import re
from math import lcm

INSTRUCT_L = "L"
INSTRUCT_R = "R"


def instruction_generator(chars):
    i = 0
    while True:
        yield chars[i % len(chars)]
        i += 1


input = open(path.join(path.dirname(__file__), "../inputs/08.txt"), "r").read()

instructions, lines = input.split("\n\n")
instructions = instruction_generator(instructions)
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


nodes = {}

for line in lines:
    name = line.split("=")[0].strip()
    nodes[name] = Node(line)

start_nodes = list(filter(lambda node: node.endswith("A"), nodes.keys()))
solution = 0

def get_cycle_length(node):
    steps = 0
    current_node = node
    while not current_node.endswith("Z"):
        current_node = nodes[current_node].get_next(next(instructions))
        steps += 1
    return steps

solution = lcm(*map(get_cycle_length, start_nodes))

print(f"The solution for 07-2 is: {solution}")
