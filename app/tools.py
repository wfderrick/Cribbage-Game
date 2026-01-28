import random
import structs


def deal(player1_hand, player2_hand, cut_card):
    curr_cards = structs.CONST_CARDS.copy
    deal_opts = []
 
    for i in range(13):
        new_card = int(random.random() * 52)
        while new_card in deal_opts:
            new_card = int(random.random() * 52)
        deal_opts.append(new_card)

    for i in range(6):
        player1_hand.append(deal_opts.pop(0))
        player2_hand.append(deal_opts.pop(0))

    cut_card = deal_opts.pop(0)

    return cut_card
    

def transform_cards(player_nums, player_hand):
    player_hand.card1 = get_card(player_nums[0], structs.Card(0, 0, 0))
    player_hand.card2 = get_card(player_nums[1], structs.Card(0, 0, 0))
    player_hand.card3 = get_card(player_nums[2], structs.Card(0, 0, 0))
    player_hand.card4 = get_card(player_nums[3], structs.Card(0, 0, 0))
    player_hand.card5 = get_card(player_nums[4], structs.Card(0, 0, 0))
    player_hand.card6 = get_card(player_nums[5], structs.Card(0, 0, 0))
    return player_hand

def get_card(num, card):
    if num < 14:
        card.suit = structs.Suit.CLUBS
    elif num < 27:
        card.suit = structs.Suit.DIAMONDS
    elif num < 40:
        card.suit = structs.Suit.HEARTS
    else:
        card.suit = structs.Suit.SPADES
    
    temp = num % 13

    if temp == 0:
        card.value = 10
        card.face = structs.Face.KING
    elif temp == 1:
        card.value = 1
        card.face = structs.Face.ACE
    elif temp == 2:
        card.value = 2
        card.face = structs.Face.TWO
    elif temp == 3:
        card.value = 3
        card.face = structs.Face.THREE
    elif temp == 4:
        card.value = 4
        card.face = structs.Face.FOUR
    elif temp == 5:
        card.value = 5
        card.face = structs.Face.FIVE
    elif temp == 6:
        card.value = 6
        card.face = structs.Face.SIX
    elif temp == 7:
        card.value = 7
        card.face = structs.Face.SEVEN
    elif temp == 8:
        card.value = 8
        card.face = structs.Face.EIGHT
    elif temp == 9:
        card.value = 9
        card.face = structs.Face.NINE
    elif temp == 10:
        card.value = 10
        card.face = structs.Face.TEN
    elif temp == 11:
        card.value = 10
        card.face = structs.Face.JACK
    elif temp == 12:
        card.value = 10
        card.face = structs.Face.QUEEN
    
    return card

def get_vals(player_hand, vals):
    