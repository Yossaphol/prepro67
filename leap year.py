"""leap year"""
cs = int(input())
if not cs % 4:
    if not cs % 100:
        if not cs % 400:
            print("True")
        else:
            print("False")
    else:
        print("True")
else:
    print("False")
