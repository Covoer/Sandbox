def load_number(filename):
    try:
        infile = open(filename,"r")
        number = int(infile.read())
    except ValueError:
        print(f"Invalid contents in{filename}")
        number = 6
    except FileNotFoundError:
        print(f"{filename} not found")
        number = 4
    else:
        infile.close()
    return number
def main():
    load_number(input("File name: ")
main()