# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:24:02 2018

@author: ramir
"""

import random
import itertools
import Card


def convert_to_card(cards):
    deck = []
    for card in cards:
        card = Card.Card(card[0], card[1])
        deck.append(card)
    return deck
    
def classify(hand):
    pass
    

PLAYERS = [[]]
player_1 = PLAYERS[0]

SUITS = 'cdhs'
RANKS = '23456789TJQKA'
DECK = list(''.join(card) for card in itertools.product(RANKS, SUITS))
random.shuffle(DECK)


DECK = convert_to_card(DECK)
print(DECK)

hand = [DECK.pop(), DECK.pop()]
print(DECK)
print(hand)
card_1, card_2 = hand
print(card_1 > card_2)
print(card_1.is_suited(card_2))
print(card_1.is_connected(card_2))
print(card_1.is_connected(card_2, by=3))
print(card_1.is_pocketpair(card_2))
print(card_1.is_suitedconnector(card_2))


#DECK = Card.Deck(''.join(card) for card in itertools.product(RANKS, SUITS))
##random.shuffle(DECK)
#DECK = DECK.shuffle()
#
#DECK = convert_to_card(DECK)
#print(DECK)
#
#hand = [DECK.pop(), DECK.pop()]
#print(DECK, hand)


   
    

#class Deck:
#    def __init__(self):
#        SUITS = 'cdhs'
#        RANKS = '23456789TJQKA'
#        self.DECK = list(''.join(card) for card in itertools.product(RANKS, SUITS))
#        
#    @property
#    def deck(self):
#        return self.DECK
#            
#    def deal(self, recipient):
#         recipient.append(random.sample(self.DECK, 2))
#    
#class Player:
#    def __init__(self, stack=100):
#        self.stack = stack
#        self.cards = []
#        
#    
#deck = Deck()
#cards = deck.deck
#print(cards)
#player_1 = []
#deck.deal(player_1)
#print(player_1)
#print(cards)
#PLAYERS = [Player(), Player()]