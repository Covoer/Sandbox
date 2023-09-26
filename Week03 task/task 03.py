name = input("Name:")
with open("name.text", "w") as out_file:
    print(name, file=out_file)