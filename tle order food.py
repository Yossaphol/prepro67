"""(Tle) พี่เติ้ลตามสั่ง"""
def main() :
    """main"""
    menu = input()
    if menu.find("Special") != -1 :
        print(f"{menu} Total 50 baht!!!")
    else :
        print(f"{menu} Total 40 baht!!!")
main()
