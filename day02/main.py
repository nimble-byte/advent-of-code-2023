from os import path
import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def get_max_color_count(hand, color):
    pattern = f"(\\d+) {color}"
    counts = re.findall(pattern, hand)
    if len(counts) == 0:
        return 0
    else:
        return max([int(count) for count in counts])


def extract_game_info(line):
    game = []
    gameid, hands = line.split(":")

    game.append(int(gameid.split(" ")[1]))
    game.append(get_max_color_count(hands, "r"))
    game.append(get_max_color_count(hands, "g"))
    game.append(get_max_color_count(hands, "b"))

    return game


# Read input
lines = []
with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()

sum_part_1 = 0
sum_part_2 = 0

for line in lines:
    game = extract_game_info(line)

    # Part 1
    if game[1] <= MAX_RED and game[2] <= MAX_GREEN and game[3] <= MAX_BLUE:
        sum_part_1 += game[0]

    # Part 2
    sum_part_2 += game[1] * game[2] * game[3]

print(f"The sum for part 1 is {sum_part_1}")
print(f"The sum for part 2 is {sum_part_2}")
