"""
# Python Practice

# Define a variable:
Name = "Muhammad Ahsan"
age = 27

# Check the type of variable by using type function:
print (type(Name))

# isinstance function id used to check the data type of instance in True or False result
print (isinstance(Name, str))
print (isinstance(age, int))
print (isinstance(age, float))

# Convert the variable instances as per your requirements
_number = 98
print(type(_number))

_num = 90
_cs = str(_num)
print (isinstance(_cs, str))

# Operators Learning:

print (2 + 5) # Addition
print (2 - 5) # Subtraction
print (9 / 5) # Float Division
print (5 * 4) # Multiplication
print (4 ** 6) # Power / Square of the value
print (9 // 5) # Integer Division

# String Concatenation (+ operator is used to combine two strings)
print ("Muhammad " + "Ahsan")

# * operator convert the single string into no of time of value
print ("Muhammad Ahsan " * 5)

# Values concatenation
age = 8
age += 8 # it add 8 more into the age values (age = age + 8)
print(age)

age = 27
age *= 5 # it can multiply the age value by 5
print (age)

# Comparison Operators
a = 54
b = 46
print (a < b)
print (a > b)
print (a >= b)
print (a <= b)
print (a != b)
print (a == b)

# Boolean Operators
_Condition = True
_Condition2 = False

print (_Condition and _Condition2)

print (_Condition or _Condition2)

not _Condition
"""


"""
# and operator function, If and operator found false value as first then it will return first value. If and founds true value as first then it will returm second value

print (0 and 1) # retunrs 0
print (1 and 0) # retunr 0
print (3 and 5) # return 5 because adn founds first value as true so it will return 5 second value

# or operator function, If or operator found true value as first then it will return first value. If or founds false value as first then it will returm second value
print (1 or 0) # return 1
print (0 or 1) # return 1
print (0 or 0) # return 0

"""

"""
# Operators with symbols
& performs Binary AND
| performs BInary OR
^ performs a Binary XOR operation
~ performs a Binary NOT operation
<< Shift left operation
>> Shift right operation

"""

"""
# is operator used to compare the identity of both objects if both are true it returns True
a = 3
b = a
# a = 4 # uncomment this code to check its behaviour
print (a is b)

# in operator is used to chcek the membership of the object in list loof or sequence of string

food = ["apple", "banana", "strawberry"]
# print ("orange" in food) 
print ("apple" in food)

# Ternary Operator
def is_adult(age):
    if age > 18:
        return True
    else:
        return False

# we using this instead of above function:
def is_adult2(age):
    return True if age > 18 else False

"""

# String

Name = "Muhammad"

# My_Name = Name + " Ahsan"
# print (My_Name)

# OR Anotherway is
Name += " Ahsan"
print (Name)

# Multiline String use 3 double quotes at the beginning and end of the strings

print ("""Muhammad

Ahsan 

Hamza

Farooqi """)

# Upper method is used to convert all letters into upper case
print ("Muhammad Ahsan".upper())

# Lower method is used to convert all letters into lower case
print ("MUHAMMAD AHSAN".lower())

# Title method is used to first letter of each word into CApital
print ("MUHAMMAD AHSAN".title())

# Session need to start from 01:13:56 for further learning and implementation