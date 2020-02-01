def main():
    from sys import argv
    script, filename = argv

    latin = open(filename)

    count_ln = 0

    line = latin.readline()

    while line:
        count_ln += 1
        line = latin.readline()
        print(count_ln)





main()
#print total lines and total characters
