import random
from logo import day_14_vs,day_14_logo 
from instagramdata import data
score = 0
# print(data)
# print(day_14_vs)

#  {
#         'name': 'Instagram',
#         'follower_count': 685,
#         'description': 'Social media platform',
#         'country': 'United States'
#     }
def format(account):
    return f"{account["name"]}, a {account["description"]}, from {account["country"]}"

def score_count(status):
    global score
    if status == "win":
        
        score += 1
    elif status == "loose" :
        score += 0

def random_account_selection(one_select = False):#if user is correct then true is pass to select random account as if he/she wins we need one account to compare
   
   if one_select == False:
       two_random_accounts = random.choices(data,k=2)
       return two_random_accounts
   elif one_select == True:
       one_random_account = random.choice(data)
       return one_random_account
def dispay(dict1,dict2 = None,result = None):
    if result == None:
        print("\n\n______________________________________________________________________________________")
        print(f"Account A : {format(dict1)}")
        print("______________________________________________________________________________________\n\n")
        if dict2 != None:
            print(day_14_vs)
            print("\n\n______________________________________________________________________________________")
            print(f"Account B :{format(dict2)}")
            print("______________________________________________________________________________________\n\n")
    elif result == "show":
             print("\n\n___________________________________________")
             print(f"Your Choice :{dict1["name"]} \nFollower Count : {dict1["follower_count"]}")
             
             print("_______________________________________________")
             print(f"Not Your Choice :{dict2["name"]} \nFollower Count : {dict2["follower_count"]}")
             print("______________________________________________\n")



def main():
    print(day_14_logo)   #display the art
    # print(random_account_selection())
    # print(random_account_selection(True))
    A = random_account_selection(one_select = True)
    while True:
        print(f"Your  score is {score}")
        B = random_account_selection(one_select = True)
        while A == B:
            
                B = random_account_selection(True)

        dispay(A,B)
        computer_choice = ''
        user_choice = input("Guess which account has more followers A or B  : ")
        if  user_choice == 'A':
            user_choice = A
            computer_choice = B
        else:
            user_choice = B
            computer_choice = A
        
        # print(f"userchoice = {user_choice} \n computerchoice = {computer_choice}")
        if user_choice["follower_count"] > computer_choice["follower_count"]:
            print("YOU ARE CORRECT")
            dispay(A,B,result="show")
            status = "win"
            A = user_choice
            
            score_count(status=status)
        else:
            print("YOU LOOSE")
            dispay(A,B,result="show")
            status = "loose"
            score_count(status=status)
            break
            

            
        print(f"you score is : {score}")
newGame = True
while newGame:
    main()
    print("----------game over----------")
    newGame = input("Do you want to start the new game (y/n)")
    if newGame == "y":
        newGame = True
    else:
        newGame = False

