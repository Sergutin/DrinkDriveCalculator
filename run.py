drinks_pub = {'Pints of lager, 3% (568ml)',
'Pints of lager, 4.5% (568ml)',
'Bottles of lager, 4.5% (330ml)',
'Pints of stout, 4.2% (568ml)',
'Pints of cider, 4.5% (568ml)',
'Bottles of cider, 4.5% (330ml)',
'Bottles of alcopop, 4% (330ml)',
'Glasses of white wine, 12.5% (150ml)',
'Bottles of white wine, 12.5% (750ml)',
'Glasses of red wine, 12.5% (150ml)',
'Bottles of red wine, 12.5% (750ml)',
'Glasses of sparkling wine, 11.5% (125ml)',
'Measures of spirits, 40% (35.5ml)'}

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

drinks_home = {'Cans of lager, 4.5% (500ml)',
'Bottles of lager, 4.5% (330ml)',
'Cans of stout, 4.2% (500ml)',
'Cans of cider, 4.5% (500ml)',
'Bottles of cider, 4.5% (330ml)',
'Bottles of alcopop, 4% (330ml)',
'Glasses of white wine, 12.5% (150ml)',
'Bottles of white wine, 12.5% (750ml)',
'Glasses of red wine, 12.5% (150ml)',
'Bottles of red wine, 12.5% (750ml)',
'Glasses of sparkling wine, 11.5% (125ml)',
'Measures of spirits, 40% (35.5ml)'}

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

print("Wellcome to Drink and Drive Calculator!!")

print("\n")

gender = input("Are you male or female? m/f \n")
while gender != 'm' or gender != 'f':
    print('Please use "m" or "f" to reply \n')
    gender = input("Are you male or female? m/f \n")
    if gender == "m" or gender == "f":
        print(f'You entered {gender}')
        break

print("\n")

drinks_number = 0
process_time_pub = 0

place = input("Where were you Drinking: pub / home? \n")
while place != 'pub' or place != 'home':
    print('Please use "pub" or "home" to reply \n')
    place = input("Where were you Drinking: pub / home? \n")
    
    if place == 'pub':
        drinks_pub = int(input("""\n What drinks did you have? Enter a number: \n
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
        print(f'You entered: {drinks_pub}')
        print('\n')
    
        try:
            drinks_number = int(input("How many drinks did you have? \n"))
        except ValueError:
            print("Please enter a number \n")
            continue
        else:
            print(f'You entered: {drinks_number}')
            print('\n')

        process_time_pub = drinks_number * 3
        print(f'The alcohol should have left your system in: {process_time_pub} hours at _time_')
        break

    elif place == 'home':
        drinks_home = int(input("""\n What drinks did you have? Enter a number: \n
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
        print(f'You entered: {drinks_home}')
        print('\n')
        
        try:
            drinks_number = int(input("How many drinks did you have? \n"))
        except ValueError:
            print("Please enter a number \n")
            continue
        else:
            print(f'You entered: {drinks_number}')
            print('\n')

        process_time_home = drinks_number * 6
        print(f'The alcohol should have left your system in: {process_time_home} hours at _time_')
        break

print("\n")

# drinks_number = 0
# while True:
#     try:
#         drinks_number = int(input("How many drinks did you have? "))
#     except ValueError:
#         print("Please enter a number")
#         continue
#     else:
#         print(f'You entered: {drinks_number}')
#         break

# process_time_pub = drinks_pub(st_drinks_pub) * drinks_number 
# print(f'The alcohol should have left your system in: {process_time_pub} hours at {time}')