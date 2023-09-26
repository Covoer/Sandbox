filename = input("File:")

in_file = open(filename,'r')
for line in in_file:
    if line[0] == "#":
        print(line)
in_file.close()

