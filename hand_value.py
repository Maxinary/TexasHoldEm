from assets import HAND, RANK, SUIT


class PlayerHand():

    def __init__(self, hand_tuple):
        self.hand_tuple = hand_tuple

        """
        Formatted as RANK SUIT
        Do something like this and the eval hand
        """

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
PlayerHand([
    (RANK.TEN, SUIT.CLUBS),
    (RANK.ACE, SUIT.CLUBS),
    (RANK.KING, SUIT.CLUBS),
    (RANK.QUEEN, SUIT.CLUBS),
    (RANK.JACK, SUIT.CLUBS),
    (RANK.FIVE, SUIT.DIAMONDS)
]).flush()