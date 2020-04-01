import random
import math

# Write a method rand divis 3 that takes no parameters, generates and prints a random number, and finally
# returns True if the randomly generated number is divisible by 3, and False otherwise. For this method we’ll
# use a new module, the random module. At the top of your code, underneath import math, add the line
# import random. We’ll use this module to generate a random integer using the function randint, which works
# as follows:
# random.randint(lo, hi)
# where lo and hi are integers that tell the code the range in which to generate a random integer (this range
# is inclusive). 0 to 100 is probably a decent range.
def rand_divis_3():
    r_num = random.randint(0,100)
    if r_num % 3 == 0:
        return True
    else:
        return False

# Write a method roll dice that takes in 2 parameters - the number of sides of the die, and the number of dice
# to roll - and generates random roll values for each die rolled. Print out each roll and then return the string
# “That’s all!” An example output:
# >>> roll_dice(6, 3)
# 4
# 1
# 6
# That’s all!
def roll_dice(dice_sides,dice_roll):
    
    for i in range(dice_roll):
        print(random.randint(0,dice_sides))

    print("That’s all!")
    

if __name__ == "__main__":
    
    print(rand_divis_3())

    roll_dice(6,3)
   