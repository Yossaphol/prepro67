"""take flight"""
def main():
    """main"""
    cls = input().upper()
    if cls in ('R', 'P', 'F', 'A'):
        print("First Class")
    elif cls in ('J', 'C', 'D', 'I'):
        print("Business Class")
    elif cls == 'W':
        print("Premium economy Class")
    elif cls in ('S', 'Y', 'B', 'II', 'K', 'L'):
        print("Economy Class")
    elif cls in ('M', 'T', 'Q', 'V', 'X'):
        print("Economy Class")
    else:
        print("invalid booking code")
main()
