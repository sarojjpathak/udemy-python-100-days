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
def dispay(dict1,dict2 = None):
    print("\n\n______________________________________________________________________________________")
    print(f"Account A :{dict1["name"]}, a {dict1["description"]}, from {dict1["country"]}")
    print("______________________________________________________________________________________\n\n")
    if dict2 != None:
        print(day_14_vs)
        print("\n\n______________________________________________________________________________________")
        print(f"Account B :{dict2["name"]}, a {dict2["description"]}, from {dict2["country"]}")
        print("______________________________________________________________________________________\n\n")


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
            status = "win"
            A = user_choice
            
            score_count(status=status)
        else:
            print("YOU LOOSE")
            status = "loose"
            score_count(status=status)
            break
            

            
        print(f"you score is : {score}")




    





#select random account 2 or 1 depends on the status is win or loose


#decorate or display in format



#input from user guess the follower a or b



#result or test score


main()
print("game over")

