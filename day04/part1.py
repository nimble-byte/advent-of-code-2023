from os import path

# sidenote: input does not contain duplicate numbers in winners or hand

# Read input
lines = []
with open(path.join(path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()

result = 0

for line in lines:
    game, numbers = line.split(":")
    winners, hand = numbers.split(" |")

    matches = 0

    # divide hand into a list of substrings length 3
    for number in [hand[i:i + 3] for i in range(0, len(hand), 3)]:
        if number in winners:
            matches += 1

    if matches > 0:
        result += pow(2, matches - 1)

print(f"The sum for part 1 is {result}")
