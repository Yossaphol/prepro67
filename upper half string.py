"""(Beer) Uppercase Half String"""
import math
def main() :
    """main"""
    text = input()
    text2 = ''
    for i in text :
        if i.isalpha() or i == " ":
            text2 += i
    text = text2
    half = math.ceil(len(text) / 2)
    text2 = ''
    for i , v in enumerate(text) :
        if i <= half-1 :
            text2 += v.upper()
        else :
            text2 += v.lower()
    print(text2)
main()
