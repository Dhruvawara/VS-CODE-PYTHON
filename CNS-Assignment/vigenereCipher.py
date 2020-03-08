MIN_KEY_SIZE = 32
MAX_KEY_SIZE = 126
MENU = True
ASCII_VALUE = {}
alphabet = 32
for value in range(94):
    ASCII_VALUE[chr(alphabet)] = value
    alphabet += 1

# print(chr(65))
# print(ord('A'))

def getMenuOptionData():
    while True:
        try:
            op = int(input("Option : "))

            if op < 1 or op > 3:
                5/0
            break
        except:
            print("Enter a valid input")
    return op


def vigenereEncrypt(plainText, key):
    Text = []
    k=0

    for pT in range(len(plainText)):
        uniCode = ord(plainText[pT])
        if(k == len(key)):
            k = 0
        code = uniCode + ASCII_VALUE.get(key[k])
        k+=1

        if code > MAX_KEY_SIZE:
            code = 31 + (code - MAX_KEY_SIZE)
            Text.append(chr(code))
        else:
            Text.append(chr(code))
    return Text


def vigenereDecrypt(cipherText, key):
    Text = []
    k=0

    for cT in range(len(cipherText)):
        uniCode = ord(cipherText[cT])
        if(k == len(key)):
            k = 0
        code = uniCode - ASCII_VALUE.get(key[k])
        k+=1
        if code < MIN_KEY_SIZE:
            code = 127 - (MIN_KEY_SIZE - code)
            Text.append(chr(code))
        else:
            Text.append(chr(code))
    return Text


def getTextInput():

    while True:

        try:
            Text = input("Text : ")

            for t in range(len(Text)):
                if ord(Text[t]) < MIN_KEY_SIZE or ord(Text[t]) > MAX_KEY_SIZE:
                    5/0
            else:
                print("Input Text : ", Text)
            break
        except:
            print("Enter a valid input")
    return Text


def getKeyInput():

    while True:

        try:
            key = input("Key : ")
            
            for k in range(len(key)):
                if ord(key[k]) < MIN_KEY_SIZE or ord(key[k]) > MAX_KEY_SIZE:
                    5/0
            else:
                print("Input Text : ", key)
            break

        except:
            print("Enter a valid input")
    return key


while MENU:
    print("\n\nMenu Boi of Vigenere Cipher Program\nSelect a number(Option)")
    print("1 -> ENCRYPT\n2 -> DECRYPT\n3 -> EXIT")

    menuOption = getMenuOptionData()

    if menuOption == 3:
        MENU = False
    elif menuOption == 1:
        key = getKeyInput()
        Text = getTextInput()
        print(end="Encrypted Text : ")
        eText = vigenereEncrypt(Text, key)

        for e in range(len(eText)):
            print(end=""+eText[e])
    elif menuOption == 2:
        key = getKeyInput()
        Text = getTextInput()
        print(end="Decrypted Text : ")
        dText = vigenereDecrypt(Text, key)

        for d in range(len(dText)):
            print(end=""+dText[d])
else:
    print("Thanks for using")
