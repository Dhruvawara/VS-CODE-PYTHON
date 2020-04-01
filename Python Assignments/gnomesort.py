# Write a Python program to sort a list of elements using Gnome sort.
# Gnome sort is a sorting algorithm originally proposed by 
# Dr. Hamid Sarbazi-Azad(Professor of Computer Engineering at 
# Sharif University of Technology) in 2000 and called 
# "stupid sort" (not to be confused with bogosort), and then 
# later on described by Dick Grune and named "gnome sort". The 
# algorithm always finds the first place where two adjacent elements 
# are in the wrong order, and swaps them. It takes advantage of the 
# fact that performing a swap can introduce a new out-oforder adjacent
# pair only next to the two swapped elements

def gnome_sort(a_list):
    print(a_list)
    index = 0
    while index < len(a_list) :
        if index == 0:
            index += 1
        if a_list[index] >= a_list[index - 1]:
            index += 1
        else:
            a_list[index], a_list[index- 1] = a_list[index- 1], a_list[index]
            index -= 1
        
    print(a_list)

if __name__ == "__main__":
    gnome_sort([3,7,3,6,1,8,4])
