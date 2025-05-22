# This programm acts as a simple calculator that performs basic arithmetic operations on two numbers based on user input

def simple_calculator():
    #This functin takes two numbers and an operator as input from the user and performs the corresponding arithmetic operation
    
    # Display welcome message
    print('welcome to simple calculator')
    print("Available operations: + (addition), - (subtraction)(multiplication), / (division)")
    try:
        # Get user input for the first number
        num1 = float(input('Enter the first number: '))

        # Get user input for the operator
        operator = input('Enter the operator (+, -, *, /): ')

        # Get user input for the second number
        num2 = float(input('Enter second number: '))

        # Perform the calculation based on the operator
        if operator == '+':
            result = num1 + num2
            print(f'Result: {num1} + {num2} = {result}')
        elif operator == '-':
            result = num1 - num2
            print(f'Result: {num1} - {num2} = {result}')
        elif operator == '*':
            result = num1 * num2
            print(f'Result: {num1} * {num2} = {result}')
        elif operator == '/':
            # check for division error
            if num2 == 0:
                print('Error: Division by zero is not allowed!')
            else:
                result = num1 / num2
                print(f'Result: {num1} / {num2} = {result}')
        else:
            # Handle invalid operators
            print('Error: Invalid operator! Please use one of: = +, -, *, /')
    except ValueError:
        # Handle non-numeric input
        print('Error: Please input valid numbers')

# Run the calculator function
if __name__ == "__main__":
    simple_calculator()
        