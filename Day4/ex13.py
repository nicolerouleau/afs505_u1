# argv stands for argument variables
# imports a package
from sys import argv
# unpacks argv variable
# argv works likes a list
# we want to store the list items in separate variables
# first, second, and third here are string variables
script, first, second, third = argv
# once in separate variables we can print it out
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# when you run the code must name three variables for the code
