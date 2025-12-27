import random

dystans = random.randint(50, 500)
print(f"Dystans: {dystans} km")

spalanie = float(input("Średnie spalanie (l/100 km): "))
cena_paliwa = float(input("Cena paliwa za litr: "))

zuzycie_paliwa = (dystans / 100) * spalanie
koszt = zuzycie_paliwa * cena_paliwa

print(f"\nDystans: {dystans} km")
print(f"Spalanie: {spalanie:.2f} l/100 km")
print(f"Zużycie paliwa: {zuzycie_paliwa:.2f} l")
print(f"Koszt podróży: {koszt:.2f} PLN")
