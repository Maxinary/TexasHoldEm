from assets import HAND, RANK, SUIT


class PlayerHand():

    def __init__(self, hand_tuple):
        self.hand_tuple = hand_tuple

        self.get_ranks()

    # This wont get suits but it should be somthing to the effect of this
    def get_ranks(self):
        return sorted([i[0].value for i in self.hand_tuple])

    def pair(self):
        for i, v in enumerate(self.get_ranks()):
            if i < len(self.hand_tuple) - 1:
                if [] is self.hand_tuple[i+1][0]:
                    return True

    """
    This is really hard
    I need to go down the card checks
    """

    """
    def flush(self):
        x = sorted([i[0].value for i in self.hand_tuple])
        for i in x:
    """

    '''
    def non_suit(self):
        # For non suit based hands
        # Gets ranks
        card_rank = []
        scores = []

        for card in self.hand_tuple:
            card_rank.append(card)

        # Finds how many times each card appears
        for i in card_rank:

            # TODO this really doesnt work
            # TODO need to fix look at unit test
            # TODO maybe i should use a flow chart idk???
            if card_rank.count(i) is 2:
                scores.append(HAND.ONE_PAIR)
            if card_rank.count(i) is 3:
                scores.append(HAND.THREE_OF_A_KIND)

        return scores
    '''

'''
# UNIT TEST
x = PlayerHand((
    (RANK.EIGHT, SUIT.DIAMONDS),
    (RANK.EIGHT, SUIT.DIAMONDS),
    (RANK.EIGHT, SUIT.DIAMONDS)
)).non_suit()
print(x)
'''


# Then im gonna need unit test for all of these
print(
    PlayerHand([
        (RANK.QUEEN, SUIT.CLUBS),
        (RANK.QUEEN, SUIT.CLUBS),
    ]).pair()
)

print(
    PlayerHand([
        (RANK.QUEEN, SUIT.CLUBS),
        (RANK.ACE, SUIT.HEARTS),
        (RANK.QUEEN, SUIT.CLUBS),
    ]).pair()
)

print(
    PlayerHand([
        (RANK.QUEEN, SUIT.CLUBS),
        (RANK.JACK, SUIT.HEARTS),
        (RANK.ACE, SUIT.CLUBS),
    ]).pair()
)
