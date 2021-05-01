"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 
MIN_NUMBER = 10
MAX_NUMBER = 100

def main():
    number1 = random.randint(MIN_NUMBER,MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER,MAX_NUMBER)
    print("What is " + str(number1) + "+" + str(number2) + "?")
    answer = number1 + number2
    guess = input("Your answer: ")
    if int(guess) == int(answer):
        print("Correct")
    else:
        print("Incorrect. The expected answer is ", answer)

if __name__ == '__main__':
    main()