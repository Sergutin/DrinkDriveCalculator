print("Wellcome to Drink and Drive Calculator!!")

gender = input("Are you male or female? m/f ")
while gender != 'm' or gender != 'f':
    print('Please use "m" or "f" to reply')
    gender = input("Are you male or female? m/f ")
    if gender == "m" or gender == "f":
        print(gender)
        break

print("\n")

place = input("Where were you Drinking: pub / home? ")
while place != 'pub' or place != 'home':
    print('Please use "pub" or "home" to reply')
    place = input("Where were you Drinking: pub / home? ")
    
    print("\n")

    if place == 'pub':
        drinks = int(input("""What drinks did you have?
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
        13. Measures of spirits, 40% (35.5ml)
        """))
        print(f'You entered: {drinks}')
        break

    elif place == 'home':
        drinks = int(input("""What drinks did you have?
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
        12. Measures of spirits, 40% (35.5ml) 
        """))
        print(f'You entered: {drinks}')
        break

print("\n")

drinks_number=0
while True:
    try:
        drinks_number = int(input("How many drinks did you have? "))
    except ValueError:
        print("Please enter a number")
        continue
    else:
        print(f'You entered: {drinks_number}')
        break