# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:24:02 2018

@author: ramir
"""
SUITS = 'cdhs'
RANKS = '23456789TJQKA'
class Card:

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit
        
    def __repr__(self):
        return str(self.rank) + str(self.suit)
        
    def __gt__(self, other):
        return RANKS.index(str(self.rank)) > RANKS.index(str(other.rank))
        
    def __ge__(self, other):
        return RANKS.index(str(self.rank)) >= RANKS.index(str(other.rank))
        
    def __lt__(self, other):
        return RANKS.index(str(self.rank)) < RANKS.index(str(other.rank))
        
    def __le__(self, other):
        return RANKS.index(str(self.rank)) <= RANKS.index(str(other.rank))
        
    def __eq__(self, other):
        return RANKS.index(str(self.rank)) == RANKS.index(str(other.rank))
        
    def is_suited(self, other):
        return self.suit == other.suit
        
    def is_connected(self, other, by=1):
        return abs(RANKS.index(str(self.rank)) - RANKS.index(str(other.rank))) <= by
        
    def is_pocketpair(self, other):
        return self.rank == other.rank
        
    def is_suitedconnector(self, other):
        return self.is_suited(other) and self.is_connected(other)
        
class Deck:
    def __init__(self, cards):
        self.cards = cards
        
    def __repr__(self):
        return self.cards
        
    def shuffle(self):
        return self.cards.shuffle()
        
#class Hand:
#    def __init__(self, cards):
#        self.cards = cards
#        
#    def classify_two(self):
#        if card_1.suit == card_2