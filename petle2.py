dictonary = {'imie': 'Radek', 'nazwisko': 'Kowalski'}

print(dictonary)
print(type(dictonary))  # <class 'dict'>

# zwraca klucze
for k in dictonary:
    print(k)

for k in dictonary.keys():
    print(k)

# imie
# nazwisko
# imie
# nazwisko

# zwraca wartosci
for v in dictonary.values():
    print(v)

# zwraca pary klucz : wartosc
for k, v in dictonary.items():
    print(k, "=>", v)  # nazwisko => Kowalski

dict1 = {'name': 'imie', 'company': 'Comarch'}
# zbuduje słownik z zamienionymi miejscami dla klucz : wartosc
# klucz, wartosc = wartosc, klucz
print({value: key for key, value in dict1.items()})
# {'imie': 'name', 'Comarch': 'company'}
