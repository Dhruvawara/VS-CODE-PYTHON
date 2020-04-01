# Write a funtion in python which detects whether the given two strings are anagrams or not


def detect_anagram(string1, string2):
    print(string1 + " | " + string2)
    s1 = [i for i in string1 if ord(i) != 32]
    s2 = [i for i in string2 if ord(i) != 32]
    s1.sort()
    s2.sort()
    if len(s1) == len(s2):
        for index in range(len(s1)):
            if s1[index] != s2[index]:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    print(detect_anagram("rail safety", "fairy tales"))
