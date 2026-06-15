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
