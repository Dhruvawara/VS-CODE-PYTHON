# Write a Python program to find the first duplicate element in a 
# given array of integers. Return -1 If there are no such elements

def firstduplicate(arraynum):
    num_set = set()

    for i in range(len(arraynum)):

        if arraynum[i] in num_set:
            return arraynum[i]
        else:
            num_set.add(arraynum[i])

    return -1

if __name__ == "__main__":
    print(firstduplicate([1,2,3,4,5,6,3]))