gol = int(input("podaj liczbę zdobytych goli: "))

wynik = gol * 10

bonus = 0
if gol > 10:
    bonus += 10
if gol > 5:
    bonus += 5

wynik_calkowity = wynik + bonus
print(f"wynik całkowity: {wynik_calkowity}")