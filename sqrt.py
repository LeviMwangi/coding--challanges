import math

try:
    number = float(input('Enter number here: '))
    if number < 0:
        print('Error: Cannot calculate sqaure root of a negative number')
    else:
        square_root = math.sqrt(number)
        print(f'The square root of {number} is {square_root:.4f}')

except ValueError:
    print('Error: Please enter a valid number')