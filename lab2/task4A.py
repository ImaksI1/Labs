gol = int(input("podaj liczbę zdobytych goli: "))

wynik = gol * 10

if gol > 10:
    bonus = 10
elif gol > 5:
    bonus = 5
else:
    bonus = 0

wynik_calkowity = wynik + bonus
print(f"wynik całkowity: {wynik_calkowity}")