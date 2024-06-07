"""song"""
levelsong = int(input())
EXP = 0
COUNT = 0
GAIN = 0
while True:
    leveling = input()
    if leveling == 'End':
        break
    GAIN += int(leveling)
    EXP += int(leveling)
    while EXP > levelsong ** 2 + 1000:
        COUNT += 1
        levelsong += 1
        EXP -= levelsong ** 2 + 1000
print(f"Exp gained : {GAIN}")
print(f"{COUNT} Level up, Now you are level {levelsong}")
