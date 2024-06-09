"""item check"""
def main():
    """main"""
    text = input().lower()
    text2 = input()
    check = text2.lower()
    have_text = text.split()
    if check in have_text:
        print(f"{text2} is in the list")
    else:
        print(f"{text2} is not in the list")
main()
