"""(Khaow) Natasha Romanoff"""
def main() :
    """main"""
    text = input()
    char1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char2 = "NOPQRSTUVWXYZABCDEFGHIJKLM"
    result = ''
    for i in text :
        if char1.find(i) != -1 :
            result += char2[char1.find(i)]
        else :
            result += " "
    print(result)
main()
