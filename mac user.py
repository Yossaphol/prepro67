"""main"""
MAC = input()
SERIE = input()
MONI = input()
SIZE = input()
if MAC == "MacBook Air":
    if SIZE == '2':
        if SERIE == 'M2':
            if MONI == '13':
                print("34,900")
            else:
                print("unavailable ")
        elif SERIE == 'M3':
            if MONI == '13':
                print("39,900")
            elif MONI == '15':
                print("47,900")
            else:
                print("unavailable ")
        else:
            print("unavailable ")
    else:
        print("unavailable ")
elif MAC == "MacBook Pro":
    if SERIE == 'M3' and SIZE == '2' and MONI == '14':
        print("59,900")
    elif (SERIE in ('M3 Pro', 'M3 Max')) and SIZE == '8':
        if MONI == '14':
            print("79,900")
        elif MONI == '16':
            print("94,900")
        else:
            print("unavailable ")
    else:
        print("unavailable ")
else :
    print("unavailable")
