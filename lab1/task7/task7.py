a = int(input("number a: "))
b = int(input("number b: "))

print(f"{a}x + {b} = 0")
print(f"{a}x = {-b}")
b /= a
a /= a
if a < 0:
    a = -a
    b = -b
print(f"x = {-b:.2}")
