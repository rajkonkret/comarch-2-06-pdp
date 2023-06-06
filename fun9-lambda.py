# lambda - skrócony zapis funkcji

odejmij = lambda a, b: a - b  # labda domyslnie zwraca wynik (return)
print(odejmij(5, 4))

# def odejmij(a, b):
#     return a - b

oblicz_vat = lambda cena, vat=7: cena * (100 + vat) / 100
print(oblicz_vat(1000, 23))
print(oblicz_vat(1000))  # 1070.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")

print(wiek(9))
print(wiek(15))
print(wiek(25))

lista = [1, 2, 3, 8, 10, 23, 50]
# map() - mapuje kolejne elementy kolekcji wg wzorca
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")  # Zastosowanie map: [2, 4, 6, 16, 20, 46, 100]

# filter - zwraca elementy spełniające przekazany warunek
print(f"Zastosowanie filter: {list(filter(lambda x: x < 3, lista))}")  # Zastosowanie filter: [1, 2]
# wieksze od 8
print(f"Zastosowanie filter: {list(filter(lambda x: x > 8, lista))}")  # Zastosowanie filter: [10, 23, 50]
# wieksze od 3, mniejsze od 20
print(f"Zastosowanie filter: {list(filter(lambda x: 3 < x < 20, lista))}")  # Zastosowanie filter: [8, 10]
# x > 3 and x < 20 oznacza 3 < x < 20
# 13:20
