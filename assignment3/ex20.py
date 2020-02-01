from sys import argv

script, input_file = argv

# prints whole file
def print_all(f):
    print(f.read())

# seek(0) find the first point in first line
def rewind(f):
    f.seek(0)

# reads the lines of the script and counts them (that's why we see a 1,2,3)
# readline goes through each line 1 by 1
def print_a_line(line_count, f):
    print(line_count, f.readline())

# opens file
current_file = open(input_file)

#\n adds a space inbetween
print("First let's print the whole file: \n")

#uses previously defined print_all and adds in current_file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# rewind goes back to repeat the previous process,
# in this case reading the whole txt file
rewind(current_file)

print("Let's print three lines:")

# tells which lines to print from file (in this case the 1st one)
current_line = 1
print_a_line(current_line, current_file)

# tells which lines to print from txt file (in this case another one from earlier)
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
