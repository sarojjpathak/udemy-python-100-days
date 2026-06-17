# in this project we generate a password of two version or level one is easy another is hard
#easy level 
import random
print("WELCOME TO PASSWORD GENERATOR SYSTEM")
print("-"*80)
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '+', '=', '{', '}', '[', ']', '|',
           '\\', ':', ';', '"', "'", '<', '>', ',', '.',
           '?', '/']
letters_number = int(input("How many letters do you want in your password"))
numbers_number = int(input("How many number do you want in your password"))
symbols_number = int(input("How many symbols do you want in your password"))

simple_password = ""
for i in range(0,letters_number):
    simple_password += random.choice(letters)
for i in range(0,symbols_number):
    simple_password += random.choice(symbols)
for i in range(0,numbers_number):
    simple_password += random.choice(numbers)
print(f"basic password suggested : {simple_password}")

#know i try a very hard logic to implement where i ask user how many letter symbol and number they want and i select random characters from list  and randomly distribute those characters   
#main function used is random.sample() which select random  unique character from list and make a new list

l_list = random.sample(letters,letters_number)
n_list = random.sample(numbers,numbers_number)
s_list = random.sample(symbols,symbols_number)

pass_characters = []
pass_characters.extend(l_list)
pass_characters.extend(n_list)
pass_characters.extend(s_list)
strong_password = random.sample(pass_characters,len(pass_characters))
password = ""
for char in strong_password:
    password +=  char
print(f"Strong password suggested : {password}")