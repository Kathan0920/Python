import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for i in range(len(chosen_word)):
    display += '_'


print(''.join(display))
print("\n")

Blank_remaining = display.count('_')

while Blank_remaining > 0:
    user_guess = input("Guess a letter: ").lower()
    
    for i in range(len(chosen_word)):
        if user_guess == chosen_word[i]:
            display[i] = chosen_word[i] 
            
    Blank_remaining = display.count('_')


print(''.join(display))
print("You won")

# You can also do like:
# end_of_game = False
# while not end_of_game:
#     user_guess = input("Guess a letter: ").lower()
#    
#     for i in range(len(chosen_word)):
#         if user_guess == chosen_word[i]:
#             display[i] = chosen_word[i]
#     
#     print(''.join(display)) 
#     if "_" not in display:
#         end_of_game = True
#          print("You won")

