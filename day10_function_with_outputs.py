#leap year 
# a year is leap year if it is divisible by 4 
# not divisible by 100 unless it is divisible by 400


def is_leap_year(year):
    """This is return boolean value whether the 
       input year is leap year or not"""
    # Write your code here.
    count = 0
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                return True
            else:
                return False
    else:
        return False
        
    
    # Don't change the function name.
print(f" 2100 is a leap year : {is_leap_year(2100)}")
print(f" 2000 is a leap year : {is_leap_year(2000)}")


def greet(time=1):
    if time < 12:
        print("good morning")
    else:
        print("good afternoon")
greet(13)
greet()