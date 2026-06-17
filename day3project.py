# pizza billing system
# in this we take a input from customer about pizza size {s ,m ,l} ask if they want extra paepperoni y/n and ask if they want extra cheese 

pizza_size = input("what size do you want Small ,Large or medium :")
pepperoni = input("do you want extra pepperoni y/n :")

cheese = input("do you want extra cheese y/n :")

if(pizza_size == "small"):
    print("you want small size pizza")
    bill = 20
elif(pizza_size == "large"):
     print("you want large size pizza")
     bill = 35
else:
      print("you want middle level size piazza")
      bill = 27


if(pepperoni == "y"):
     bill += 5
if(cheese == "y"):
     bill += 6




print(f"final amount to pay is $ {bill}")



#project of day 3 project hunt challenge
print("WELCOME TO TREASURE HUNT CHALLENGE")



restart = "y"
while restart == "y":
 print("\n\n\n\n\nlETS GO !!!!!!!!!!!!!\n\n\n")
 first_move = input("you want to move left , right  ")
 status = "continue"
 if(first_move == "left"):
     status = "continue"
     print("\n-------You are on the right track-----\n\n\n\n\n")
 else:
     print("--------THATS THE WRONG CHOICE MY FRIEND-------\n\n")
     status = "game_over"
     print(f"|------{status}----|")
    
 if(status == "continue"):
     second_move = input(" |  DO you want to swim or run    |")
     if(second_move == "run"):
          status == status
          print("\n------wow you are very close to treasure------")
          
     else:
           print("--------THATS THE WRONG CHOICE MY FRIEND-------\n\n")
           status = "game_over"
           print(f"|------{status}----|")
           

 if(status == "continue"):
     treasure_box = input("which box do you want red yellow black")
     if(treasure_box == "yellow"):
          print("\n-----Congrats you found a treasure-----")
          
     elif(treasure_box == "red"):
          print("ohhh you are dead there is a lave in the box")
          print("game over")
          
     else:
          print("ohhh you are dead there is a lave in the box")
          print("game over")
          
 restart = input("DO you want to restart the game y/n")
print("THANK YOU")