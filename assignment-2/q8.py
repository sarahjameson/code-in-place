"""
TODO: Write a description here
"""

import random

def main():
    stones = 20
    player = 1
    while stones > 0:
        print(f"There are {stones} stones left")
        choice = int(input(f"Player {player} would you like to remove 1 or 2 stones? "))
        while choice < 1 or choice > 2:
            choice = int(input("Please enter 1 or 2: "))
        print()
        if choice == 1:
            stones -= 1
        elif choice == 2:
            stones -= 2
        if player == 1:
            player = 2
        else:
            player = 1
    print(f"Player {player} wins!")



if __name__ == '__main__':
    main()