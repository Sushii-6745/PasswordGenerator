import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []
for nr in range(0,nr_letters):
    length = len(letters)
    random_gen = random.randint(0,(length-1))
    password.append(letters[random_gen])
for nr in range(0,nr_symbols):
    length = len(symbols)
    random_gen = random.randint(0,(length-1))
    password.append(symbols[random_gen])
for nr in range(0,nr_numbers):
    length = len(numbers)
    random_gen = random.randint(0,(length-1))
    password.append(numbers[random_gen])
counter = 0
for token in password:
    random_gen = random.randint(counter,len(password)-1)
    primary_token = password[counter]
    password[counter] = password[random_gen]
    password[random_gen] = primary_token
    counter += 1


password_string =""
for token in password:
    password_string+=token

print(password_string)



