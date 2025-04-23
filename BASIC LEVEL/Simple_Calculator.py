# Function to perform basic arithmetic operations
def Simple_Calculator():
    # Taking two numbers from the user
    num1 = int(input("Enter the first Number : "))
    num2 = int(input("Enter the second Number : "))

    # Defining functions for each arithmetic operation
    def addition(num1, num2):
        result = num1 + num2
        return f'Sum of {num1} and {num2} is {result}'

    def Subtraction(num1, num2):
        result = num1 - num2
        return f'Difference of {num1} and {num2} is {result}'

    def Multiplication(num1, num2):
        result = num1 * num2
        return f'Difference of {num1} and {num2} is {result}'  # (Note: message says "Difference" but it's multiplication)

    def Division(num1, num2):
        # Checking to avoid division by zero
        if num2 != 0:
            result = num1 / num2
            return f'The value of {num1} / {num2} is {result}'
        else:
            return "Undefined"  # Cannot divide by zero

    # This flag keeps the loop running until the user enters a valid option
    conditon = True

    # Loop to let the user choose an operation
    while conditon:
        # Ask the user to select an operation
        Operator = int(input(
            "1) Enter 1 to perform Addition\n"
            "2) Enter 2 to perform Subtraction\n"
            "3) Enter 3 to perform Multiplication\n"
            "4) Enter 4 to perform Division : "
        ))

        # Check if the selected option is valid (between 1 and 4)
        if Operator >= 1 and Operator <= 4:
            conditon = False  # Exit the loop after valid input

            # Perform the selected operation
            if Operator == 1:
                print(addition(num1, num2))
            elif Operator == 2:
                print(Subtraction(num1, num2))
            elif Operator == 3:
                print(Multiplication(num1, num2))
            elif Operator == 4:
                print(Division(num1, num2))
        else:
            # Prompt user to enter a valid option again
            print("Enter valid option")

# Call the calculator function
Simple_Calculator()
