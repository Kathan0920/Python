import random 
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clrscr():
    click.clear()

wantToPlay = input("Want to start Black Jack game? Type 'yes' to start else type 'no'. ").lower()

if wantToPlay == "yes":
    clrscr()
    print(logo)
    player_cards = []
    dealer_cards = []
    sum_of_player_cards = 0
    sum_of_dealer_cards = 0

    for i in range(0, 2):
        player_cards.append(random.choice(cards))
        sum_of_player_cards += player_cards[i]
    
    print(
        f"Your two cards are = {player_cards} ,  Your cards sum = {sum_of_player_cards}"
    )
    
    for i in range(0, 2):
        dealer_cards.append(random.choice(cards))
    
    print(f"Dealer's one card is {dealer_cards[0]}")
    
    for card_value in dealer_cards:
        sum_of_dealer_cards += card_value
    
    pickNextCard = "y"
    
    while pickNextCard == "y":
    
        pickNextCard = input("Type 'y' to pick a next card. Otherwise type 'n' to pass. ").lower()
        
        if pickNextCard == "y":
            player_cards.append(random.choice(cards))
            print(f"Your next card is {player_cards[-1]}")
        
            if player_cards[-1] == 11:
                if not (sum_of_player_cards + 11 <= 21):
                    player_cards[-1] = 1
    
            sum_of_player_cards += player_cards[-1]
            print(f"Your cards are {player_cards},  Your cards sum = {sum_of_player_cards}")
            
        if pickNextCard == "y":
            if sum_of_dealer_cards <= 16:
                dealer_cards.append(random.choice(cards))
                
                if dealer_cards[-1] == 11:
                    if not (sum_of_dealer_cards + 11 <= 21):
                        dealer_cards[-1] = 1
                        
                sum_of_dealer_cards += dealer_cards[-1]
                
        if pickNextCard == "y" and sum_of_player_cards < 21:
            pickNextCard = "y"
        else:
            pickNextCard = "n"
            print(f"Dealer cards sum = {sum_of_dealer_cards}")
    
        
    if sum_of_player_cards > 21:
        print("You lose!")
        
    elif sum_of_dealer_cards == sum_of_player_cards:
        print("Match draw!")
    
    elif sum_of_dealer_cards > 21:
        print("You win!")
    
    elif sum_of_player_cards > sum_of_dealer_cards:
        print("You win!")
    
    else:
        print("You lose!")    