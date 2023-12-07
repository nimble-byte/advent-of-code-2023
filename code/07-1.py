from enum import Enum
from os import path
from collections import Counter


class CardType(Enum):
    D2 = 2
    D3 = 3
    D4 = 4
    D5 = 5
    D6 = 6
    D7 = 7
    D8 = 8
    D9 = 9
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14

    def __str__(self) -> str:
        match self.name:
            case "D2":
                return "2"
            case "D3":
                return "3"
            case "D4":
                return "4"
            case "D5":
                return "5"
            case "D6":
                return "6"
            case "D7":
                return "7"
            case "D8":
                return "8"
            case "D9":
                return "9"
            case "T":
                return "T"
            case "J":
                return "J"
            case "Q":
                return "Q"
            case "K":
                return "K"
            case "A":
                return "A"

    @classmethod
    def parse_char(cls, char) -> "CardType":
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
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

    def __str__(self) -> str:
        return self.name


class Hand:
    def __init__(self, string, bid):
        self.bid = int(bid)
        self.cards = []
        for c in string:
            self.cards.append(CardType.parse_char(c))

    def __str__(self) -> str:
        return f"{"".join([str(card) for card in self.cards])} ({self.bid})"

    def get_hand_type(self) -> HandType:
        counts = [count for _, count in Counter(self.cards).most_common()]

        match counts:
            case [5, *_]:
                return HandType.FIVE_OF_A_KIND
            case [4, *_]:
                return HandType.FOUR_OF_A_KIND
            case [3, 2, *_]:
                return HandType.FULL_HOUSE
            case [3, *_]:
                return HandType.THREE_OF_A_KIND
            case [2, 2, *_]:
                return HandType.TWO_PAIRS
            case [2, *_]:
                return HandType.ONE_PAIR
            case _ :
                return HandType.HIGH_CARD


hands = []
with open(path.join(path.dirname(__file__), "../inputs/07.txt")) as f:
    for cards, bid in [line.split(" ") for line in f.read().splitlines()]:
        hands.append(Hand(cards, bid))


def sort_key(hand):
    return hand.get_hand_type().value, [card.value for card in hand.cards]


# this needs a bit of work
ranked_hands = sorted(hands, key=sort_key)

result = sum([hand.bid * (idx + 1) for idx, hand in enumerate(ranked_hands)])

print(f"The result for part 1 is: {result}")
