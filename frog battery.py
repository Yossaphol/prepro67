"""(Cruz) Placeholder"""
def main() :
    """def"""
    text = input()
    start = text.find("-")+1
    end = text.find(":")
    text = text[start:end]
    print(text)
main()
