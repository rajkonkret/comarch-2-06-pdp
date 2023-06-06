# while - sterowana warunkiem

licznik = 0
while True:
    licznik += 1  # licznik = licznik + 1
    print("komunikat")
    if licznik > 10:
        break  # przerwie działanie pętli

print(licznik)  # 11
licznik = 0
while licznik < 10:
    print("Komunikat!")
    licznik += 1

lista = []
lista2 = []

while True:
    wej = input("Podaj liczbę")  # zwraca str
    if not wej.isnumeric():
        break
    lista.append(wej)  # ['1', '2', '3']
    lista2.append(int(wej))  # [1, 2, 3, 4, 5, 6]

print(lista)
print(lista2)
