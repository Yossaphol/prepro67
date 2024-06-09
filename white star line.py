"""(Ford) White Star Line"""
def main() :
    """main"""
    ws = 0
    nws = 0
    while True :
        name = input()
        if name != "END" :
            if name.endswith("ic") :
                ws += 1
            else :
                nws += 1
        else :
            break
    print(f"There are a total of {ws} White Star Line fleets.")
    print(f"There are a total of {nws} non-White Star Line fleets.")
main()
