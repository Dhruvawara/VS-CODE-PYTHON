MIN_KEY_SIZE = 32
MAX_KEY_SIZE = 126
MENU = True

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


def caeserEncrypt(plainText, key):
    Text = []

    for pT in range(len(plainText)):
        uniCode = ord(plainText[pT])
        code = uniCode + key

        if code > MAX_KEY_SIZE:
            code = 31 + (code - MAX_KEY_SIZE)
            Text.append(chr(code))
        else:
            Text.append(chr(code))
    return Text


def ceaserDecrypt(cipherText, key):
    Text = []

    for cT in range(len(cipherText)):
        uniCode = ord(cipherText[cT])
        code = uniCode - key

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
            key = int(input("Key : "))

            if key < 0 or key > 94:
                5/0
            break
        except:
            print("Enter a valid input")
    return key


while MENU:
    print("\n\nMenu Boi of Caeser Cipher Program\nSelect a number(Option)")
    print("1 -> ENCRYPT\n2 -> DECRYPT\n3 -> EXIT")

    menuOption = getMenuOptionData()

    if menuOption == 3:
        MENU = False
    elif menuOption == 1:
        key = getKeyInput()
        Text = getTextInput()
        print(end="Encrypted Text : ")
        eText = caeserEncrypt(Text, key)

        for e in range(len(eText)):
            print(end=""+eText[e])
    elif menuOption == 2:
        key = getKeyInput()
        Text = getTextInput()
        print(end="Decrypted Text : ")
        dText = ceaserDecrypt(Text, key)

        for d in range(len(dText)):
            print(end=""+dText[d])
else:
    print("Thanks for using")
