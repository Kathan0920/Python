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

underscore = "_"
b = True

while b == True:
    user_guess = input("Guess a letter: ").lower()
    b = False
    
    for i in range(len(chosen_word)):
        if user_guess == chosen_word[i]:
            display[i] = chosen_word[i]           
    for j in range(len(display)):
        if underscore == display[j]:
            b = True

print(''.join(display))
print("You won")
