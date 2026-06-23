# Love Calculator
# 💪 This is a difficult challenge! 💪 

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out. 
# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"
# T occurs 0 times 
# R occurs 1 time 
# U occurs 2 times 
# E occurs 2 times 
# Total = 5 
# L occurs 1 time 
# O occurs 0 times 
# V occurs 0 times 
# E occurs 2 times 
# Total = 3 
# Love Score = 53
# Example Input 
# calculate_love_score("Kanye West", "Kim Kardashian")
# Example Output
# 42

def calculate_love_score(boy_name,girl_name):
 count_true = 0
 count_love = 0
 name_list = [boy_name,girl_name]
 letter_to_check = [["t","r","u","e"],["l","o","v","e"]]
 for i in range(0,2):
    
    for letter in name_list[i]:
        print(letter)
        if letter == letter_to_check[0][0]:
            count_true += 1
        elif letter == letter_to_check[0][1]:
         count_true += 1
        elif letter == letter_to_check[0][2]:
         count_true += 1
        elif letter == letter_to_check[0][3]:
         count_true += 1

        if letter == letter_to_check[1][0]:
            count_love += 1
        elif letter == letter_to_check[1][1]:
         count_love += 1
        elif letter == letter_to_check[1][2]:
         count_love += 1
        elif letter == letter_to_check[1][3]:
         count_love += 1
        
 print(f" YOUR LOVE SCORE IS {count_true*10+count_love}")
calculate_love_score("true","lover")
calculate_love_score("Kanye West", "Kim Kardashian")

