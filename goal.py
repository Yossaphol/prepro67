"""goal"""
home = int(input())
away = int(input())
if home > away:
    print("Home Win!")
elif home < away:
    print("Away Win!")
else:
    print("Draw!")
