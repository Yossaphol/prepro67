"""creep score"""
def cspm(cs, time):
    """creep score"""
    return cs / time
print(f"CSPM = {cspm(int(input()), int(input())):.2f}")
