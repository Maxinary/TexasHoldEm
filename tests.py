import assets
import deck
import hand_value

# "ENUM" tests

print('### RANK ###')
for i in assets.RANK:
    print(i)

assert assets.RANK.TWO.value < assets.RANK.THREE.value
print(assets.RANK.TWO.value, assets.RANK.THREE.value)

print('### SUIT ###')
for i in assets.SUIT:
    print(i)


# Deck Tests
print("Shuffle Method")

x = deck.Deck()
print(x.cards)
x.shuffle()
print(x.cards)

print("Draw Method")
x = deck.Deck()
print(x.draw())
print(x.draw())

x = deck.Deck()
print(x.draw()[0])

# hand_value tests
print("hand_value methods")
x = hand_value.PlayerHand((
    (assets.RANK.ACE, assets.SUIT.CLUBS),
    (assets.RANK.EIGHT, assets.SUIT.DIAMONDS)
))