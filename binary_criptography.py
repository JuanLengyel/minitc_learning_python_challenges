def binaryDecrypt(toDecrypt):
    res = ''

    charList = [toDecrypt[0: len(toDecrypt)- 1][i:i + 8] for i in range(0, len(toDecrypt), 8)]

    for char in charList:
        try:
            res += str(chr(int(char, 2)))
        except Exception:
            res = res

    return res

def binaryEncrypt(toEncrypt):
    res = ''

    for letter in toEncrypt:
        res += str(bin(ord(letter)))[2:].zfill(8)
    
    return res

def run():
    print("Binary encription\n")
    while True:
        print(
            '''
            [e]ncript
            [d]ecript
            [f]inish
            ''')

        cmd = str(raw_input("Input the desired command: "))[0]

        if (cmd == 'e'):
            stringToEncrypt = str(raw_input("Sequence to encrypt: "))
            print(binaryEncrypt(stringToEncrypt))
        elif (cmd == 'd'):
            stringToDecrypt = str(raw_input("Sequence to decrypt: "))
            print(binaryDecrypt(stringToDecrypt))
        elif (cmd == 'f'):
            return 0
        else :
            print("Couldn\'t understand that command")

if __name__ == "__main__":
    run()