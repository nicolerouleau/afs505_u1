# uses argv to get a filename 2-4
from sys import argv

script, filename = argv

# opens file ^^ from argv
txt = open(filename)

# prints message of which file is out
print(f"Here's your file {filename}:")
# prints message of txt file (reads file)
print(txt.read())

# simply prints phrase
print("Type the filename again:")
# instructs human to enter something here
# (preferably the file name) so that is correlates
file_again = input("> ")

# opens file
txt_again = open(file_again)

# reads above file
print(txt_again.read())

# closes files
txt.close()

txt_again.close()
