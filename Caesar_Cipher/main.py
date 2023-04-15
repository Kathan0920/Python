alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypts(original_text,shift_no):
    cipher_text = ""
    for i in range(0,len(original_text)):
        position = alphabet.index(original_text[i])
        new_position = (position + shift_no) % 26
        cipher_text += alphabet[new_position]
    print(f"The encoded message is {cipher_text}")
    
encrypts(original_text = text, shift_no = shift)
