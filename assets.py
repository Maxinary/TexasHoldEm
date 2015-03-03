from enum import Enum


class RANK(Enum):
    TWO = 0
    THREE = 1
    FOUR = 2
    FIVE = 3
    SIX = 4
    SEVEN = 5
    EIGHT = 6
    NINE = 7
    TEN = 8
    JACK = 9
    QUEEN = 10
    KING = 11
    ACE = 12


class SUIT(Enum):
    SPADES = 0
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3


class HAND(Enum):
    """
    I will still need to specify specific values
    ie a pair of 2's vs a pair of 4's but the HAND
    is olny for specify general hand ranks

    http://www.myrakesite.com/website_images/4261/PokerHandRankings.png
    """
    ONE_PAIR = 0
    TWO_PAIR = 1
    THREE_OF_A_KIND = 2
    STRAIGHT = 3
    FLUSH = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    ROYAL_FLUSH = 7