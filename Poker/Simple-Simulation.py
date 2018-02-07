# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:24:02 2018

@author: ramir
"""

import random
import itertools
import Card
import pandas as pd


def convert_to_card(cards):
    deck = []
    for card in cards:
        card = Card.Card(card[0], card[1])
        deck.append(card)
    return deck
    
def classify(hand):
    pass
    
def initialize_deck():
    SUITS = 'cdhs'
    RANKS = '23456789TJQKA'
    DECK = list(''.join(card) for card in itertools.product(RANKS, SUITS))
    random.shuffle(DECK)
    DECK = convert_to_card(DECK)
    return DECK
    
def deal(deck, to):
    pass

### INITIATE CONDITIONS
PLAYERS = [[]]
player_1 = PLAYERS[0]
n_simulations = int(1E5)
hand_types = {'Pocket Pair':0, 'Suited Connector':0, 'Suited':0, 'Connected':0, 'Has Ace':0}

for i in range(n_simulations):
    DECK = initialize_deck()
    card1, card2 = [DECK.pop(), DECK.pop()]
    if card1.is_pocketpair(card2):
        hand_types['Pocket Pair'] += 1
    if card1.is_suitedconnector(card2):
        hand_types['Suited Connector'] += 1
    if card1.is_suited(card2):
        hand_types['Suited'] += 1
    if card1.is_connected(card2):
        hand_types['Connected'] += 1
    if (card1.rank or card2.rank) == 'A':
        hand_types['Has Ace'] += 1
        
hand_probs = pd.DataFrame(hand_types, index=['probability (%)'])
hand_probs *= (100/n_simulations)
print("n = %s simulations" % n_simulations)
print(hand_probs)
