# Global variable
message = "I am a global variable"

def show_global():
    # Accessing a global variable
    print("Inside show_global():", message)

def local_scope():
    # Local variable
    message = "I am a local variable"
    print("Inside local_scope():", message)

def change_global():
    global message
    message = "Global variable has been changed!"
    print("Inside change_global():", message)

# Main Program
print("Before function call:", message)

show_global()      # Uses global variable
local_scope()      # Uses local variable
print("After local_scope():", message)  # Global variable remains unchanged

change_global()    # Modifies global variable using 'global'
print("After change_global():", message)


#trying to build simple project
school_name = "ABC School"

def show_school():
    print("School:", school_name)

def student_details():
    student = input("Enter student name: ")
    grade = input("Enter grade: ")
    print("Student:", student)
    print("Grade:", grade)

def change_school():
    global school_name
    school_name = input("Enter new school name: ")
    print("School updated to:", school_name)

print("Welcome to Student Record System")
print("Current School:", school_name)

show_school()
student_details()

print("School after student entry:", school_name)

change_school()

print("Final School Name:", school_name)


#library mgmt system
library_name = "City Library"

def show_library():
    print("Library:", library_name)

def borrow_book():
    book = input("Enter book name: ")
    member = input("Enter member name: ")
    print(member, "borrowed", book)

def change_library():
    global library_name
    library_name = input("Enter new library name: ")
    print("Library name updated to:", library_name)

print("Welcome to the Library System")
print("Current Library:", library_name)

show_library()

borrow_book()

print("Library Name:", library_name)

change_library()

print("Final Library Name:", library_name)