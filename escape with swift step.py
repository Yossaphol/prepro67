"""esc with swift step"""
import math
def kirito():
    """kirito"""
    x = float(input())
    y =float(input())
    x1 =float(input())
    y1 =float(input())
    x2 =float(input())
    y2 =float(input())
    x3 =float(input())
    y3 =float(input())
    x4 = float(input())
    y4 =float(input())
    p1 = math.sqrt(((x1 - x)** 2) + ((y1 - y)**2))
    p2 = math.sqrt(((x2 - x)** 2) + ((y2 - y)**2))
    p3 = math.sqrt(((x3 - x)** 2) + ((y3 - y)**2))
    p4 = math.sqrt(((x4 - x)** 2) + ((y4 - y)**2))
    count = 0
    if p1 <= 35:
        count += 1
    if p2 <= 35:
        count += 1
    if p3 <= 35:
        count += 1
    if p4 <= 35:
        count += 1
    if not count:
        print("Oh no! This position is bad...")
    else:
        print(f"I can use Swift Step to {count} allies.")
kirito()
