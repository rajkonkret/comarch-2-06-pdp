# for - petla iteracyjna
import random
from itertools import zip_longest

for i in range(10):  # int 0 .. 9
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # niema zmienna
    print()

for i in range(10):
    print(i * 2)

print(random.randint(1, 6))  # int 1..6
print(random.random())  # float 0 do 0.999999
print(random.random() * 6)  # float od 0 do 5.99999
print(random.randrange(6))  # int 0..5
print(random.randrange(1, 6))  # int 1..5

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))

lista2 = list(range(1, 50))  # od 1 do 49
print(lista2)

for i in range(6):  # 0..5, 0 , 1 ,2 ,3,4,5
    wyn = random.choice(lista2)
    lista2.remove(wyn)
    print(wyn)

print(random.choices(lista2, k=6))  # [18, 7, 42, 30, 4, 39]

for i in range(10):
    if i % 2 == 0:
        print(i, "jest parzysta")
        # jakaslista.append(i)

lista3 = [j for j in range(10) if j % 2 == 0]

print(lista3)  # [0, 2, 4, 6, 8]
for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
    print(c)

imiona = ['Radek', 'Zenek', 'Marta']
print(imiona)

for p in imiona:
    print(p)

# Radek
# Zenek
# Marta
# wyswietlic imiona z tej listy w taki sposob 0 Radek, itd...

for i in range(len(imiona)):
    print(i, imiona[i])

# enumerate - zwraca indeks i element kolekcji
for p, w in enumerate(imiona):
    print(p, "-", w)  # 0 - Radek  p  - indeks w= imiona[p]

for p, w in enumerate(imiona):
    print(p, w, sep=":", end=" ")  # 0:Radek 1:Zenek 2:Marta
    # sep - separator(domyslnie spacja)
    # end - znak końca lini(domyslnie \n - new line)

ludzie = ["Radek", "Zenek", "Asia", "Michał", "Ania"]
wiek = [47, 67, 34, 32]
jezyk = ['java', 'python']
# for p, o in enumerate(ludzie):
#     print(p, o, wiek[p])  # 3 Michał 32

for o, w in zip(ludzie, wiek):
    print(o, w)

# Zenek 67
# Asia 34
# Michał 32

for o, w, j in zip(ludzie, wiek, jezyk):
    print(o, w, j)
# Radek 47 java
# Zenek 67 python
# 0 Radek 47 java

# ValueError: not enough values to unpack (expected 4, got 2)
for i, o in enumerate(zip(ludzie, wiek, jezyk)):
    print(i, o)  # i - indeks, o,w,j = (o,w,j)
# 0 ('Radek', 47, 'java')
# 1 ('Zenek', 67, 'python')

# (o,w,j) - w locie rozpakuje krotke do zmiennych
for i, (o, w, j) in enumerate(zip(ludzie, wiek, jezyk)):
    print(i, o, w, j)  # i - indeks, o,w,j = (o,w,j)
# 0 Radek 47 java
# 1 Zenek 67 python

# zip z biblioteki itertools - łączy kolekcje, może wstawic w brakujące miejsca wskazany element(komunikat)
zipped = zip_longest(ludzie, wiek, jezyk, fillvalue="Nan")

for item in zipped:
    print(item)
# ('Radek', 47, 'java')
# ('Zenek', 67, 'python')
# ('Asia', 34, 'Nan')
# ('Michał', 32, 'Nan')
# ('Ania', 'Nan', 'Nan')

for i in range(0, 10, 2):  # start, stop, krok
    print(i)
