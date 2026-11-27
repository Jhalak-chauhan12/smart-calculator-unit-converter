
# Calculator and Unit Converter Project

# Display Menu
def show_menu():
    print("\n===== CALCULATOR & UNIT CONVERTER =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Kilometers to Miles")
    print("6. Celsius to Fahrenheit")
    print("7. Quit")


# Get Valid Number
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


# Arithmetic Functions
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b


# Unit Conversion Functions
def km_to_miles(km):
    return km * 0.621371


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Main Program
while True:
    show_menu()

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        print("Result:", addition(a, b))

    elif choice == "2":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        print("Result:", subtraction(a, b))

    elif choice == "3":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        print("Result:", multiplication(a, b))

    elif choice == "4":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        print("Result:", division(a, b))

    elif choice == "5":
        km = get_number("Enter kilometers: ")
        print("Miles:", km_to_miles(km))

    elif choice == "6":
        celsius = get_number("Enter Celsius: ")
        print("Fahrenheit:", celsius_to_fahrenheit(celsius))

    elif choice == "7":
        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice! Please select between 1 and 7.")

