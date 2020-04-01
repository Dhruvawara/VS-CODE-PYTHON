# Write a program to calculate number of upper case letters and number of lower case letters?

def noofupperandlower(String):
    print(String)
    upper = 0
    lower = 0
    for char in String:
        if ord(char) in range(65,91):
            upper += 1
        elif ord(char) in range(97,123):
            lower += 1
    print("UPPER : ", upper,"| LOWER : ", lower)
        

if __name__ == "__main__":
    noofupperandlower("AbcDsdBasB")