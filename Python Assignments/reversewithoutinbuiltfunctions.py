# Write a program in python to reverse a string without using inbuilt funtion reverse string 

def reversestring(string):
    print(string)
    charlist = list()
    for char in string[::-1]:
        charlist.append(char)
    return "".join(charlist)
    
if __name__ == "__main__":
    print(reversestring("Dhruva"))