# Operators-  + - & / % ** //
# Comparison Operators > < == != >= <=
# Identity Operators is, isnot
# & - and | - or  
# List [] Tupple () like list, but faster; cannot be modified. Dictionary {}
# Dir(function) - in python termianl for help

import datetime

mynow = datetime.datetime.now()
print("Current date:", mynow)

from statistics import mean

print ("Input single digit numbers =<9. Example: 145157")
a = [int(x) for x in input()]
grades = a
list_avg = mean(grades)
length = len(grades)
print ("This is the average:", list_avg)
print ("There are", length, "numbers in the string.")

# Dictionary (key:value)
dictionary = {"Emma":1, "John":2, "Robert":3}
print(dictionary.values(),dictionary.keys())

# Index object[x] starts from 0; can be negative starting from -1. Slice with : .Can chain index strings with [x][y]
dogs = ["Blue", "Yellow", "Green"]
print("Dogs are ",dogs[-3:])

# Define own function with def name(parameter):
def funct(value):

    # For conditionals if condition: else: condition
    if type(value) == dict:
        the_funct = sum(value.values()) / len(value)
    else:
        the_funct = sum(value) / len(value)

    return the_funct

testdict = {1,5,7,9}
testlist = [1,5,7,9,50]

print("List average", funct(testlist), "Dictionary average", funct(testdict))

# elif is another conditional. If criteria is matched then .. in all other cases 'else'
x = 1
y = 5

if x > y:
    print("X is greater than Y")
elif x == y:
    print("X is equal to Y")
else:
    print("X is lesser than Y")

#String formatting. Store msg in variable and use 'f' prefix and {}.
name = input("Hello, what's your name ?")
surname = input("What's your surname ?")
when = mynow
message = f"Hello, {name} {surname}, the time is {when} " 
print(message)

# iterate function to lookup data structure and execute different instructions of for loop 
def iterate(data):
    if type(data) == dict:
        for item in testlist.value():
            print(item)
    else:
        for item in testlist:
            print(item)
    return data
result = iterate('Result')
print(result)
    

# While loop, until condition is satisfied
password = ''
while password != "secret":
    password = input("What's the SECRET password?")

# Another while loop, while true (always) 
while True:
    password2 = input("What's the second SECRET password?")
    if password2 == "secret2":
        break
    else:
        continue

