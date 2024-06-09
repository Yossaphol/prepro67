"""Flight Ticket"""
def main() :
    """main"""
    text = input()
    name_start = text.find("Name") + 5
    name_end = text.find("From") - 1
    name = text[name_start:name_end]
    print(name)

    from_start = text.find("From") + 5
    from_end = text.find("To") - 1
    come_from = text[from_start:from_end]
    print(come_from.lower())

    to_start = text.find("To") + 3
    to = text[to_start:]
    print(to.lower())
main()
