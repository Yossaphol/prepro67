"""Khaow"""
def enc(encrypt) :
    """encrypt"""
    text_e = encrypt[:encrypt.find(",")]
    text_n = encrypt[encrypt.find(",")+1:]
    text_result = ''
    for i in text_e :
        if i != " " :
            dec = ord(i)
            dec += int(text_n)
            if dec > 90 :
                dec -= 26
            char = chr(dec)
            text_result += char
        else :
            text_result += " "
    print(text_result)

def decpt(decrypt) :
    """decrypt"""
    text_e = decrypt[:decrypt.find(",")]
    text_n = decrypt[decrypt.find(",")+1:]
    text_result = ''
    for i in text_e :
        if i != " " :
            dec = ord(i)
            dec -= int(text_n)
            if dec < 65 :
                dec += 26
            char = chr(dec)
            text_result += char
        else :
            text_result += " "
    print(text_result)

def main() :
    """def"""
    while True :
        text = input()
        if text == "End" :
            break
        if text == "Encryption" :
            enc(input().upper())
        elif text == "Decryption":
            decpt(input().upper())
        else :
            print("error")
main()
