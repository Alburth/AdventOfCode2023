from day7.problem import Hand, HandType, sort_hands

def test_get_type():
    five_of_a_kind = "AAAAA"
    four_of_a_kind = "KAAAA"
    four_of_a_kind1 = "AKAAA"
    four_of_a_kind2 = "AAKAA"
    four_of_a_kind3 = "AAAKA"
    four_of_a_kind4 = "AAAAK"
    full_house = "AKKAA"
    three_of_a_kind = "AKJAA"
    high_card = "AKQJT"
    two_pairs = "KK677"
    one_pair = "KK678"
    bid = 1
    hand1 = Hand(five_of_a_kind, bid)
    hand2 = Hand(four_of_a_kind, bid)
    hand21 = Hand(four_of_a_kind1, bid)
    hand22 = Hand(four_of_a_kind2, bid)
    hand23 = Hand(four_of_a_kind3, bid)
    hand24 = Hand(four_of_a_kind4, bid)
    hand3 = Hand(full_house, bid)
    hand4 = Hand(three_of_a_kind, bid)
    hand5 = Hand(two_pairs, bid)
    hand6 = Hand(high_card, bid)
    hand7 = Hand(one_pair, bid)
    hand8 = Hand("3J4KT", bid)
    hand9 = Hand("33399", bid)
    hand10 = Hand("TATJA", bid)

    assert hand1.get_type() == HandType.FIVE_OF_A_KIND
    assert hand2.get_type() == HandType.FOUR_OF_A_KIND
    assert hand21.get_type() == HandType.FOUR_OF_A_KIND
    assert hand22.get_type() == HandType.FOUR_OF_A_KIND
    assert hand23.get_type() == HandType.FOUR_OF_A_KIND
    assert hand24.get_type() == HandType.FOUR_OF_A_KIND
    assert hand3.get_type() == HandType.FULL_HOUSE
    assert hand4.get_type() == HandType.THREE_OF_A_KIND
    assert hand5.get_type() == HandType.TWO_PAIR
    assert hand6.get_type() == HandType.HIGH_CARD
    assert hand7.get_type() == HandType.ONE_PAIR
    assert hand8.get_type() == HandType.HIGH_CARD
    assert hand9.get_type() == HandType.FULL_HOUSE
    assert hand10.get_type() == HandType.TWO_PAIR
    print("All Type tests passed!")


def test_sorting():
    hands = [
        Hand("555J5", 1),
        Hand("44494", 1),
        Hand("TTTT8", 1),
        Hand("33399", 1),
        Hand("9999A", 1),
        Hand("44499", 1),
        Hand("83333", 1),
    ]

    # recursive_sort(hands)
    hands = sort_hands(hands)
    print(hands)
    assert hands[0].cards == "TTTT8"
    assert hands[1].cards == "9999A"
    assert hands[2].cards == "83333"
    assert hands[3].cards == "555J5"
    assert hands[4].cards == "44494"
    assert hands[5].cards == "44499"
    assert hands[6].cards == "33399"
    print("All sorting tests passed!")

def test_hand_upgrade():
    hand = Hand("555J5", 1)
    hand2 = Hand("55JJ5", 1)
    hand3 = Hand("5JJJ5", 1)
    fullHouse = Hand("2233J", 1)
    assert hand.get_type() == HandType.FIVE_OF_A_KIND
    assert hand2.get_type() == HandType.FIVE_OF_A_KIND
    assert hand3.get_type() == HandType.FIVE_OF_A_KIND
    assert fullHouse.get_type() == HandType.FULL_HOUSE
    print("All upgrade tests passed!")

test_hand_upgrade()
# test_get_type()
# test_sorting()
