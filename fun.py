# funkcja - wydzielona częś cprogrmu, która może być wykonana wielokrotnie

a = 4
b = 8


# definicja funkcji
def dodaj():
    print(a + b)


def dodaj2(a, b):
    print(a + b)


# nadanie wartosci domyslnej argumentow c=0
def odejmij(a, b, c=0):
    print(a - b - c)


# wywołanie funkcji
dodaj()
dodaj2(6, 7)
odejmij(8, 9)
odejmij(9, 9, 5)

# podanie argumentów po nazwie
odejmij(4, c=6, b=8)

print(dodaj())  # None
# te funkcje nie zwracają wyniku do głownego programu

# print(dodaj() + dodaj2(3, 5))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# 11:25
