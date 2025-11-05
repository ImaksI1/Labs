litera = str(input("podaj literę: "))

if litera.isalpha() and len(litera) == 1:
    if litera.isupper():
        print("litera jest duża")
    else:
        print("litera jest mała")
else:
    print("to nie jest 1 litera")