# Function for Division
def divide(num1, num2):
    if num2 == 0:
        print("Error: Denominator must not be zero.")
        return None
    return num1 / num2

# Function for Exponentiation
def exponentiation(base, exponent):
    return base ** exponent

# Function for Remainder
def remainder(num1, num2):
    if num2 == 0:
        print("Error: Denominator must not be zero.")
        return None
    return num1 % num2

# Function for Summation
def summation(start, end):
    if start > end:
        print("Error: The second number must be greater than the first number.")
        return None
    return sum(range(start, end + 1))

# Menu-driven program
def main_menu():
    while True:
        print("\nMathematical Operations Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")

        choice = input("Enter your choice: ").upper()

        if choice == 'D':
            num1 = float(input("Enter the numerator: "))
            num2 = float(input("Enter the denominator: "))
            result = divide(num1, num2)
            if result is not None:
                print(f"Result: {result}")
        elif choice == 'E':
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            print(f"Result: {exponentiation(base, exponent)}")
        elif choice == 'R':
            num1 = float(input("Enter the numerator: "))
            num2 = float(input("Enter the denominator: "))
            result = remainder(num1, num2)
            if result is not None:
                print(f"Result: {result}")
        elif choice == 'F':
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            result = summation(start, end)
            if result is not None:
                print(f"Summation Result: {result}")
        elif choice == 'Q':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
main_menu()
