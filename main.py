"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
Hra "Bulls & Cows"
Kurz 'Datový analytik s Pythonem'

author: Jana Zamachajeva
email: janazamachajeva@seznam.cz

"""

import random

separator = "-"*50

const = 4

# input control function
# the number should be 4 digits long and cant start with 0
def input_control(number):
    if not number.isdigit():
        print("Enter a number, not just random letters.")
        return False
    if len(number) != const:
        print(
            f"The number is {len(number)} characters long, "                  
            f"enter a {const}-digit number."
            )
        return False
    if len(set(number)) != const:
        print("All the digits should be different.")
        return False
    if number[0] == "0":
        print("The number can\'t start with 0.")
        return False
    return True

# generating random 4-digit number, cant start with 0
def comp_number():
    x = random.sample(range(10), 4)
    if x[0] == 0:
        return comp_number()
    return ''.join(str(d) for d in x)

# evaluation of bulls/cows
def evaluating_the_number(mine, comp):
    bulls = 0
    cows = 0
    for digit in range(const):
        if mine[digit] in str(comp):
            cows += 1
            if mine[digit] == str(comp)[digit]:
                bulls += 1
    return bulls, cows

def main():

    # number of guesses
    counter = 0

    # introduction message for an user
    print(   
        separator,
        "Hi there!",
        separator,
        "I\'ve generated a random 4 digit number for you.",
        "Let\'s play a bulls and cows game.",
        separator,
        sep="\n"
    )

    secret = comp_number()

    # enter a number
    while True:
        my_number = input("Enter a number: ")
        print(separator)
        if input_control(my_number):
            print("So, let\'s play!") 
            break
    
    # comparing the user number and randomly generated number
    while True:
        counter += 1

        bulls, cows = evaluating_the_number(my_number, secret)

        # results
        if bulls == const:
            print(f"Correct, you\'ve guessed the right number in {counter}",
            "guesses!")
            break
        else:
            if bulls == 1 and cows == 1:
                print("1 bull, 1 cow", separator, sep="\n")
                my_number = input("Try again: ")
            elif bulls == 1:
                print(f"1 bull, {cows} cows", separator, sep="\n")
                my_number = input("Try again: ")
            elif cows == 1:
                print(f"{bulls} bulls, 1 cow", separator, sep="\n")
                my_number = input("Try again: ")
            else:   
                print(f"{bulls} bulls, {cows} cows", 
                    separator, sep="\n")
                my_number = input("Try again: ")
            print(separator)

if __name__ == "__main__":
    main()