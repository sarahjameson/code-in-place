"""
TODO: Write a description here
"""

import random 

def main():
    steps = 0
    number = int(input("Enter a number: "))
    while number > 1:
        if number % 2 == 0:
            original_number = number
            number = number // 2
            print(f"{original_number} is even, so I take half: {number}")
            steps += 1
        elif number % 2 ==  1:
            original_number = number
            number = 3 * number + 1
            print(f"{original_number} is odd, so I make 3n+1: {number}")
            steps += 1
    print(f"The process took {steps} steps to reach 1")

if __name__ == "__main__":
    main()