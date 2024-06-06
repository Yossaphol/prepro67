"""year"""
past = float(input())
present = float(input())
x = present - past
y = x / past * 100
future = x / past * present + present
print(f"The price has increased {y:.4f}% from 10 years ago.")
print(f"In next 10 years price will be {future:.2f} baht.")
