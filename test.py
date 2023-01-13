# gender = input("Are you male or female? m/f \n")
# while gender != 'm' or gender != 'f':
#     print('Please use "m" or "f" to reply \n')
#     gender = input("Are you male or female? m/f \n")
#     if gender == "m" or gender == "f":
#         print(f'You entered {gender}')
#         break

gender = input("Are you male or female? m/f \n")
while gender != 'm' and gender != 'f':
    print('Please use "m" or "f" to reply \n')
    gender = input("Are you male or female? m/f \n")
    if gender == "m" or gender == "f":
        print(f'You entered {gender}')
        break



    # if gender == "m" or gender == "f":
    #     print(f'You entered: {gender}')
    #     break
    