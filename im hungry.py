"""hungry"""
check = input()
if check == 'Hungry':
    food = input()
    if food == 'Empty':
        print("There must be only one way left.")
    elif food == 'Cooked Chicken':
        print("I\'d rather die than eat this.")
    else:
        print("I survived.")
else:
    print("I\'m fine.")
