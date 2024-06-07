"""salmontuna"""
COUNTSALMON = 0
COUNTTUNA = 0
while True:
    FISH = str(input())
    if FISH == 'Empty':
        break
    if FISH == 'Salmon':
        COUNTSALMON += 1
    elif FISH == 'Tuna':
        COUNTTUNA += 1
print(f"Salmon : {COUNTSALMON}")
print(f"Tuna : {COUNTTUNA}")
