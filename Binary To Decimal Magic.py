"""(Cruz) Binary To Decimal Magic"""
def main() :
    """main"""
    text = input()
    num = text[::-1]
    result = 0
    for i , v in enumerate(num) :
        result += (2**i) * int(v)
    print(result)
main()
