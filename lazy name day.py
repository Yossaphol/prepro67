"""days"""
def main():
    """main"""
    days = {"sun" : "Sunday", "mon" : "Monday", "tues" : "Tuesday", "wed" :\
"Wednesday", "thurs" : "Thursday", "fri" : "Friday", "sat" : "Saturday"}
    for _ in range(5):
        day = input().lower()
        print(days[day])
main()
