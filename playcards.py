# Module palycards

def create_deck():
    rank_string = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
    suit_string = ("C","D","H","S")
    cards = []
    for suit in range(4):
        for rank in range(13):
            card_string = rank_string[rank] + suit_string[suit]
            cards.append(card_string)
    return cards

import random as rnd 

def shuffle_deck(deck):
    rnd.shuffle(deck)
    return

def deal_cards(deck, num_cards, num_players):
    deal = [[0 for x in range(num_cards)] for y in range(num_players)]
    for i in range(num_cards):
        for k in range(num_players):
            deal[k][i]=deck.pop(0)
    return deal
