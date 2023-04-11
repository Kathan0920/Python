import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for i in range(len(chosen_word)):
    display += '_'


lives = 6
correct_guess = False
Blank_remaining = display.count('_')


while Blank_remaining > 0:
    user_guess = input("\nGuess a letter: ").lower()

    correct_guess = False
    for i in range(len(chosen_word)):
        if user_guess == chosen_word[i]:
            display[i] = chosen_word[i]
            correct_guess = True
            
    
    if not correct_guess:
        lives -= 1
    Blank_remaining = display.count('_')
    
    print(f"{' '.join(display)}")


    if "_" not in display:
        print("\nYou win!")

    if lives == 0:
        print("\nYou lose!")
        break
    