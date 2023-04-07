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

print("Welcome to Rock, Paper, Scissors Game!")
player_choice = int(input("What do you want to choose? 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))

computer_choice = random.randint(0,2)

if player_choice == 0:
  print(f"You choose\n\n{rock}")
elif player_choice == 1:
  print(f"You choose\n\n{paper}")
else:
  print(f"You choose\n\n{scissors}")

if computer_choice == 0:
  print(f"Computer choose\n\n{rock}")
elif computer_choice == 1:
  print(f"Computer choose\n\n{paper}")
else:
  print(f"Computer choose\n\n{scissors}")

if player_choice == 0:
  if computer_choice == 1:
    print("You lose")
  elif computer_choice == 2:
    print("You win")
  else:
    print("Match draw")

elif player_choice == 1:
  if computer_choice == 0:
    print("You win")
  elif computer_choice == 2:
    print("You lose")
  else:
    print("Match draw")

elif player_choice == 2:
  if computer_choice == 0:
    print("You lose")
  elif computer_choice == 1:
    print("You win")
  else:
    print("Match draw")

else:
  print("Select Correct choice")
  

