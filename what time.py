"""time"""
num = int(input())
day = num // 86400
hour = (num // 3600) % 24
mins = (num // 60) % 60
sec = num % 60
print(f"{day:>02}:{hour:>02}:{mins:>02}:{sec:>02}")
