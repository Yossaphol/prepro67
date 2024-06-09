"""doc"""
def main():
    """ssss"""
    have_cat = []
    cat = 0
    while True:
        bag = input().lower()
        if bag == "-1":
            break
        if bag.count("cat"):
            cat += 1
            have_cat.append(bag)
    print(f"The number of cat in bag {cat}")
    print(f"List of cat {have_cat}")
main()
