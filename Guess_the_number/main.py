from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I\'m thinking of a number between 1 and 100 ")
actual_number = random.randint(1,100)
difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard'. ").lower()

def GuessTheNumber(difficulty_level):
    
    if difficulty_level == "easy":
        attempts_remaining = 10
        
    elif difficulty_level == "hard":
        attempts_remaining = 5
        
    while attempts_remaining > 0:
        print(f"You have {attempts_remaining} attempts remaining to guess a number.")
        number_guessed = int(input("Guess a number. "))

        if number_guessed == actual_number:
            print(f"You got it. The actual number was {actual_number}")
            break
            
        if attempts_remaining > 1:
            if number_guessed < actual_number:
                print("Too low.")
                      
            elif number_guessed > actual_number:
                print("Too high.")
                
            print("Guess again.")
        attempts_remaining -= 1  
        
    if attempts_remaining == 0:
        print("You run out of attempts. Better luck next time!")

GuessTheNumber(difficulty_level)