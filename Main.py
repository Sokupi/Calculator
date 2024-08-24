def add(x, y):  # Responsible for adding the values
    print(f"{x} + {y} = {x + y}")
    return x + y


def subtract(x, y):  # Responsible for subtracting the values
    print(f"{x} - {y} = {x - y}")
    return x - y


def multiply(x, y):  # Responsible for multiplying the values
    print(f"{x} * {y} = {x * y}")
    return x * y


def divide(x, y):  # Responsible for dividing the values
    if y != 0:  # Check if the divisor is zero
        print(f"{x} / {y} = {x / y}")
        return x / y
    else:
        print("Cannot divide by zero")
        return None


def get_user_input():  # Responsible for getting the user's input
    while True:
        print("\nCALCULATION")
        print("Pick your operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")  # Asks the user what operations it is using

        if choice == "5":  # If the user's wishes to exit, this returns no values at all
            print("Exiting...")
            return choice, None, None

        try:
            num1 = float(input("Enter your first number: "))  # Asks the first number
            num2 = float(input("Enter your second number: "))  # Asks the second number
            return choice, num1, num2
        except ValueError:  # Make sures that the user can only input numbers
            print("Invalid input. Please enter numbers only.")


def calculation(choice, num1, num2):  # This does the calculations base on the user's choice
    if choice == "1":
        return add(num1, num2)
    elif choice == "2":
        return subtract(num1, num2)
    elif choice == "3":
        return multiply(num1, num2)
    elif choice == "4":
        return divide(num1, num2)


def main():
    while True:
        choice, num1, num2 = get_user_input()
        if choice == "5":  # Exits the whole program when the user chooses "5"
            break
        result = calculation(choice, num1, num2)
        if result is not None:  # This prints out the result when the user didn't choose "5"
            print(f"Result: {result}")


if __name__ == "__main__":
    main()
