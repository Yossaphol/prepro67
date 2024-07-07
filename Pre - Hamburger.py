"""Pre - Hamburger"""
def main():
    """main"""
    front = int(input())
    end = int(input())
    pork = (front + end) * 2
    print(front * "|" + pork * "*" + end * "|")
main()
