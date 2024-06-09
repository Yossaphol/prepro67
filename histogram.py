"""histogram"""
def histogram(dic):
    """main"""
    dic_key = dic.keys()
    for i in dic_key:
        print(i, "|" * dic[i])

def main(text):
    """main"""
    my_dict = {}
    for i in text:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    histogram(my_dict)
main(input())
