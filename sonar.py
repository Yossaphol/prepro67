def generate_pattern(n):
    # Generate the top half of the pattern
    for i in range(n):
        for j in range(n - i - 1):
            print("   ", end="")
        for j in range(i + 1):
            print(f"{n-j:02} ", end="")
        for j in range(i):
            print(f"{n-j-1:02} ", end="")
        print()
    
    # Generate the bottom half of the pattern
    for i in range(n-1):
        for j in range(i + 1):
            print("   ", end="")
        for j in range(n - i - 1):
            print(f"{n-j:02} ", end="")
        for j in range(n - i - 2):
            print(f"{n-j-1:02} ", end="")
        print()

n = int(input())
generate_pattern(n)