import random
print(''' 
___________                        _________                      __  .__    .__                 
\__    ___/__.__.______   ____    /   _____/ ____   _____   _____/  |_|  |__ |__| ____    ____   
  |    | <   |  |\____ \_/ __ \   \_____  \ /  _ \ /     \_/ __ \   __\  |  \|  |/    \  / ___\  
  |    |  \___  ||  |_> >  ___/   /        (  <_> )  Y Y  \  ___/|  | |   Y  \  |   |  \/ /_/  > 
  |____|  / ____||   __/ \___  > /_______  /\____/|__|_|  /\___  >__| |___|  /__|___|  /\___  /  
          \/     |__|        \/          \/             \/     \/          \/        \//_____/ 
      
        ''')

print("_______WELCOME TO NUMBER GUESSING GAME_________")

level = input("Choose a difficulty Level (hard/easy)")
if level == "hard":
    attempt = 5
else:
    attempt = 10
number_to_guess = random.randint(1,100)
print(number_to_guess)
while attempt != 0:
    guessed_number = int(input("Guess a number from 1 t0 100 :"))
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

    
