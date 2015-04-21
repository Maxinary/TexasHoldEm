from assets import HAND, RANK, SUIT
from random import randint

def weighted_randint(min_val, max_val, weightedness):
    max_scaled_val=max_val-min_val
    weighted_val = 0
    for i in range(weightedness):
        weighted_val+= randint(0,int(max_scaled_val/weightedness))
    return weighted_val+min_val

class Player():
    def __init__(self, Name):
        self.value = 100 #credits for betting
    def bet():
        
class Bot():
    def __init__(self):
        self.value = weighted_randint(25,275,5);
    def bet():
        
