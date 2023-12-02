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


sum_part_1 = 0

lines = []
with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()

# Part 1

for line in lines:
    digits = re.sub(r'[a-z]+', '', line)

    first = int(digits[0])
    last = int(digits[-1])

    sum_part_1 += 10 * first + last

print(f'The sum for part 1 is {sum_part_1}')

# Part 2

sum_part_2 = 0

for line in lines:
    first = find_first_digit(line)
    last = find_last_digit(line)

    sum_part_2 += 10 * first + last

print(f'The sum for part 2 is: {sum_part_2}')
