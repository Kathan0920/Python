import random
#This computer based game, in which computer while play rock, paper, scissor with you.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper,scissors]
print("Welcome to Rock, Paper, Scissors Game!")
player_choice = int(input("What do you want to choose? 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
print(f"You choose\n\n{game_images[player_choice]}")

computer_choice = random.randint(0,2)
print(f"Computer choose\n\n{game_images[computer_choice]}")


if player_choice >= 3 or player_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif player_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and player_choice == 2:
  print("You lose")
elif computer_choice > player_choice:
  print("You lose")
elif player_choice > computer_choice:
  print("You win!")
elif computer_choice == player_choice:
  print("It's a draw")

