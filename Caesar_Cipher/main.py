from art import logo

alphabet = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar(entered_text, shift_no, user_choice):
    converted_text = ""
    if user_choice == "decode":
        shift_no = -shift_no
    for character in entered_text:
        if character not in alphabet:
            converted_text += character
        else:
            position = alphabet.index(character)
            new_position = (position + shift_no) % 26
            converted_text += alphabet[new_position]

    print(f"The {user_choice}d message is {converted_text}")

print(logo)

user_ans = "yes"
while user_ans == "yes":
    
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(entered_text=text, shift_no=shift, user_choice=direction)

    user_ans = input("\nType 'yes' if you want to do this again. Otherwise type 'no'. \n").lower()
    if user_ans == "no":
        print("Hope you enjoyed it!. Bye bye.")


