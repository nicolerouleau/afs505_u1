from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")

example = open(filename, 'w')

example.truncate()

print("Now fill in these 3 lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

all_lines = "%s\n%s\n%s\n" % (line1, line2, line3)
example.write(all_lines)

example.close()
