# set - przechowuje niezduplikowane elementy

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
# nie pamieta kolejnosci

print(lista)  # [44, 55, 66, 777, 33, 22, 11, 33, 11]

zb2 = set()  # tworzymy pusty zbior
print(zb2)  # set()
zbior.add(33)
print(zbior)
zbior.add(18)
print(zbior)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

print(zbior.pop())  # 33
print(zbior.pop())  # 66
print(zbior.pop())  # 777
print(zbior.pop())  # 11
print(zbior)  # {44, 18, 22, 55}

zbior.remove(55)
print(zbior)
zbior.remove(18)
print(zbior)  # {44, 22}

lista2 = list(zbior)  # zamiana na liste
print(lista2)  # [44, 22]
print(type(lista2))  # <class 'list'>

zbior2 = {66, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)  # {66, 18, 52, 999, 11, 44, 62}

print(zbior | zbior2)  # {66, 999, 11, 44, 18, 52, 22, 62} - suma
print(zbior & zbior2)  # {44} - część wspolna
print(zbior - zbior2)  # {22} - różnica

print(zbior.difference(zbior2))  # {22}

print(zbior2.difference(zbior))  # {66, 999, 11, 18, 52, 62}

print(zbior2 - zbior)  # {66, 999, 11, 18, 52, 62}
