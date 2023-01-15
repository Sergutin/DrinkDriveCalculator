from datetime import datetime, timedelta
from os import system

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
        start_app()
    elif start == 'n':
        quit()

# Standard drinks number in a drink in a pub-----------

standard_drinks_pub = {'Pints of lager, 3% (568ml)': 1.3,
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

standard_drinks_home = {'Cans of lager, 4.5% (500ml)': 1.8,
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
    welcome_message = print("""Welcome to Drink and Drive Calculator!\n
This tool calculates an estimated time
of processing alcohol for information
purposes only. On average, it takes one hour
to process one standard drink (for men).
Any amount of alcohol will affect your ability to drive.\n
Let's start!\n""")
welcome()

# Drink place input----------------------------------------

def start_app():
    drinks_number = 0
    process_time_pub = 0
    process_time_home = 0
    process_time = 0
    drink = 0
    place = input("Where were you Drinking: pub / home? \n")

    while place != 'pub' and place != 'home':
        print('Please use "pub" or "home" to reply \n')
        place = input("Where were you Drinking: pub / home? \n")

# Drink choice in a pub--------------------------------

    if place == 'pub':
        while True:
            try:
                drink = int(input("""\nWhat drinks did you have? Enter a number: \n
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
                    print(f'You entered {drink}. Please enter a number from 1 to 13.')

# Number of drinks choice in a pub--------------------------------

        try:
            drinks_number = int(input("How many drinks did you have? \n"))
        except ValueError:
            print("Please enter a number \n")
            drinks_number = int(input("How many drinks did you have? \n"))
        else:
            print(f'You entered: {drinks_number}')
            print('\n')

# Process time formula, pub

        process_time_pub = drinks_number * list(standard_drinks_pub.values())[drink - 1]
        p_time = str(round(process_time_pub, 1))
        time_pub = datetime.now() + timedelta(hours=process_time_pub)
        y = time_pub.strftime("%H:%M %Y-%m-%d")
        print(f'The alcohol should have left your system in: {p_time} hours at {y}')
        print("\nRemember! Drink responsibly and never ever drink and drive!")
        menu()


    # Process time formula
    # def process_time(number_of_drinks, standard_drinks):
    #     process_time = drink * list(standard_drinks.values())[drinks - 1]
    #     time_pub = datetime.now() + timedelta(hours=process_time)
    #     y = time_pub.strftime("%H:%M %Y-%m-%d")
    #     print(f'The alcohol should have left your system in: {process_time} hours at {y}')
    #     print("\nRemember! Drink responsibly and never ever drink and drive!")


# Drink choice at home--------------------------------

    if place == 'home':
        while True:
            try:
                drink = int(input("""\nWhat drinks did you have? Enter a number:\n
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
                    print(f'You entered {drink}. Please enter a number from 1 to 12.')

# Number of drinks choice at home--------------------------------

        try:
            drinks_number = int(input("How many drinks did you have? \n"))
        except ValueError:
            print("Please enter a number \n")
            drinks_number = int(input("How many drinks did you have? \n"))
        else:
            print(f'You entered: {drinks_number}')
            print('\n')

# Process time formula, home

        process_time_home = drinks_number * list(standard_drinks_home.values())[drink - 1]
        p_time = str(round(process_time_home, 1))
        time_home = datetime.now() + timedelta(hours=process_time_home)
        x = time_home.strftime("%H:%M %Y-%m-%d")
        print(f'The alcohol should have left your system in: {p_time} hours at {x}.')
        print("\nRemember! Drink responsibly and never ever drink and drive!")
        menu()
start_app()