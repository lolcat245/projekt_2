"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
Hra "Bulls & Cows"
Kurz 'Datový analytik s Pythonem'

author: Jana Zamachajeva
email: janazamachajeva@seznam.cz
"""
import random

separator = "-"*50

results = {
    "bulls": 0,
    "cows": 0
}

# pocitadlo pokusu
counter = 0

# funkce pro kontrolu vstupu
# zadane cislo musi mit 4 unikatni cislice a nesmi zacinat nulou
def input_control(number):
    if not number.isdigit():
        print("Enter a number, not just random letters.")
        return False
    if len(number) != 4:
        print(f"The number is {len(number)}",
              "characters long, enter a 4-digit number.")
        return False
    if len(set(number)) != 4:
        print("All the digits should be different.")
        return False
    if number[0] == "0":
        print("The number can\'t start with 0.")
        return False
    return True

# funkce pro vyhodnoceni bulls/cows
def evaluating_the_number(mine, comp):
    for digit in range(4):
        if mine[digit] in comp:
            results["cows"] += 1
            if mine[digit] == comp[digit]:
                results["bulls"] += 1
    return results["bulls"], results["cows"]

# pozdrav
print(   
    separator,
    "Hi there!",
    separator,
    "I\'ve generated a random 4 digit number for you.",
    "Let\'s play a bulls and cows game.",
    separator,
    sep="\n"
)

# vygenerovani 4mistneho cisla s unikatnimi cislicemi
figure = random.sample(range(10), 4)
if figure[0] == 0: # pokud cislo zacina 0, prohodim prvni 2 cifry
    figure[0], figure[1] = figure[1], figure[0]
comp_number = ''.join(str(f) for f in figure)

# uzivatelsky vstup
while True:
    my_number = input("Enter a number: ")
    print(separator)
    """
    nasledujici maly loop tu uvadim z toho duvodu, ze pokud uzivatel zada
    spravne 4mistne cislo az po nekolika pokusech, je lepsi naznacit, ze
    posledni cislo je spravne a hra muze zacit 
    """
    if input_control(my_number):
        print("So, let\'s play!") 
        break

# porovnani vstupu a random vygenerovaneho cisla
while True:
    counter += 1
    results["bulls"] = 0
    results["cows"] = 0

    # vyhodnoceni zadaneho cisla
    if not input_control(my_number):
        print("C\'mon, you know that this number is not ok.")
    evaluating_the_number(my_number, comp_number)

    # vypisovani vysledku
    if results["bulls"] == 4:
        print(f"Correct, you\'ve guessed the right number in {counter}",
              "guesses!")
        break
    else:
        if results["bulls"] == 1 and results["cows"] == 1:
            print("1 bull, 1 cow", separator, sep="\n")
            my_number = input("Try again: ")
        elif results["bulls"] == 1:
            print(f"1 bull, {results["cows"]} cows", separator, sep="\n")
            my_number = input("Try again: ")
        elif results["cows"] == 1:
            print(f"{results["bulls"]} bulls, 1 cow", separator, sep="\n")
            my_number = input("Try again: ")
        else:   
            print(f"{results["bulls"]} bulls, {results["cows"]} cows", 
                  separator, sep="\n")
            my_number = input("Try again: ")
        print(separator)