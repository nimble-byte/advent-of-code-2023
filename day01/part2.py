from os import path
import re

result = 0

lines = []
with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()


def map_digits(reg_match):
    digit = reg_match.group()
    match digit:
        case "one" | "1":
            return 1
        case "two" | "2":
            return 2
        case "three" | "3":
            return 3
        case "four" | "4":
            return 4
        case "five" | "5":
            return 5
        case "six" | "6":
            return 6
        case "seven" | "7":
            return 7
        case "eight" | "8":
            return 8
        case "nine" | "9":
            return 9


def find_first(line):
    return map_digits(
        re.search(r"(one|two|three|four|five|six|seven|eight|nine|\d)", line)
    )


def find_last(line):
    for idx in range(len(line), -1, -1):
        reg_match = re.match(
            r"(one|two|three|four|five|six|seven|eight|nine|\d)", line[idx:]
        )
        if reg_match is not None:
            return map_digits(reg_match)


for line in lines:
    first = find_first(line)
    last = find_last(line)

    result += first * 10 + last

print(f"The result for part 2 is {result}")
