#dictionaries normal syntax
dic = {
    "name":"saroj pathak",
    "age":21
}
for key in dic:   # this loop all the key in dic
    print(key)
for value in dic.values():  #this loop all the values in dic
    print(value)
for name,age in dic.items():  # this will loop all the key and vlaue in given dictionaries
    print(name +"," )
    print(age)

#from list or string count different letter occurance
string = "helloejjjdhe"
letter_count = {}
for letter in string:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
print(letter_count) 
dict = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4
        }
print("key : value")
for key,value in dict.items():
    print(f"{key} : {value}")
#to delete elem from dic
print(f"Before deleting c {dict}")
del dict["c"]

print(f"After deleting c {dict}")


#to use value inside the dict we canuse get function which is better then []
print(dict.get("b"))

#to delete all the elements in dict we can use clear function
dict.clear()
print(dict)#output is {}


#adding new key value
dict["newkey"] = "new value"
print(dict)


#problem 1
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores. 
# Write a program that converts their scores to grades.
# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values. 
# The final version of the student_grades dictionary will be checked. 
# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary. 
# This is the scoring criteria: 
# - Scores 91 - 100: Grade = "Outstanding" 
# - Scores 81 - 90: Grade = "Exceeds Expectations" 
# - Scores 71 - 80: Grade = "Acceptable" 
# - Scores 70 or lower: Grade = "Fail" 

def grading(score):
    if score > 90 and score <= 100:
        return "Outstanding"
    elif score > 80 and score <= 90:
        return "Exceeds Expectations"
    elif score > 70 and score <= 80:
        return "Acceptable"
    elif score <= 70:
        return "Fail"
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}
for key,value in student_scores.items():
    
    student_grades[key] = grading(value)  #using function makes block of code more reusable
print(student_grades)
