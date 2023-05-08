############## The Blackjack game ###############

import random
from art import logo
import click

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clrscr():
    click.clear()

def check_Blackjack_for_player(sum_of_player_cards):
    if sum_of_player_cards == 21:
        return 1
    else:
        return 0

def check_Blackjack_for_dealer(sum_of_dealer_cards):
    if sum_of_dealer_cards == 21:
        return 1
    else:
        return 0
    
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
        if player_cards[-1] == 11:
            if not (sum_of_player_cards + 11 <= 21):
                player_cards[-1] = 1
        sum_of_player_cards += player_cards[i]
    
    print(
        f"Your cards = {player_cards} ,  Your score = {sum_of_player_cards}"
    )
    
    for i in range(0, 2):
        dealer_cards.append(random.choice(cards))
        if dealer_cards[-1] == 11:
            if not (sum_of_dealer_cards + 11 <= 21):
                dealer_cards[-1] = 1
        sum_of_dealer_cards += dealer_cards[i]
        
    print(f"Dealer's one card is {dealer_cards[0]}\n")
       
    pickNextCard = "y"

    if check_Blackjack_for_player(sum_of_player_cards):
        print(f"Dealer cards = {dealer_cards}, Dealer's score = {sum_of_dealer_cards}")
        print("Blackjack occured for you, You win!")
        pickNextCard = "n"
        
    elif check_Blackjack_for_dealer(sum_of_dealer_cards):
        print(f"Dealer cards = {dealer_cards}, Dealer's score = {sum_of_dealer_cards}")
        print("Blackjack occured for dealer, You lose!")  
        pickNextCard = "n"

    if pickNextCard == "y":
        while pickNextCard == "y":
        
            pickNextCard = input("Type 'y' to pick a next card. Otherwise type 'n' to pass. ").lower()
            
            if pickNextCard == "y":
                player_cards.append(random.choice(cards))
                print(f"Your next card is {player_cards[-1]}")
            
                if player_cards[-1] == 11:
                    if not (sum_of_player_cards + 11 <= 21):
                        player_cards[-1] = 1
        
                sum_of_player_cards += player_cards[-1]
                print(f"Your cards are {player_cards},  Your score = {sum_of_player_cards}")
                                
            if pickNextCard == "y" and sum_of_player_cards < 21:
                pickNextCard = "y"
                
            else:
                pickNextCard = "n"
                
                
        while sum_of_dealer_cards <= 16 and sum_of_player_cards <21:
            dealer_cards.append(random.choice(cards))
                    
            if dealer_cards[-1] == 11:
                if not (sum_of_dealer_cards + 11 <= 21):
                    dealer_cards[-1] = 1
                            
            sum_of_dealer_cards += dealer_cards[-1]
                    
        print(f"Dealer cards = {dealer_cards}, Dealer's score = {sum_of_dealer_cards}")  
                 
        if sum_of_dealer_cards == sum_of_player_cards:
            print("Match draw")
        
        elif sum_of_player_cards > 21:
            print("You lose")
            
        elif sum_of_dealer_cards > 21:
            print("You win")
        
        elif sum_of_player_cards > sum_of_dealer_cards:
            print("You win")
        
        else:
            print("You lose") 