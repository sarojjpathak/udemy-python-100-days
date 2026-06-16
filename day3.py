#if else statement  and using a modulo operator
# a = 32

# if(a % 2 == 0):
#     print(f"{a} is a even number")
# else:
#     print(f"{a} is a odd number")

#BMI Calculator with Interpretations
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"

# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)
# if(bmi < 18.5):
#     print("underweight")
# elif(bmi >= 18.5 and bmi <25):
#     print("normal weight")
# else:
#     print("overweight")

restart = "y"

print("WELCOME TO TREASURE HUNT CHALLENGE")

while restart == "y":

    status = "continue"

    first_move = input("Do you want to move left or right? ")

    if first_move == "left":
        print("\n-------You are on the right track-----\n")
    else:
        print("--------THAT'S THE WRONG CHOICE MY FRIEND-------")
        status = "game_over"

    if status == "continue":
        second_move = input("Do you want to swim or run? ")

        if second_move == "run":
            print("\n------Wow! You are very close to the treasure------")
        else:
            print("--------THAT'S THE WRONG CHOICE MY FRIEND-------")
            status = "game_over"

    if status == "continue":
        treasure_box = input("Which box do you want? red, yellow, or black: ")

        if treasure_box == "yellow":
            print("\n-----Congrats! You found the treasure!-----")
        elif treasure_box == "red":
            print("\nOh no! There is lava in the box.")
            print("GAME OVER")
        else:
            print("\nOh no! There is lava in the box.")
            print("GAME OVER")

    print(f"\nCurrent Status: {status}")
    restart = input("\nDo you want to restart the game? (y/n): ").lower()