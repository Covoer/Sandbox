names = ["Bob","James","Cook"]
position = 1
for name in names:
    with open(f"{name}.txt", "w")as out_file:
        out_file.write(name)
        out_file.write(f"{position}")
        position = position + 1