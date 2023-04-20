#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

length_letters = len(letters)
lenght_symbols = len(symbols)
lenght_numbers = len(numbers)

password = ""
for letter in range(0,nr_letters):
  password += random.choice(letters)

for symbol in range(0,nr_symbols):
  password += random.choice(symbols)

for number in range(0,nr_numbers):
  password += random.choice(numbers)

print(f"Password in ordered: {password}")

password_random_ordered = list(password)
random.shuffle(password_random_ordered)
password_random_ordered = ''.join(password_random_ordered)
print(f"Password in random ordered: {password_random_ordered}")

# OR 
# Instead of join function we could have use for loop
# pwd = ""
# for char in password_random_ordered:
#   pwd += char

# print(pwd)