from os import path
import re

CUBES = {"r": 12, "g": 13, "b": 14}


def get_color_count(hand, color):
    pattern = f"(\\d+) {color}"
    color = re.search(pattern, hand)
    if color is not None:
        return int(color.group(1))
    else:
        return 0


def extract_game_info(line):
    game = {"id": None, "r": 0, "g": 0, "b": 0}
    gameid, hands = line.split(":")

    game["id"] = int(gameid.split(" ")[1])

    for hand in hands.split(";"):
        red = get_color_count(hand, "r")
        if red > game["r"]:
            game["r"] = red
        green = get_color_count(hand, "g")
        if green > game["g"]:
            game["g"] = red
        blue = get_color_count(hand, "b")
        if blue > game["b"]:
            game["b"] = blue

    return game


# Read input
lines = []
with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()

sum_part_1 = 0

for line in lines:
    # Part 1
    game = extract_game_info(line)
    if (CUBES["r"] >= game["r"] & CUBES["g"] >= game["g"] & CUBES["b"] >= game["b"]):
        sum_part_1 += game["id"]

print(f'The sum for part 1 is {sum_part_1}')
