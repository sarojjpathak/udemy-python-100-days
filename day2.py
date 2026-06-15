#subscripting
print("hello world"[2])
nums = [0, 1, 2, 3, 4, 5]

print(nums[1:4])   # [1, 2, 3]
print(nums[:3])    # [0, 1, 2]
print(nums[::2])   # [0, 2, 4]
print(nums[::-1])  # reversed list

print(2_34_999)
#this is for better visualization of large number the python compiler will display it as  a number integer
print(2_22_253.95)
print(True)
#to find the datatype we use this type function 
print(type(2_4_5_455))
print(type("hello"))
print(type(3_3.12))


# name = input("What is your name buddy  ?")
# length = len(name)
# #to concate name and length we have to convert lenght into string
# print("Lenght of "+ name + " is "+str(length))

print (type(6/3))
print(34/3)
a =print(33//3)
#here a will assign with the walue none as print return none

print (a);
#output none 
#pemdas
# PYTHON OPERATOR PRECEDENCE (Highest to Lowest)

# 1. ()                          Parentheses
# 2. **                          Exponentiation
# 3. +x, -x, ~x                  Unary operators
# 4. *, /, //, %                 Multiplication, Division, Floor Division, Modulus  
# 5. +, -                        Addition, Subtraction
# 6. <<, >>                      Bitwise Shift
# 7. &                           Bitwise AND
# 8. ^                           Bitwise XOR
# 9. |                           Bitwise OR
# 10. <, <=, >, >=, ==, !=       Comparisons
# 11. not                        Logical NOT
# 12. and                        Logical AND
# 13. or                         Logical OR
# 14. if ... else                Conditional Expression
# 15. lambda                     Lambda Expression
# 16. :=                         Walrus Operator

# ASSOCIATIVITY

# Left to Right:
# +, -, *, /, //, %, <<, >>, &, ^, |

# Example:
# 10 - 5 - 2
# = (10 - 5) - 2
# = 3

# Right to Left:
# **

# Example:
# 2 ** 3 ** 2
# = 2 ** (3 ** 2)
# = 2 ** 9
# = 512

# Examples of Precedence:

# 3 + 4 * 5
# = 3 + (4 * 5)
# = 23

# 2 + 3 ** 2 * 4
# = 2 + (9 * 4)
# = 38

# not True or False
# = (not True) or False
# = False

# Tip:
# When in doubt, use parentheses () to make the order clear.




#f-strings (formatted string literals) are used to insert variables or expressions directly inside a string.

a= 20
b = 30
print(f"the sum of {a} and {b} is {a+b}")
#using fstring we dont have to use + everywhere and we sont have to convert integer to string  to concat
