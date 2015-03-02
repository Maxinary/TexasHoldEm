#!/usr/bin/python3

import assets


### "ENUM" tests ###

print('### RANK ###')
for i in assets.RANK:
	print(i)

assert assets.RANK.TWO.value < assets.RANK.THREE.value
print(assets.RANK.TWO.value, assets.RANK.THREE.value)

print('### SUIT ###')
for i in assets.SUIT:
	print(i)

print('### COLOR ###')
for i in assets.COLOR:
	print(i)