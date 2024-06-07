"""pizza"""
import math

def pizza(rad, thick):
    """pizza"""
    if rad > 0 and thick > 0:
        volume = math.pi * (rad ** 2) * thick
        per = volume / 6
        print(f"{volume:.2f}")
        print(f"{per:.2f}")
    else:
        print("No Pizza")
pizza(int(input()), int(input()))
