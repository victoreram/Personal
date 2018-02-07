# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:58:22 2018

@author: ramir
"""

import random
import itertools


SUITS = 'cdhs'
RANKS = '23456789TJQKA'
DECK = list(''.join(card) for card in itertools.product(RANKS, SUITS))
random.shuffle(DECK)
print(DECK)
hand = [DECK.pop(), DECK.pop()]
print(hand, len(DECK))
