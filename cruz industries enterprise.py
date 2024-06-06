"""Cruz Industries Enterprise"""
name = input()
age = int(input())
exp = int(input())
if age > exp:
    if 15 <= age <= 20:
        parent = input()
        if parent == 'No':
            print(f"{name}, you aren\'t accepted.")
        else:
            if 0 <= exp <= 2:
                print(f"{name}, you\'re Newbie Cruz of Cruz Industries Enterprise.")
            elif 3 <= exp <= 5:
                print(f"{name}, you\'re Advance Cruz of Cruz Industries Enterprise.")
            else:
                print(f"{name}, you\'re Master universal Cruz of Cruz Industries Enterprise.")
    elif 50 <= age <= 60:
        if exp > 5:
            print(f"{name}, you\'re Master universal Cruz of Cruz Industries Enterprise.")
        else:
            print(f"{name}, you aren\'t accepted.")
    elif 20 <= age <= 50:
        if 0 <= exp <= 2:
            print(f"{name}, you\'re Newbie Cruz of Cruz Industries Enterprise.")
        elif 3 <= exp <= 5:
            print(f"{name}, you\'re Advance Cruz of Cruz Industries Enterprise.")
        else:
            print(f"{name}, you\'re Master universal Cruz of Cruz Industries Enterprise.")
    else:
        print(f"{name}, you aren\'t accepted.")
else:
    print(f"{name}, you aren\'t accepted.")
