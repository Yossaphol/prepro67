"""Let's Fill The Jar With Stars!"""
STAR = int(input())
if STAR >= 25:
    STAR = STAR - 25
    print("-------")
    print("|*****|")
    print("|*****|")
    print("|*****|")
    print("|*****|")
    print("|*****|")
    print("-------")
    print(f"Stars left : {STAR}")
else:
    for row in range(7):
        for col in range(7):
            if not row or row == 6:
                print("-",end='')
            elif (not col and 0 < row <= 5) or (col == 6 and 0 < row <= 5):
                print("|",end='')
            else:
                if STAR:
                    print("*",end='')
                    STAR -= 1
                else:
                    print(" ",end='')
        print()
    print("Stars left : 0")
