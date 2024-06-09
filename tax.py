"""tax"""
import math
def main():
    """tax tax"""
    income = int(input())
    result = 0
    if income > 10000000 :
        income -= 10000000
        result += math.ceil(income * 0.4)
        income = 10000000
    if 3500001 <= income <= 10000000:
        income -= 3500000
        result += math.ceil(income * .35)
        income = 3500000
    if 1500001 <= income <= 3500000:
        income -= 1500000
        result += math.ceil(income * .3)
        income = 1500000
    if 700001 <= income <= 1500000:
        income -= 700000
        result += math.ceil(income * .25)
        income = 700000
    if 350001 <= income <= 700000:
        income -= 350000
        result += math.ceil(income * .2)
        income = 350000
    print(f"You have to pay {result:,} baht.")
main()
