alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(entered_text, shift_no, user_choice):
    converted_text = ""
    if user_choice == "decode":
        shift_no = -shift_no
    for i in range(0, len(entered_text)):
        position = alphabet.index(entered_text[i])
        new_position = (position + shift_no) % 26
        converted_text += alphabet[new_position]
    print(f"The {user_choice}d message is {converted_text}")

caesar(entered_text=text, shift_no=shift, user_choice=direction)
