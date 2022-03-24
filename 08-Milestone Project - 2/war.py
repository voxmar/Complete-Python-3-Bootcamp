'''
Script for playing the card game War
'''

import random

values = {'Ace' : 14, 'King' : 13, 'Queen' : 12, 'Jack' : 10, 'Ten' : 10, 'Nine' : 9, 'Eight' : 8, 'Seven' : 7,
              'Six' : 6, 'Five' : 5, 'Four' : 4, 'Three' : 3, 'Two' : 2 }

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for rank in values.keys():
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_cards(self, cards):
        if type(cards) == type([]):
            self.hand.extend(cards)
        else:
            self.hand.append(cards)

    def draw_card(self):
        return self.hand.pop(0)


    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards.'