from os import path

# sidenote: input does not contain duplicate numbers in winners or hand

# Read input
lines = []
with open(path.join(path.dirname(__file__), "../inputs/04.txt")) as f:
    lines = f.read().splitlines()

result = 0

card_matches = {}

for idx, line in enumerate(lines):
    game, numbers = line.split(":")
    winners, hand = numbers.split(" |")

    matches = 0

    # divide hand into a list of substrings length 3
    for number in [hand[i : i + 3] for i in range(0, len(hand), 3)]:
        if number in winners:
            matches += 1

    card_matches[idx] = matches

# count cards afterwards
# initially all cards are avaialble exactly once
available_cards = list(card_matches.keys())

# loop over all available card (indices)
for idx in available_cards:
    result += 1
    # for each match, add the next card at the end of the list of available cards
    for id in range(1, card_matches[idx] + 1):
        available_cards.append(idx + id)


print(f"The sum for part 2 is {result}")
