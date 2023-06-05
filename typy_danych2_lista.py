# lista - kolekcja do przechowywania elementów

lista = []
print(type(lista))  # <class 'list'>
print(lista)  # [] - pusta lista
lista.append("Radek")
lista.append("MAciek")
lista.append("JAcek")
lista.append("Zenek")
print(lista)  # ['Radek', 'MAciek', 'JAcek', 'Zenek']
# indeksy w liscie zaczynają sie od 0
print(lista[0])  # Radek
print(lista[1])  # Maciek
# print(lista[10])  # IndexError: list index out of range
print(lista[-1])  # Zenek
print(lista[-2])  # JAcek

print(len(lista))  # 4 - długość listy

lista[2] = "Mikołaj"  # zamiana pozycji na indeksie 2
print(lista)  # ['Radek', 'MAciek', 'Mikołaj', 'Zenek']

lista.insert(1, "Paweł")
print(lista)  # ['Radek', 'Paweł', 'MAciek', 'Mikołaj', 'Zenek']

lista.remove("MAciek")
print(lista)  # ['Radek', 'Paweł', 'Mikołaj', 'Zenek']

indeks = lista.index("Zenek")
print(lista.pop(indeks))  # Zenek

lista_copy = lista.copy()  # ['Radek', 'Paweł', 'Mikołaj']
print(lista_copy)

lc2 = lista
print(lc2)  # ['Radek', 'Paweł', 'Mikołaj']

a = 3
b = a
lista.clear()  # usuniecie calłj listy
print(lista)  # []
print(lc2)  # []

print("Radek" in lista_copy)  # True

liczby = [54, 999, 34, 22, 12.34, 687]
print(liczby)
liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 687, 999]

lista2 = ["radek", "ola"]
lista2.sort()
print(lista2)  # ['ola', 'radek']

liczby.reverse()
print(liczby)  # [999, 687, 54, 34, 22, 12.34]

liczby[3] = 6666
print(liczby)  # [999, 687, 54, 6666, 22, 12.34]

print(liczby[0:3])  # [999, 687, 54] od 0..2
print(liczby[-2])
print(liczby[:-2])  # [999, 687, 54, 6666] od 0 .. -3 (-2 juz nie drukuje)
print(liczby[2:])  # [54, 6666, 22, 12.34] wydrukuje włacznie z ostatnim
# 13:30

liczby.remove(54)
print(liczby)
print(len(liczby))  # 5

krotka = tuple(liczby)
print(krotka)  # (999, 687, 6666, 22, 12.34)
print(type(krotka))  # <class 'tuple'>

