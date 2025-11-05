liczba_punktow = int(input("liczba punktów: "))

if liczba_punktow > 80:
    print("egzamin zaliczony w terminie 0")
elif liczba_punktow > 50 and liczba_punktow < 80:
    print("możesz poprawić")
else:
    print("musisz poprawić")