"""(Cruz) Fishing assistant"""
def main() :
    """def"""
    land = input()
    num = int(input())

    land = land[num:num+1]
    if land == "~" :
        print("That's Water!")
    else :
        print("That's Land!")
main()
