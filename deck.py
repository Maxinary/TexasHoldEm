from assets import RANK, SUIT
from random import shuffle


class Deck:

    cards = [
        (suit, rank)
        for suit in SUIT
        for rank in RANK
    ]

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

x = Deck()
print(x.cards)
x.draw()
print(x.cards)