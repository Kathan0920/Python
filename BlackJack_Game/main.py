import random 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []
sum_of_player_cards = 0
for i in range(0, 2):
    player_cards.append(random.choice(cards))
    sum_of_player_cards += player_cards[i]

print(
    f"Your two cards are = {player_cards} ,  Your cards sum = {sum_of_player_cards}"
)

for i in range(0, 2):
    dealer_cards.append(random.choice(cards))

print(f"Dealer's one card is {dealer_cards[0]}")