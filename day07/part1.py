from enum import Enum
from os import path
from collections import Counter


class CardType(Enum):
    D2 = (2,)
    D3 = (3,)
    D4 = (4,)
    D5 = (5,)
    D6 = (6,)
    D7 = (7,)
    D8 = (8,)
    D9 = (9,)
    T = (10,)
    J = (11,)
    Q = (12,)
    K = (13,)
    A = 14

    @classmethod
    def parse_char(cls, char):
        match char:
            case "2":
                return cls.D2
            case "3":
                return cls.D3
            case "4":
                return cls.D4
            case "5":
                return cls.D5
            case "6":
                return cls.D6
            case "7":
                return cls.D7
            case "8":
                return cls.D8
            case "9":
                return cls.D9
            case "T":
                return cls.T
            case "J":
                return cls.J
            case "Q":
                return cls.Q
            case "K":
                return cls.K
            case "A":
                return cls.A


class HandType(Enum):
    HIGH_CARD = (0,)
    ONE_PAIR = (1,)
    TWO_PAIRS = (2,)
    THREE_OF_A_KIND = (3,)
    FULL_HOUSE = (4,)
    FOUR_OF_A_KIND = (5,)
    FIVE_OF_A_KIND = 6


class Hand:
    def __init__(self, string, bid):
        self.bid = int(bid)
        self.cards = []
        for c in string:
            self.cards.append(CardType.parse_char(c))

    def get_card_type(self):
        counts = Counter(self.cards).values()

        if any(count == 5 for count in counts):
            return HandType.FIVE_OF_A_KIND
        elif any(count == 4 for count in counts):
            return HandType.FOUR_OF_A_KIND
        elif any(count == 3 for count in counts) and any(
            count == 2 for count in counts
        ):
            return HandType.FULL_HOUSE
        elif any(count == 3 for count in counts):
            return HandType.THREE_OF_A_KIND
        elif filter(lambda count: count == 2, counts) == 2:
            return HandType.TWO_PAIRS
        elif any(count == 2 for count in counts):
            return HandType.ONE_PAIR
        else:
            return HandType.HIGH_CARD


hands = []
with open(path.join(path.dirname(__file__), "example_input.txt")) as f:
    for cards, bid in [line.split(" ") for line in f.read().splitlines()]:
        hands.append(Hand(cards, bid))

# this needs a bit of work
ranked_hands = sorted(hands)

result = sum([hand.bid * (idx + 1) for idx, hand in enumerate(ranked_hands)])

print(f"The result for part 1 is: {result}")
