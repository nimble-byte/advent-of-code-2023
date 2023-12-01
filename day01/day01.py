import re
from os import path


def replace_digits(reg_match):
    digit = reg_match.group()
    match digit:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9


def extract_digit_at(line, index):
    print(f"      index: {index}; char: {line[index]}")
    if line[index].isdigit():
        return int(line[index])
    else:
        match = re.match(
            r"^(one|two|three|four|five|six|seven|eight|nine)", line[index : index + 5]
        )
        if match:
            return replace_digits(match)


def find_first_digit(line):
    for i in range(len(line)):
        digit = extract_digit_at(line, i)
        if digit:
            return digit


def find_last_digit(line):
    for i in range(len(line))[::-1]:
        digit = extract_digit_at(line, i)
        if digit:
            return digit


sum = 0

inputPath = path.join(path.dirname(__file__), "input.txt")
file = open(inputPath, "r")
lines = file.read().splitlines()

for line in lines:
    print(line)
    first = find_first_digit(line)
    last = find_last_digit(line)

    print(f"  {first}")
    print(f"  {last}")

    sum += 10 * first + last

print(sum)
