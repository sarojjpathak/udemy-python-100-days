def greet(para):
    print(f"NAMASTE {para}")
    print("HELLO")
    print("HOLA")
    
greet("saroj")#saroj is argument which is passedI was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.



# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
# **Warning** The function must be called life_in_weeks for the tests to pass. Also the output must have the same punctuation and spelling as the example. Including the full stop!
# Example Input
# 56
# Example Output
# You have 1768 weeks left.
def life_in_weeks(current_age):
    years_left = 90-current_age
    in_weeks = years_left * 52
    print(f"You have {in_weeks} weeks left.")

life_in_weeks(current_age =56)
# using current_age = 56 make code more readable
def sum(a,b,c):
    print(f''' 
        a = {a}
        b = {b}
        c = {c}
''')
    print(f"sum is {a+b+c}")
sum(1,2,3)#this is positional argument here first int is a second is b and then c 
sum(b=2,c=3,a=1) # keyword argument if we use keyword the position doesnot matter




