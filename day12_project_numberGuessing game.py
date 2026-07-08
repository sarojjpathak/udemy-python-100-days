import random
from logo import day_12_logo as logo
HARD_LEVEL = 5
EASY_LEVEL = 10

def set_difficulties():
    level = input("Choose a difficulty Level (hard/easy)")
    if level == "hard":
        return HARD_LEVEL
    else:
        return EASY_LEVEL
    





print(logo)

print("_______WELCOME TO NUMBER GUESSING GAME_________")


attempt = set_difficulties()
number_to_guess = random.randint(1,100)
list_of_guess_num = []
# print(number_to_guess)
while attempt != 0:
    guessed_number = int(input("Guess a number from 1 t0 100 :"))
    if guessed_number in list_of_guess_num:
        print("you have already guessed this number try another number")
    else:
        list_of_guess_num.append(guessed_number)

        # print(list_of_guess_num)
        if guessed_number == number_to_guess:
            print("you have won this game")
            break
        elif guessed_number < number_to_guess:
            print("too low ")
            attempt -= 1
        elif guessed_number > number_to_guess:
            print("too high")
            attempt -= 1
        print(f"Attempt Available : {attempt}")
if attempt == 0:
    print("you loose this game")

    
