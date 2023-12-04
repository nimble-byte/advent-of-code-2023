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
    game = {}
    gameid, hands = line.split(":")

    game["game"] = int(gameid.split(" ")[1])
    game["red"] = get_max_color_count(hands, "r")
    game["green"] = get_max_color_count(hands, "g")
    game["blue"] = get_max_color_count(hands, "b")

    return game

result = 0

lines = []
with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()

for line in lines:
    game = extract_game_info(line)


    result += game["red"] * game["green"] * game["blue"]

print(f"The result for part 1 is {result}")
