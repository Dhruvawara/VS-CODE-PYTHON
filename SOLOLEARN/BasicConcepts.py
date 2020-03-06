# FRIST PROGRAM

print("Hello World")
# Hello World
print('Hello World')
# Hello World


# SIMPLE OPERATIONS

print(2 + 2)
# 4
print(5 + 4)
# 6
print(2 * (3 + 4))
# 14
print(10 / 2)
# 5.0
print(-8)
# -8
print((-5 + 2) * (-4))
# 12
# print(11/0)
# Traceback (most recent call last):
#   File "c:/V S PYTHON/SOLOLEARN/Basic Concepts/BasicConcepts.py", line 23, in <module>
#     print(11/0)
# ZeroDivisionError: division by zero


# FLOAT

print(3 / 4)
# 0.75
print(9.8765000)
# 9.8765000
print(8 / 2)
# 4.0
print(6 * 7.0)  # MULTIPLICATION
# 42.0
print(4 + 1.35)  # ADDITION
# 5.35
print(10 / 3)   # DIVISION
# 3.3333333333333335


# OTHER NUMERICAL OPERATIONS

print(2 ** 5)   # POWER OR EXPONENT
# 32
print(9 ** (10 / 3))
# 1516.3811070048387
print(10 // 3)  # FLOOR DIVISION OR QUOTIENT
# 3
print(1.25 % 0.5)
# 0.25


# STRINGS : CAN"T BE CONCATINATED WITH A INT USING '+' OPERATOR

print("Python " + "is", 'fun')  # ',' puts a space and concatinates
# Python is fun
print("Dhruva\'s Book\'s")  # String Escape
# Dhruva's Book's
print("""\
Line 1
Line 2
Line 3
""")  # the '\' deletes the line only works at begining
# Line 1
# Line 2
# Line 3
#
print("abc" * 3)    # Sting multiplication
# abcabcabc


# SIMPLE INPUT OUTPUT

print("You Entered : ", input("Enter some Character : "))
# Enter some Character : abc
# You Entered :  abc


# TYPE CONVERSION

print(str(5))   # To convert to string
# 5
print(int("5645"))  # To convert to integer
# 5645
print(float("123.2343211"))  # To convert to float
# 123.2343211


# VARIABLES

a = 0   # Single initialization
b, c = "Dhruva ", 1 # Multiple initialization
print(a, b, c)
# 0 Dhruva  1


# OPERATORS

# Arithmetic Operators
# + (ADDITION) : Adds values on either side of the operator.
# - (SUBTRACTION) : Subtracts right hand operand from left hand operand.
# / (DIVISION) : Divides left hand operand by right hand operand
# * (MULTIPLICATION) : Multiplies values on either side of the operator
# % (MODULUS) : Divides left hand operand by right hand operand and returns remainder
# ** (EXPONENT) : Performs exponential (power) calculation on operators
# // (FLOOR DIVISION) : The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero

# Comparison Operators
# == : If the values of two operands are equal, then the condition becomes true.
# != : If values of two operands are not equal, then condition becomes true.
# <> : If values of two operands are not equal, then condition becomes true.
# > : If the value of left operand is greater than the value of right operand, then condition becomes true.
# < : If the value of left operand is less than the value of right operand, then condition becomes true.
# >= : If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.
# <= : If the value of left operand is less than or equal to the value of right operand, then condition becomes true.

# Assignment Operators
# = : Assigns values from right side operands to left side operand
# += (Add AND) : It adds right operand to the left operand and assign the result to left operand
# -= (Subtract AND) : It subtracts right operand from the left operand and assign the result to left operand
# *= (Multiply AND) : It multiplies right operand with the left operand and assign the result to left operand
# /= (Divide AND) : It divides left operand with the right operand and assign the result to left operand
# %= (Modulus AND) : It takes modulus using two operands and assign the result to left operand
# **= (Exponent AND) : Performs exponential (power) calculation on operators and assign value to the left operand
# //= (Floor Division) : It performs floor division on operators and assign value to the left operand

# Bitwise Operators

# & (Binary AND) : Operator copies a bit to the result if it exists in both operands
# | (Binary OR) : It copies a bit if it exists in either operand.
# ^ (Binary XOR) : It copies the bit if it is set in one operand but not both.
# ~ (Binary Ones Complement) : It is unary and has the effect of 'flipping' bits.
# << (Binary Left Shift) : The left operands value is moved left by the number of bits specified by the right operand.
# >> (Binary Right Shift) : The left operands value is moved right by the number of bits specified by the right operand.

# Logical Operators

# and (Logical AND) : If both the operands are true then condition becomes true.
# or (Logical OR) : If any of the two operands are non-zero then condition becomes true.
# not (Logical NOT) : Logical NOT

# Membership Operators

# in	: Evaluates to true if it finds a variable in the specified sequence and false otherwise.
# not in	: Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.

# Identity Operators
# is : Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
# is not : Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.

# Operators Precedence

# 1	
# **
# Exponentiation (raise to the power)

# 2	
# ~ + -
# Complement, unary plus and minus (method names for the last two are +@ and -@)

# 3	
# * / % //
# Multiply, divide, modulo and floor division

# 4	
# + -
# Addition and subtraction

# 5	
# >> <<
# Right and left bitwise shift

# 6	
# &
# Bitwise 'AND'

# 7	
# ^ |
# Bitwise exclusive `OR' and regular `OR'

# 8	
# <= < > >=
# Comparison operators

# 9	
# <> == !=
# Equality operators

# 10	
# = %= /= //= -= += *= **=
# Assignment operators

# 11	
# is is not
# Identity operators

# 12	
# in not in
# Membership operators

# 13	
# not or and
# Logical operators