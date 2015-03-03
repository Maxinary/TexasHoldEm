from assets import RANK, SUIT
from random import shuffle


class Deck:

    # I could make a static list which would be faster
    # But this is easier to read
    cards = [
        (suit, rank)
        for suit in SUIT
        for rank in RANK
    ]

    # Shuffles each time a new deck obj is made
    shuffle(cards)
    index = -1

    def shuffle(self):
        shuffle(self.cards)

    # Moves index up on and then returns the next card
    def draw(self):
        self.index += 1
        return self.cards[self.index]


