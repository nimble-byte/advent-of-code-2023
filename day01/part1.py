from os import path
import re

result = 0

lines = []
with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()

for line in lines:
    digits = re.findall(r"\d", line)

    result += int(digits[0]) * 10 + int(digits[-1])

print(f"The result for part 1 is {result}")
