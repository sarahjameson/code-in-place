"""
Asks the user for two numbers and prints the result
of the first number minus the second number.
"""

def main():
    print("This program subtracts one number from another.")
    number1 = input("Enter first number: ")
    number2 = input("Enter second number: ")
    print("The result is",float(number1) - float(number2))

if __name__ == '__main__':
    main()