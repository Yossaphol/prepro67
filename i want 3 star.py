"""champion"""
star = int(input())
champion = 9 - star
if champion <= 0:
    print("Success! You created a 3 stars champion!")
else:
    print(f"You need {champion} more to get 3 stars champion.")
