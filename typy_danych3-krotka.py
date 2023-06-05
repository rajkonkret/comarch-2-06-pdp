# krotka, tupla - niemutowalna, niemodyfikowalna
# zmienna, niezmienna
tupla = ("Radek",)  # tupla jednolelementowa
print(type(tupla))  # <class 'tuple'>

tupla2 = ("Tomek", "Asia", "Marek", "Paulina",)
print(type(tupla2))  # <class 'tuple'>

tupla3 = (43, 55, 22.34, 11, 200)
print(type(tupla3))  # <class 'tuple'>

print(tupla2.count("Tomek"))
print(tupla2.index("Tomek"))  # 0 - indeksowanie od zera

a, b = 1, 2
print(a)
print(b)
a, b = b, a
print(a, b)  # 2 1

tp = 1, 2, 3
print(tp)
print(type(tp))

# a, b = tp  # ValueError: too many values to unpack (expected 2)
*a, b = 1, 2, 3  # * worek na pozostałę dane
print(a, b)  # [1, 2] 3

a, *b = 1, 2, 3
print(a, b)  # 1 [2, 3]

imie1, *imie2, imie3 = tupla2
print(imie1, imie2, imie3)  # Tomek ['Asia', 'Marek'] Paulina
# rozpakowanie tupli


lista = list(tupla2)
print(lista)  # ['Tomek', 'Asia', 'Marek', 'Paulina']
print(type(lista))  # <class 'list'>
