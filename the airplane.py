"""the airplane"""
NUM = int(input())
COUNT = 0
for row in range(NUM):
    for col in range(NUM+1):
        if row >= (NUM - col):
            print("*", end='')
            COUNT = COUNT + 1
        else:
            print(" ",end='')
    print()
print(f"The number of stars use {COUNT}")
