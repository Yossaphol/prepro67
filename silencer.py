"""silencer"""
def silence(a, b):
    """silence"""
    if a > 15 and b > 15:
        print("Silence, All of you!")
    elif a > 15 or b > 15:
        print("Silence, mere mortal.")
    elif a <= 15 and b <= 15:
        print("Hmm... Silence is golden.")
silence(len(input()), len(input()))
