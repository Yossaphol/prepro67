"""FizzBuzz"""
num = int(input())
i = 1
while i <= num:
    if not i % 3 and not i % 5:
        print("FizzBuzz")
    elif not i % 3:
        print("Fizz")
    elif not i % 5:
        print("Buzz")
    else:
        print(i)
    i += 1
