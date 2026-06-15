# qn1   : BMI Calculator
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the person's height squared.
height = 1.65 
weight = 84


# Calculate the bmi using weight and height.
bmi = weight / height ** 2

print(bmi)
# round(number , ndigitafterdecimal how much we want to round after decimal 1, 2 ,3 4,)
print(type(round(bmi)))  #this will return integer 31
print(type(round(bmi,0))) # this will return float 31.0
print(type(round(bmi,1))) # this will return a float value 30.9





#final project  of say 2 TIP CALCULATOR and bill amount

print("WELCOME TO THE TIP CALCULATOR")
total_bill = int(input("what is the total bill amount ? $"))
tip = int(input("Do you want to give some tip? in percentage"))
people = int(input("How many people are going to pay the total bill amount"))
per_person = (total_bill + tip / 100 * total_bill)/people

print(f"Each person should pay  ${ round(per_person,2) }  ")