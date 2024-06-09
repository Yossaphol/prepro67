"""goku"""
def main():
    """main"""
    num = int(input())
    my_dict = {}
    for _ in range(num):
        food = input()
        amount = int(input())
        my_dict[food] = amount
    ask = input()
    print(f"Goku's Shopping List: {my_dict}")
    print(my_dict[ask])
main()
