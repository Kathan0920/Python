from game_data import data
import random
import click

def clrscr():
    click.clear()

            
player_score = 0

# Displaying first person details
A = random.choice(data)
player_answer = True
print(f"Compare A: {A['name']}, a {A['description']} , from {A['country']}")
A_followers = A['follower_count']

