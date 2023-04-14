import random
from hangman_words import word_list
import hangman_art

chosen_word = random.choice(word_list)
lives = 6

print(hangman_art.logo)

display = []
for i in range(len(chosen_word)):
    display += '_'

correct_guess = False
Blank_remaining = display.count('_')

while Blank_remaining > 0:
    user_guess = input("\nGuess a letter: ").lower()
    correct_guess = False

    if user_guess in display:
        print(f"You have already guessed '{user_guess}'")
    
    for i in range(len(chosen_word)):
        if user_guess == chosen_word[i]:
            display[i] = chosen_word[i]
            correct_guess = True

    if not correct_guess:
        lives -= 1
    Blank_remaining = display.count('_')

    if user_guess not in chosen_word:
        print(f"letter {user_guess} is not in the word. You lose a life.")
        
    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])

    if "_" not in display:
        print("\nYou win!")

    if lives == 0:
        print("\nYou lose!")
        print(f"The correct word is {chosen_word}")
        break

