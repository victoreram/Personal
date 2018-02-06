# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:24:02 2018

@author: ramir
"""
#RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#
#SUITS = ['']
#print(list(enumerate(RANKS)))
#class Card:
#    def __init__(self, rank, suit):
#        self.rank = rank
#        self.suit= suit
#        
#class Deck:
#    def __init__(self):
#        pass
import random
import itertools
SUITS = 'cdhs'
RANKS = '23456789TJQKA'
DECK = tuple(''.join(card) for card in itertools.product(RANKS, SUITS))
hand = random.sample(DECK, 2)
print(hand)

class Player:
    def __init__(self, stack=100):
        self.stack = stack
        
PLAYERS = [Player(), Player()]