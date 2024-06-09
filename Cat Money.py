"""(In) Cat Money"""
def main() :
    """main"""
    account = input()
    price = 0
    acc = ''
    have_num1 = False
    for i in account :
        if i.isnumeric() :
            acc += i
            have_num1 = True

    if have_num1 :
        while True :
            money = input()

            have_num = False
            for i in money :
                if i.isnumeric() :
                    have_num = True

            if have_num :
                money2 = ''
                for i in money :
                    if i.isnumeric() :
                        money2 += i
                price += int(money2)
            else :
                break
        print(f"Account: {acc} | {price:,} Baht")
    else :
        print("ERROR")
main()
