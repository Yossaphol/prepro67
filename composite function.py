"""function"""
def f(x):
    """fx"""
    return 3 * x + 5
def g(x):
    """gx"""
    return (f(4 * x) + 23) / 2
def h(x, y):
    """hxy"""
    return (g(f(3 * y) + 2 * x) - g(2 * y)) * (f(4 * y) + 5 * x)

print(f"{h(float(input()), float(input())):.2f}")
