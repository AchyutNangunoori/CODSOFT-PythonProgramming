def calculator():
    while True:
        print("\nSimple Calculator")
        print("Select an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        operation = input("Enter your choice (1/2/3/4/5): ")

        if operation == "5":
            print("Exiting the calculator. Goodbye!")
            break

        if operation not in ["1", "2", "3", "4"]:
            print("Invalid operation. Please try again.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if operation == "1":
                result = num1 + num2
                print(f"The result of addition is: {result}")
            elif operation == "2":
                result = num1 - num2
                print(f"The result of subtraction is: {result}")
            elif operation == "3":
                result = num1 * num2
                print(f"The result of multiplication is: {result}")
            elif operation == "4":
                if num2 == 0:
                    print("Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result of division is: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
