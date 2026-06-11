import pandas as pd
import tools
from structs import Card, Hand, Suit, Rank
from calculate import score
from opponentbrain import discard
import random

def generate(player1_hand, player2_hand, cut_card):
    cut_card[0] = tools.deal(player1_hand, player2_hand, cut_card)
    player1_hand = tools.transform_cards(player1_hand, Hand(0, 0, 0, 0, 0, 0))
    player2_hand = tools.transform_cards(player2_hand, Hand(0, 0, 0, 0, 0, 0))
    cut_card[0] = tools.get_card(cut_card, Card(0, 0, 0))

def best_discard()
    

def calculate():
    player1_hand, player2_hand, crib= []
    cut_card = [0]
    crib = bool(random.getrandbits(1))
    generate(player1_hand, player2_hand, cut_card)
    comp_discard = discard(player2_hand.hand, [])
    player2_hand.remove(comp_discard[0], comp_discard[1], crib)
    if crib:
