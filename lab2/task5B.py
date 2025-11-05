with open("notowania_gieldowe.txt", "a") as file:
    file.write("\nALR, 113")

with open("notowania_gieldowe.txt", "r") as file:
    print(file.read())