def calculate(num1, operator, num2):
    """Perform a calculation based on the given operator."""
    
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "%": lambda a, b: a % b
    }

    if operator not in operations:
        raise ValueError("Invalid operator")

    return operations[operator](num1, num2)


def main():
    """Run the calculator program."""

    while True:
        result = float(input("Enter first number: "))

        while True:
            operator = input("Enter operator (+, -, *, /, %): ")
            number = float(input("Enter next number: "))

            result = calculate(result, operator, number)
            print(f"Result: {result}")

            if input("Continue calculation? (y/n): ").lower() != "y":
                break

        if input("Start a new calculation? (y/n): ").lower() != "y":
            print("Goodbye!")
            break


main()