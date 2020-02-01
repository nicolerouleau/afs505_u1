from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# opens to_file and makes it writable while opening the from_file to read from
(open(to_file, 'w').write(open(from_file).read()))

print(f"The input file is {len(from_file)} bytes long")

# only need line 2 for line 14 below 
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()


print("Alright, all done.")

 # because i didnt got rid of all the extra out_file, indata, in_file
 # there are no files to close,the program closes the from_file and to_file
