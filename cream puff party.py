"""cream puff party"""
need = float(input())
energy = float(input())

if energy >= need:
    print("Cream Puff Party")
else:
    CREAM = 334
    COUNT = 0
    while need > energy:
        energy += CREAM
        CREAM += 5
        COUNT += 1
    print(COUNT)
