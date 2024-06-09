"""hopperv1"""
def main():
    """main"""
    num = int(input())
    my_dict = {}
    for _ in range(num):
        item = input()
        amount = int(input())
        my_dict[item] = my_dict.get(item, 0) + amount
    print("My Hopper has a list item:")
    for i, j in my_dict.items():
        print(f"{i} : {j}")
main()
