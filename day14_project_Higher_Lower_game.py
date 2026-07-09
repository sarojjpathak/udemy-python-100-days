import random
from logo import day_14_vs,day_14_logo 
from instagramdata import data
# print(data)
# print(day_14_vs)

#  {
#         'name': 'Instagram',
#         'follower_count': 685,
#         'description': 'Social media platform',
#         'country': 'United States'
#     }

def random_account_selection(status = False):#if user is correct then true is pass to select random account as if he/she wins we need one account to compare
   
   if status == False:
       two_random_accounts = random.choices(data,k=2)
       return two_random_accounts
   elif status == True:
       one_random_account = random.choice(data)
       return one_random_account
def dispay(dict1,dict2):
    
    print(f"Account A :{dict1["name"]}, a {dict1["description"]}, from {dict1["country"]}")
    print(day_14_vs)
    print(f"Account B :{dict2["name"]}, a {dict2["description"]}, from {dict2["country"]}")



def main():
    print(day_14_logo)   #display the art
    # print(random_account_selection())
    # print(random_account_selection(True))
    dispay(random_account_selection(True),random_account_selection(True))





#select random account 2 or 1 depends on the status is win or loose


#decorate or display in format



#input from user guess the follower a or b



#result or test score


main()

