#making a scissor paper rock game
# ✊ Rock beats ✌️ Scissors
# ✌️ Scissors beats ✋ Paper
# ✋ Paper beats ✊ Rock
import random
#suppose 0 is rock 1 is paper 2 is scessor 
com_score = 0
user_score = 0
draw = 0
while True:
    user_choice = int(input("choose your option 0 for rock 1 for paper and 2 for scessor"))
    computer_choice = random.randint(0,2)
    if(user_choice == 0 ):
        if(computer_choice == 1):
            print("Your choice : ✊")
            print("Computer choice : ✋")
            print("you loose")
            status = "loose"
        if(computer_choice == 2):
            print("Your choice : ✊")
            print("Computer choice : ✌️")
            print("you win")
            status = "win"
        if(computer_choice == 0):
            print("Your choice : ✊")
            print("Computer choice : ✊")
            print("DRAW")
            status = "draw"
        
    elif(user_choice == 1 ):
        if(computer_choice == 1):
            print("Your choice : ✋")
            print("Computer choice : ✋")
            print("Draw")
            status = "draw"
        if(computer_choice == 2):
            print("Your choice : ✋")
            print("Computer choice : ✌️")
            print("you loose")
            status = "loose"
        if(computer_choice == 0):
            print("Your choice : ✋")
            print("Computer choice : ✊")
            print("you win")
            status = "win"
        
    else:
        if(computer_choice == 1):
            print("Your choice : ✌️")
            print("Computer choice : ✋")
            print("you win")
            status = "win"
        if(computer_choice == 2):
            print("Your choice : ✌️")
            print("Computer choice : ✌️")
            print("DRAW")
            status = "draw"
        if(computer_choice == 0):
            print("Your choice : ✌️")
            print("Computer choice : ✊")
            print("you Loose")
            status = "loose"
    if(status == "win"):
        user_score += 1
    elif(status == "loose"):
        com_score += 1
    else:
        draw += 1
    

    print(f'''  
        ________________________________   
        |    SCORE TABLE             
        |   win   = {user_score }    
        |   loose = {com_score}      
        |   draw =  {draw}           
        |________________________________



          ''')
       
