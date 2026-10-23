
print("Zadanie 9.0")
print("Prosty kalkulator:")
while True:
    try:
        a = float(input("Podaj 1 liczbę: "))
        break
    except ValueError:
        print("Błąd danych. Popraw dane:")

while True:
    try:
        b = float(input("Podaj 2 liczbę: "))
        break
    except ValueError:
        print("Błąd danych. Popraw dane:")

print(f"Wyniki są następujące\nDodawanie: {a+b}\nOdejmowanie przy założeniu a-b: {a-b}\nOdejmowanie przy założeniu b-a: {b-a}\nMnożenie: {a*b}\nDzielenie przy założeniu a/b: {a/b}\nDzielenie przy założeniu b/a: {b/a}\nPotęgowanie przy założeniu a^b: {pow(a,b)}\nPotęgowanie przy założeniu b^a: {pow(b,a)}")


