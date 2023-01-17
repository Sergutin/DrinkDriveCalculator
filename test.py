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

# Drinks list--------------------------------------------

drinks = {
    'pub': [
        {'text': 'Pints of lager, 3% (568ml)',
        'alcohol': 1.3},
        {'text': 'Pints of lager, 4.5% (568ml)',
        'alcohol': 2.05},
        {'text': 'Bottles of lager, 4.5% (330ml)',
        'alcohol': 1},
        {'text': 'Pints of stout, 4.2% (568ml)',
        'alcohol': 2.05},
        {'text': 'Pints of cider, 4.5% (568ml)',
        'alcohol': 2.05},
        {'text': 'Bottles of cider, 4.5% (330ml)',
        'alcohol': 1},
        {'text': 'Bottles of alcopop, 4% (330ml)',
        'alcohol': 1.2},
        {'text': 'Glasses of white wine, 12.5% (150ml)',
        'alcohol': 1.5},
        {'text': 'Bottles of white wine, 12.5% (750ml)',
        'alcohol': 7.5},
        {'text': 'Glasses of red wine, 12.5% (150ml)',
        'alcohol': 1.5},
        {'text': 'Bottles of red wine, 12.5% (750ml)',
        'alcohol': 7.5},
        {'text': 'Glasses of sparkling wine, 11.5% (125ml)',
        'alcohol': 1},
        {'text': 'Measures of spirits, 40% (35.5ml)',
        'alcohol': 1}
    ],
    'home': [
        {'text': 'Cans of lager, 4.5% (500ml)',
        'alcohol': 1.8},
        {'text': 'Bottles of lager, 4.5% (330ml)',
        'alcohol': 1},
        {'text': 'Cans of stout, 4.2% (500ml)',
        'alcohol': 1.8},
        {'text': 'Cans of cider, 4.5% (500ml)',
        'alcohol': 1.8},
        {'text': 'Bottles of cider, 4.5% (330ml)',
        'alcohol': 1},
        {'text': 'Bottles of alcopop, 4% (330ml)',
        'alcohol': 1.2},
        {'text': 'Glasses of white wine, 12.5% (150ml)',
        'alcohol': 1.5},
        {'text': 'Bottles of white wine, 12.5% (750ml)',
        'alcohol': 7.5},
        {'text': 'Glasses of red wine, 12.5% (150ml)',
        'alcohol': 1.5},
        {'text': 'Bottles of red wine, 12.5% (750ml)',
        'alcohol': 7.5},
        {'text': 'Glasses of sparkling wine, 11.5% (125ml)',
        'alcohol': 1},
        {'text': 'Measures of spirits, 40% (35.5ml)',
        'alcohol': 1}
    ]
}

# Welcome--------------------------------------------------

def welcome():
    welcome_message = print("""Welcome to Drink and Drive Calculator!\n
This tool calculates an estimated time
of processing alcohol for information
purposes only. On average, it takes one hour
to process one standard drink.
Any amount of alcohol will affect your ability to drive.\n
Let's start!\n""")
welcome()

# Drink place input----------------------------------------

def start_app():
    drinks_number = 0
    process_time = 0
    drink = 0
    place = input("Where were you Drinking: pub / home? \n")

# Process time formula 

    def process_time():
        process_t = drinks_number * list(drinks.values())[drink - 1]
        p_time = str(round(process_t, 1))
        time_final = datetime.now() + timedelta(hours=process_time_pub)
        y = time_final.strftime("%H:%M %Y-%m-%d")
        print(f'The alcohol should have left your system in: {p_time} hours at {y}')
        print("\nRemember! Drink responsibly and never ever drink and drive!")
        menu()

    while place != 'pub' and place != 'home':
        print('Please use "pub" or "home" to reply \n')
        place = input("Where were you Drinking: pub / home? \n")

# Drink choice in a pub--------------------------------

    if place == 'pub':
        print('\nWhat drinks did you have? Enter a number:\n')
        for index, items in enumerate(drinks['pub']):
            print(f'{index + 1}: {items.get("text")}')
        while True:
            try:
                drink = int(input())
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
        process_time()

# Drink choice at home--------------------------------

    if place == 'home':
        print('\nWhat drinks did you have? Enter a number:\n')
        for index, items in enumerate(drinks['home']):
            print(f'{index + 1}: {items.get("text")}')
        while True:
            try:
                drink = int(input())
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
        process_time()
start_app()