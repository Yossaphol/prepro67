"""(Moss) Secret Message"""
def main() :
    """main"""
    num = int(input())
    result = ''
    for i in range(num) :
        text = input()
        if len(text) <= i :
            result += text[len(text)-1]
        else :
            result += text[i]
    print(result)
main()
