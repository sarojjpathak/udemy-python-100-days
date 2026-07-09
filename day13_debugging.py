"""
====================================================
ADVANCED PYTHON DEBUGGING EXAMPLE
====================================================

This program demonstrates:

1. print() debugging
2. assert statement
3. try-except
4. raise
5. breakpoint()
6. Function debugging
7. Loop debugging
8. Variable scope
9. Reading exception information
10. Logging program flow

Run this program and read the comments carefully.
"""

# -------------------------------
# GLOBAL VARIABLE
# -------------------------------
# Global variables can be accessed anywhere unless
# a local variable with the same name exists.
tax = 0.13


# -------------------------------
# FUNCTION
# -------------------------------
def calculate_total(price, quantity):
    """
    Calculates total amount after adding tax.

    Debugging Tip:
    Always print or inspect the values received
    by the function before performing calculations.
    """

    # Debug Print
    print("\n========== calculate_total() ==========")
    print(f"Received price = {price}")
    print(f"Received quantity = {quantity}")

    # ---------------------------------
    # ASSERT
    # ---------------------------------
    # Assert is mainly used while developing.
    # If the condition becomes False,
    # Python immediately stops the program.
    assert price >= 0, "Price cannot be negative"

    # ---------------------------------
    # MANUAL VALIDATION
    # ---------------------------------
    # Instead of letting Python fail somewhere later,
    # raise your own exception with a meaningful message.
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    subtotal = price * quantity

    print(f"Subtotal = {subtotal}")

    total = subtotal + subtotal * tax

    print(f"Tax = {tax}")
    print(f"Total = {total}")

    return total


# -------------------------------
# LOOP DEBUGGING
# -------------------------------
def display_cart(cart):
    print("\n========== DISPLAY CART ==========")

    # enumerate() gives index and value together.
    # Very useful while debugging loops.
    for index, item in enumerate(cart):

        print("----------------------")
        print(f"Current Index : {index}")
        print(f"Current Item  : {item}")


# -------------------------------
# VARIABLE SCOPE
# -------------------------------
def scope_example():

    # Local variable
    tax = 0.15

    print("\n========== SCOPE ==========")
    print("Local tax :", tax)


# -------------------------------
# MAIN PROGRAM
# -------------------------------
def main():

    print("Starting Program...")

    cart = ["Laptop", "Mouse", "Keyboard"]

    display_cart(cart)

    # ---------------------------------
    # BREAKPOINT
    # ---------------------------------
    # Uncomment the next line while debugging.
    #
    # The program will pause here.
    #
    # Commands inside debugger:
    #
    # p cart
    # p tax
    # n
    # c
    #
    # breakpoint()
    # ---------------------------------

    try:

        # User Input
        price = float(input("\nEnter product price : "))
        quantity = int(input("Enter quantity : "))

        print("\nInputs accepted successfully.")

        # Function Call
        total = calculate_total(price, quantity)

        print("\nFinal Bill =", total)

    except AssertionError as error:
        # Handles assert failures
        print("\nAssertionError Found")
        print(error)

    except ValueError as error:
        # Handles invalid values
        print("\nValueError Found")
        print(error)

    except Exception as error:
        # Handles any unexpected error
        print("\nUnexpected Error")
        print(type(error))
        print(error)

    finally:
        # finally always executes whether
        # an error occurs or not.
        print("\nCleaning Resources...")
        print("Program Finished")


# -------------------------------
# SCOPE DEMONSTRATION
# -------------------------------
scope_example()

# Notice:
# Inside the function tax = 0.15
# Outside the function tax = 0.13

print("\nGlobal tax :", tax)


# -------------------------------
# PROGRAM STARTS HERE
# -------------------------------
main()