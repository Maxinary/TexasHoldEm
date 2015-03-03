from assets import *


class PlayerHand():

    def __init__(self, hand_tuple):
        self.hand_tuple = hand_tuple

        # Do somthing like this and the eval hand
        for cards in self.hand_tuple:
            print('\n')
            for card in cards:
                print(card, end=' | ')