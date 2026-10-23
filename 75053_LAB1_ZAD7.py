
print("Zadanie 7.0")
print("Obliczanie x z równania liniowego")
while True:
    try:
        a = float(input("Podaj wartość dla a: "))
        break
    except ValueError:
        print("Błąd danych. Popraw dane:")

while True:
    try:
        b = float(input("Podaj wartość dla b: "))
        break
    except ValueError:
        print("Błąd danych. Popraw dane:")

if a == 0 and b == 0:
    print("Równanie ma nieskończenie wiele rozwiązań")
elif a == 0 and b != 0:
    print("Równanie nie ma rozwiązań")
else:
    wynik = -b / a
    print(f"Dla tego równania liniowego x jest równy: {wynik}")




