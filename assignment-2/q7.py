"""
TODO: Write a description here
"""

import random

def main():
    IN_A_ROW = 3
    correct = 0
    while correct < 3:
        number1 = random.randint(1,200)
        number2 = random.randint(1,200)
        answer = number1 + number2
        print("What is " + str(number1) + " + " + str(number2) + "?")
        guess = input("Your answer: ")
        if int(guess) == answer:
            correct += 1
            print(f"Correct! You've gotten {correct} correct in a row.")
        else:
            correct = 0
            print(f"Incorrect. The expected answer is {answer}")
    print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()