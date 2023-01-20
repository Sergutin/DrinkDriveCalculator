from datetime import datetime, timedelta
from os import system, name


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def menu():
    start = input('Do you want to start again? y / n\n')
    while start != 'y' and start != 'n':
        print('Please use "y" or "n" to reply\n')
        start = input('Do you want to start again? y / n\n')
    if start == 'y':
        clear()
        start_app()
    elif start == 'n':
        print("Thank you for using our app!")
        quit()


# Standard drinks number in a drink in a pub-----------

st_drinks_pub = {'Pints of lager, 3% (568ml)': 1.3,
                 'Pints of lager, 4.5% (568ml)': 2.05,
                 'Bottles of lager, 4.5% (330ml)': 1,
                 'Pints of stout, 4.2% (568ml)': 2.05,
                 'Pints of cider, 4.5% (568ml)': 2.05,
                 'Bottles of cider, 4.5% (330ml)': 1,
                 'Bottles of alcopop, 4% (330ml)': 1.2,
                 'Glasses of white wine, 12.5% (150ml)': 1.5,
                 'Bottles of white wine, 12.5% (750ml)': 7.5,
                 'Glasses of red wine, 12.5% (150ml)': 1.5,
                 'Bottles of red wine, 12.5% (750ml)': 7.5,
                 'Glasses of sparkling wine, 11.5% (125ml)': 1,
                 'Measures of spirits, 40% (35.5ml)': 1}

# Standard drinks number in a drink at home-------------

st_drinks_home = {'Cans of lager, 4.5% (500ml)': 1.8,
                  'Bottles of lager, 4.5% (330ml)': 1,
                  'Cans of stout, 4.2% (500ml)': 1.8,
                  'Cans of cider, 4.5% (500ml)': 1.8,
                  'Bottles of cider, 4.5% (330ml)': 1,
                  'Bottles of alcopop, 4% (330ml)': 1.2,
                  'Glasses of white wine, 12.5% (150ml)': 1.5,
                  'Bottles of white wine, 12.5% (750ml)': 7.5,
                  'Glasses of red wine, 12.5% (150ml)': 1.5,
                  'Bottles of red wine, 12.5% (750ml)': 7.5,
                  'Glasses of sparkling wine, 11.5% (125ml)': 1,
                  'Measures of spirits, 40% (35.5ml)': 1}


# Welcome--------------------------------------------------

def welcome():
    print("""Welcome to Drink and Drive Calculator!\n
This tool calculates an estimated time
of processing alcohol for information
purposes only. On average, it takes one hour
to process one standard drink.
Any amount of alcohol will affect your ability to drive.\n
Let's start!\n""")


# Drink place input----------------------------------------

def start_app():
    welcome()
    drinks_num = 0
    drink = 0
    place = input("Where were you Drinking: pub / home? \n")

    while place != 'pub' and place != 'home':
        print('Please use "pub" or "home" to reply \n')
        place = input("Where were you Drinking: pub / home? \n")

# Drink choice in a pub--------------------------------

    if place == 'pub':
        while True:
            try:
                drink = int(input("""
What drinks did you have? Enter a number: \n
1. Pints of lager, 3% (568ml)
2. Pints of lager, 4.5% (568ml)
3. Bottles of lager, 4.5% (330ml)
4. Pints of stout, 4.2% (568ml)
5. Pints of cider, 4.5% (568ml)
6. Bottles of cider, 4.5% (330ml)
7. Bottles of alcopop, 4% (330ml)
8. Glasses of white wine, 12.5% (150ml)
9. Bottles of white wine, 12.5% (750ml)
10. Glasses of red wine, 12.5% (150ml)
11. Bottles of red wine, 12.5% (750ml)
12. Glasses of sparkling wine, 11.5% (125ml)
13. Measures of spirits, 40% (35.5ml) \n
"""))
            except ValueError:
                print('Please enter a number from 1 to 13.')
            else:
                if 1 <= drink <= 13:
                    print(f'You entered: {drink}')
                    print('\n')
                    break
                else:
                    print(f'You entered {drink}. Please enter'
                          'a number from 1 to 13.')

# Number of drinks choice in a pub--------------------------------

        while True:
            try:
                drinks_num = int(input("How many drinks did you have? \n"))
                print(f'You entered: {drinks_num}')
                break
            except ValueError:
                print("Please enter a number \n")
                continue
        process_time(drinks_num, st_drinks_pub, drink)

# Drink choice at home--------------------------------

    if place == 'home':
        while True:
            try:
                drink = int(input("""\n
What drinks did you have? Enter a number:\n
1. Cans of lager, 4.5% (500ml)
2. Bottles of lager, 4.5% (330ml)
3. Cans of stout, 4.2% (500ml)
4. Cans of cider, 4.5% (500ml)
5. Bottles of cider, 4.5% (330ml)
6. Bottles of alcopop, 4% (330ml)
7. Glasses of white wine, 12.5% (150ml)
8. Bottles of white wine, 12.5% (750ml)
9. Glasses of red wine, 12.5% (150ml)
10. Bottles of red wine, 12.5% (750ml)
11. Glasses of sparkling wine, 11.5% (125ml)
12. Measures of spirits, 40% (35.5ml) \n
"""))
            except ValueError:
                print('Please enter a number from 1 to 12.')
            else:
                if 1 <= drink <= 12:
                    print(f'You entered: {drink}')
                    print('\n')
                    break
                else:
                    print(f'You entered {drink}. Please enter'
                          'a number from 1 to 12.')

# Number of drinks choice at home--------------------------------

        while True:
            try:
                drinks_num = int(input("How many drinks did you have? \n"))
                print(f'You entered: {drinks_num}')
                break
            except ValueError:
                print("Please enter a number \n")
                continue
        process_time(drinks_num, st_drinks_pub, drink)


# Process time formula

def process_time(drinks_num, st_drinks_location, drink):

    time = drinks_num * list(st_drinks_location.values())[drink - 1]
    time_r = str(round(time, 1))
    time_drive = datetime.now() + timedelta(hours=time)
    date = time_drive.strftime("%H:%M %Y-%m-%d")
    print(f'The alcohol should have left your system in: {time_r}h at {date}')
    print("\n")
    print("Remember! Drink responsibly and never drink and drive!")
    menu()


start_app()
