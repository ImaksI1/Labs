x = int(input("Podaj liczbę x: "))
y = int(input("Podaj liczbę y: "))
z = int(input("Podaj liczbę z: "))

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

print(f"Liczby w kolejności rosnącej: {x}, {y}, {z}")