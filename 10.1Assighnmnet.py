#Eric Hayden 05/21/2021

import os
import json

found = False
directory=None

while not found:
    directory = str(input("Enter full path of the Directory: "))
    print (directory)
    if not os.path.isdir(directory):
        print(directory, 'This Directory has not been found. Enter correct path. ')
    else:
        print("Directory path is correct!")
        found = True

name = input("Please enter your name: ")
adress = input("Please enter your adress: ")
number = input("Please enter your phone number: ")

info = [name, adress, number]

path = directory

filename = 'info.json'
with open(os.path.join(name + '.json'), 'w') as f:
    json.dump(info, f)

print(info)
print("This file was saved successfully!")