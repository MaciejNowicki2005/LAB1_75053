print("Zadanie 1a:")
print("Działanie 1+2 |", type(1 + 2), "| Operator + odpowiada za dodawanie, type() zwraca typ danych int")
print("Działanie 1+4.5 |", type(1 + 4.5), "| Operator + odpowiada za dodawanie, type() zwraca typ danych float")
print("Działanie 3/2 |", type(3 / 2), "| Operator / odpowiada za dzielenie, type() zwraca typ danych float")
print("Działanie 4/2 |", type(4 / 2), "| Operator / odpowiada za dzielenie, type() zwraca typ danych float")
print("Działanie 3//2 |", type(3 // 2), "| Operator // odpowiada za dzielenie całkowite, type() zwraca typ danych int")
print("Działanie -3//2 |", type(-3 // 2), "| Operator // odpowiada za dzielenie całkowite z zaokrągleniem w dół, type() zwraca typ danych int")
print("Działanie 11%2 |", type(11 % 2), "| Operator % odpowiada za resztę z dzielenia, type() zwraca typ danych int")
print("Działanie 2**10 |", type(2 ** 10), "| Operator ** odpowiada za potęgowanie, type() zwraca typ danych int")
print("Działanie 8**(1/3) |", type(8 ** (1/3)), "| Operator ** odpowiada za potęgowanie, a 1/3 oznacza wykładnik ułamkowy, type() zwraca typ danych float")
print("\n\n")#dla czytelności rozwiązania



print("Zadanie 1b:")
print("Instrukcja 'int(3.0)' odpowiada za przypisanie i typu int dla wartości typu float|", "Przed:", 3.0, "|Po:", int(3.0))
print("Instrukcja 'float(3)' odpowiada za przypisanie typu float dla wartości typu int|", "Przed:", 3, "|Po:", float(3))
print("Instrukcja 'float('3')' odpowiada za przypisanie typu float dla wartości typu string |", "Przed:", "3", "|Po:", float("3"))
print("Instrukcja 'str(12.4)' odpowiada za przypisanie wartości typu string dla wartości typu float |", "Przed:", 12.4, "|Po:", str(12.4))
print("Instrukcja 'bool(0)' odpowiada za zmianę liczby 0 na wartości typ bool (TRUE/FALSE)|", "Przed:", 0, "|Po:", bool(0))
print("\n\n")#dla czytelności rozwiązania



print("Zadanie 2:")
uczelnia = "Studiuję na WSIiZ"
print (uczelnia)
print("\n\n")#dla czytelności rozwiązania

print("Zadanie 3:")
imie="Jan"
nazwisko="Kowalski"
wiek=20
wzrost=178
print("Nazwywam się ",imie," i mam ",wiek," lat.\nMój wzrost to",wzrost," cm")
print("\n\n")#dla czytelności rozwiązania


print("Zadanie 4:")
cena=39.99
rabat=0.2
print("Cena po rabacie:",round(cena-cena*rabat,2))
print("\n\n")#dla czytelności rozwiązania

print("Zadanie 5:") #Dla wzbogacenia zadania postanowiłem dodać obdługę wyjątków, tak aby założenia dla wyliczeń boków prostokąta się zgadzały oraz nie było konfliktu wynikającego z błędnego typu zmiennej 

print("Sekcja wyliczania pola i obwodu prostokąta:")
while True:
    try:
        bok_a = float(input("Podaj długość boku a: "))
        if bok_a>0:
            break
        else:
            print("Bok musi być większy od 0!")
    except ValueError:                                              
        print("Nie podano liczby")
        
while True:
    try:
        bok_b = float(input("Podaj długość boku b: "))
        if bok_b >0:
            break
        else:
            print("Bok musi być większy od 0!")
    except ValueError:                                              
        print("Nie podano liczby")

print("Pole twojego prostokata wynosi: ",bok_a*bok_b," | Natomiast jego obwód to: ",(bok_a+bok_b)*2) #Dla czytelności chciałem użyć nawiasów kwadratowych, co ciekawe wynik obwodu wtedy wynosił: [bok_a+bok_b][bok_a+bok_b]
print("\n\n")#dla czytelności rozwiązania


print("Zadanie 6.0")
while True:
    try:
        dlugosc_trasy = float(input("Podaj długość przejechanej trasy w kilometrach: ")) #Tutaj zależnie od ustaleń możnaby użyć float/int,ale chcę aby użytkownik podał jak najdokładniejszą długość trasy. Przypisuję typ żeby uniknąć problemów tak jak w zad.5
        if dlugosc_trasy>0:
            break
        else:
            print("Podaj faktyczną długość trasy...")
    except ValueError:                                              
        print("Nie podano liczby")
dlugosc_trasy=round(dlugosc_trasy,1) #zaokrąglam wartość do setek metrów tak jak się to zazwyczaj robi
while True:
    try:
        spalanie = float(input("Podaj średnie spalanie 'x' na trasie ('x'l/100km): "))  
        if spalanie>0:
            break
        else:
            print("Spalanie musi być większe od 0!")
    except ValueError:                                              
        print("Nie podano liczby")
spalanie=round(spalanie,1) #Odrazu zaokrąglam spalanie, zazwyczaj do obliczeń bierze się dane typu 6.1l/100km, 27.4l/100km itp.
zuzycie=round(dlugosc_trasy/100*spalanie,1)
print("Przewiduję zużycie paliwa na poziomie", zuzycie,"l, a przybliżony koszt podróży to: ",zuzycie*6.5,"zł")
print("\n\n")#dla czytelności rozwiązania


print("Zadanie 6.A")
import random
while True:
    try:
        cena_paliwa = float(input("Podaj aktualną cenę paliwa(za litr):"))
        if cena_paliwa>0:
            break
        else:
            print("Podaj faktyczną cenę...")
    except ValueError:                                              
        print("Nie podano liczby")
cena_paliwa=round(cena_paliwa,2) #zaokrąglam wartość do setek (zabezpieczenie przed danymi typu 7.8323242342323254325434523)
while True:
    try:
        spalanie = float(input("Podaj średnie spalanie 'x' na trasie ('x'l/100km): "))  
        if spalanie>0:
            break
        else:
            print("Spalanie musi być większe od 0!")
    except ValueError:                                              
        print("Nie podano liczby")
spalanie=round(spalanie,1) #Odrazu zaokrąglam spalanie, zazwyczaj do obliczeń bierze się dane typu 6.1l/100km, 27.4l/100km itp.
dlugosc_trasy = random.randint(1,10000) #Zakładam że realnie więcej jak 10000km nikt nie zrobi nawet cięzarówka jadąca przykładowo z Kiruny(Szwecja północ) do Palermo(Włochy południe) (najdłusa trasa 4809km w jedną stronę)
zuzycie=round(dlugosc_trasy/100*spalanie,1)
koszt_podrozy=round(zuzycie*cena_paliwa,2)
print("Przewiduję zużycie paliwa na poziomie", zuzycie,"l, a przybliżony koszt podróży to: ", koszt_podrozy,"zł, przy założeniu że paliwo kosztuje", cena_paliwa,"zł/l a trasa ma długość",dlugosc_trasy,"km")
print("\n\n")#dla czytelności rozwiązania

###################################################################################################################################
#ZADANIE 6.B
###################################################################################################################################

print("Zadanie 6.0.B")
while True:
    try:
        dlugosc_trasy = float(input("Podaj długość przejechanej trasy w kilometrach: ")) 
        if dlugosc_trasy>0:
            break
        else:
            print("Podaj faktyczną długość trasy...")
    except ValueError:                                              
        print("Nie podano liczby")
dlugosc_trasy=round(dlugosc_trasy,1) 
while True:
    try:
        spalanie = float(input("Podaj średnie spalanie 'x' na trasie ('x'l/100km): "))  
        if spalanie>0:
            break
        else:
            print("Spalanie musi być większe od 0!")
    except ValueError:                                              
        print("Nie podano liczby")
spalanie=round(spalanie,1) 
zuzycie=round(dlugosc_trasy/100*spalanie,1)
print(f"Przewiduję zużycie paliwa na poziomie {zuzycie}l, a przybliżony koszt podróży to: {zuzycie*6.5}zł") #ZMIANA NA FSTRING
print("\n\n")


print("Zadanie 6.A.B")
while True:
    try:
        cena_paliwa = float(input("Podaj aktualną cenę paliwa(za litr):"))
        if cena_paliwa>0:
            break
        else:
            print("Podaj faktyczną cenę...")
    except ValueError:                                              
        print("Nie podano liczby")
cena_paliwa=round(cena_paliwa,2) 
while True:
    try:
        spalanie = float(input("Podaj średnie spalanie 'x' na trasie ('x'l/100km): "))  
        if spalanie>0:
            break
        else:
            print("Spalanie musi być większe od 0!")
    except ValueError:                                              
        print("Nie podano liczby")
spalanie=round(spalanie,1) 
dlugosc_trasy = random.randint(1,10000) 
zuzycie=round(dlugosc_trasy/100*spalanie,1)
koszt_podrozy=round(zuzycie*cena_paliwa,2)
print(f"Przewiduję zużycie paliwa na poziomie {zuzycie}l, a przybliżony koszt podróży to: {koszt_podrozy}zł, przy założeniu że paliwo kosztuje {cena_paliwa}zł/l a trasa ma długość {dlugosc_trasy}km") #ZMIANA NA FSTRINGA
print("\n\n")





        




