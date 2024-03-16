from enum import Enum

# Create an enum in python
class HandType(Enum):
    FIVE_OF_A_KIND = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7

card_map = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1
}

hand_upgrade_map = {
    HandType.FIVE_OF_A_KIND: HandType.FIVE_OF_A_KIND,
    HandType.FOUR_OF_A_KIND: HandType.FIVE_OF_A_KIND,
    HandType.FULL_HOUSE: HandType.FOUR_OF_A_KIND,
    HandType.THREE_OF_A_KIND: HandType.FOUR_OF_A_KIND,
    HandType.TWO_PAIR: HandType.FULL_HOUSE,
    HandType.ONE_PAIR: HandType.THREE_OF_A_KIND,
    HandType.HIGH_CARD: HandType.ONE_PAIR,
}


def parse_input(path: str):
    # read input from txt file
    f = open(path, "r")
    lines = f.readlines()
    all_cards = []
    all_bids =  []
    for line in lines:
        cards, bid =line.split()
        all_cards.append(cards)
        all_bids.append(bid)
    return all_cards, all_bids


class Hand:
    def __init__(self, cards, bid):
        self.cards: str = cards
        self.bid: int = int(bid)
        self.type: HandType = self.get_type()

    def get_base_type(self):
        # Is it five of a kind?
        cards = self.cards
        if cards[0] == cards[1] == cards[2] == cards[3] == cards[4]:
            return HandType.FIVE_OF_A_KIND
        # Is it four of a kind?
        for card in cards:
            if cards.count(card) == 4 and card != "J":
                return HandType.FOUR_OF_A_KIND
        # is it three of a kind?
        three_of_a_kind = False
        for card in cards:
            if cards.count(card) == 3 and card != "J":
                three_of_a_kind = True
                break
        # is it two of a kind?
        two_of_a_kind_count = 0
        already_counted = ""
        for card in cards:
            if cards.count(card) == 2 and card != "J":
                if card in already_counted:
                    continue
                already_counted += card
                two_of_a_kind_count += 1

        if three_of_a_kind and (two_of_a_kind_count == 1):
            return HandType.FULL_HOUSE
        elif three_of_a_kind:
            return HandType.THREE_OF_A_KIND
        elif two_of_a_kind_count == 2:
            return HandType.TWO_PAIR
        elif two_of_a_kind_count == 1:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    def upgrade_hand(self):
        self.type = hand_upgrade_map[self.type]

    def get_type(self):
        type_ = self.get_base_type()
        for _ in range(self.cards.count("J")):
            type_ = hand_upgrade_map[type_]
        return type_

    def is_better_than(self, hand2):
        if self.type.value < hand2.type.value:
            return True
        elif self.type.value > hand2.type.value:
            return False
        else:
            return compare_equal_hands(self, hand2)

    def __repr__(self) -> str:
        return f"cards: {self.cards}, bid: {self.bid}, type: {self.type}\n"


class SortedList:
    def __init__(self):
        self.hands = []

    def append(self, hand):
        self.hands.append(hand)

    def insert(self, hand):
        for i, h in enumerate(self.hands):
            if hand.is_better_than(h):
                self.hands.insert(i, hand)
                return

        self.hands.append(hand)

    def __len__(self):
        return len(self.hands)

    def __getitem__(self, index):
        return self.hands[index]

    def __repr__(self) -> str:
        return str(self.hands)


def compare_equal_hands(hand1, hand2):
    # Checks which hand wins the tiebreaker
    for card1, card2 in zip(hand1.cards, hand2.cards):
        if card_map[card1] > card_map[card2]:
            return True
        elif card_map[card1] < card_map[card2]:
            return False
    else:
        print("Error: hands are equal")
        return True


def sort_hands(hands):
    sorted_list = SortedList()
    for h in hands:
        sorted_list.insert(h)
    return sorted_list

def main():

    cards, bids = parse_input("day7/input.txt")
    hands = [Hand(card, bid) for card, bid in zip(cards, bids)]

    sorted_hands = sort_hands(hands)

    total_winnings = 0
    for i, h in enumerate(sorted_hands):
        rank = len(sorted_hands) - i
        total_winnings += h.bid * rank
        # print("rank:", rank, "winnings", h.bid, "*", rank)

    print("Total winning:", total_winnings)

if __name__ == "__main__":
    main()