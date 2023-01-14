from datetime import datetime, timedelta

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

print("Welcome to Drink and Drive Calculator!")

print("\n")

# Gender input---------------------------------------------

gender = input("Are you male or female? m/f \n")
print(f'You entered: {gender}')
while gender != 'm' and gender != 'f':
    print('Please use "m" or "f" to reply \n')
    gender = input("Are you male or female? m/f \n")

print("\n")

drinks_number = 0
process_time_pub = 0
drinks_pub = 0
drinks_home = 0

# Drink place input----------------------------------------

place = input("Where were you Drinking: pub / home? \n")

while place != 'pub' and place != 'home':
    print('Please use "pub" or "home" to reply \n')
    place = input("Where were you Drinking: pub / home? \n")

    # Drink choice in a pub--------------------------------

if place == 'pub':
    while True:
        try:
            drinks_pub = int(input("""\nWhat drinks did you have? Enter a number: \n
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
            if 1 <= drinks_pub <= 13:
                print(f'You entered: {drinks_pub}')
                print('\n')
                break
            else:
                print(f'You entered {drinks_pub}. Please enter a number from 1 to 13.')

# Number of drinks choice in a pub--------------------------------
    while True:
        try:
            drinks_number = int(input("How many drinks did you have? \n"))
        except ValueError:
            print("Please enter a number \n")
            drinks_number = input("How many drinks did you have? \n")
        else:
            print(f'You entered: {drinks_number}')
            print('\n')

# Process time formula, pub

    process_time_pub = drinks_number * list(standard_drinks_pub.values())[drinks_pub - 1]
    time_pub = datetime.now() + timedelta(hours=process_time_pub)
    print(f'The alcohol should have left your system in: {process_time_pub} hours at {time_pub}')

# Drink choice at home--------------------------------

if place == 'home':
    while True:
        try:
            drinks_home = int(input("""\nWhat drinks did you have? Enter a number: \n
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
            if 1 <= drinks_home <= 12:
                print(f'You entered: {drinks_home}')
                print('\n')
                break
            else:
                print(f'You entered {drinks_home}. Please enter a number from 1 to 12.')

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

    process_time_home = drinks_number * list(standard_drinks_home.values())[drinks_home - 1]
    time_home = datetime.now() + timedelta(hours=process_time_home)
    print(f'The alcohol should have left your system in: {process_time_home} hours at {time_home}')