import playcards

mydeck = playcards.create_deck()

playcards.shuffle_deck(mydeck)

print("before deal == ",mydeck,"\n")

num_players, num_cards = 3, 5

deal = playcards.deal_cards(mydeck, num_cards, num_players)

for k in range(num_players):
    print(deal[k][:])

print("\nafter deal == ",mydeck)


