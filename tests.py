import assets
import deck

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