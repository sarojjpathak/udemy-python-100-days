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