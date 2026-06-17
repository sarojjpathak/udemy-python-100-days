number = [33,44,55,66,77,44,33,44]
print("even number from list ")
for n in number:
    if(n % 2 == 0):
        print(n)
print("sum of number in list  using sum function")
print(sum(number))
# to find max number in a list there is a max() function
print(max(number))
#finding max using for loop
max =0
for n in number:
    if(n>max):
        max = n

print(f"max value finding using for loop not max function = {max}")



#range function
for n in range(1,100):
    print(n)#this will print from 1 to 99
#lets see the value in list using range function 
for n in range(0,len(number)):
    print(number[n])

# practice project
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
li = []
for n in range(1,101):
    if(n%5 == 0 and n%3 == 0):
        li.append("FizzBuzz")
        
    elif(n%5 == 0):
         li.append("Buzz")
    elif(n%3 == 0):
        li.append("Fizz")
    else:
        li.append(n)
print(li)


# random.sample(list,numberof element you want in a new list) it will return a list with lenght given  in second parameter and  and the elem are selected in random


#random.shuffel(list) it will shuffel the position of list in random order in existing list