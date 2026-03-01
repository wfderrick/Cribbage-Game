import random
import structs


# int list, int list, int -> CARD
# The deal function takes in two lists of integers and a single integer and uses them to create a hand for the player,
# a hand for the computer, and a cut card.
def deal(player1_hand, player2_hand, cut_card):
    player1_hand.clear
    player2_hand.clear
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


# int list, Hand object -> A Hand object full of card objects
# Takes in a list of integers between 1 and 52 and using the get_card function converts each number
# into its corresponding Card object and places it into a slot in the parameter Hand object.
def transform_cards(player_nums, player_hand):
    track = 0
    for i in player_nums:
        player_hand.hand[track] = get_card(i, structs.Card(0, 0, 0))
        track += 1

    return player_hand


# int, Card object -> A card object with values corresponding to the number
# Take in an integer between 1 and 52 and a Card object. Using the number each attribute of the parameter card
# object is filled to create the corresponding card for the number.
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
        card.rank = structs.Rank.KING
    elif temp == 1:
        card.value = 1
        card.rank = structs.Rank.ACE
    elif temp == 2:
        card.value = 2
        card.rank = structs.Rank.TWO
    elif temp == 3:
        card.value = 3
        card.rank = structs.Rank.THREE
    elif temp == 4:
        card.value = 4
        card.rank = structs.Rank.FOUR
    elif temp == 5:
        card.value = 5
        card.rank = structs.Rank.FIVE
    elif temp == 6:
        card.value = 6
        card.rank = structs.Rank.SIX
    elif temp == 7:
        card.value = 7
        card.rank = structs.Rank.SEVEN
    elif temp == 8:
        card.value = 8
        card.rank = structs.Rank.EIGHT
    elif temp == 9:
        card.value = 9
        card.rank = structs.Rank.NINE
    elif temp == 10:
        card.value = 10
        card.rank = structs.Rank.TEN
    elif temp == 11:
        card.value = 10
        card.rank = structs.Rank.JACK
    elif temp == 12:
        card.value = 10
        card.rank = structs.Rank.QUEEN

    return card


# Hand object, List -> Adds all cards from the Hand object to the list
# Takes in a Hand object and a list. The function checks each slot for a card. If there is not a card
# in the slot (aka the value is -1) then nothing is added to the list. Otherwise each card is appended
# to the end of the list.
def hand_to_list(hand, hand_list):
    if hand.card1 != -1:
        hand_list.append(hand.card1)
    if hand.card2 != -1:
        hand_list.append(hand.card2)
    if hand.card3 != -1:
        hand_list.append(hand.card3)
    if hand.card4 != -1:
        hand_list.append(hand.card4)
    if hand.card5 != -1:
        hand_list.append(hand.card5)
    if hand.card6 != -1:
        hand_list.append(hand.card6)
