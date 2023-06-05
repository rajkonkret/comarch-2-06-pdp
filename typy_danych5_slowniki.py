# slownik - para klucz, wartosc = {'name' : 'Radek'}

dict = {}  # pusty słownik
print(type(dict))  # {}
print(dict)  # <class 'dict'>

dict['imie'] = 'Radek'
print(dict)  # {'imie': 'Radek'}
dict['wiek'] = 39
print(dict)  # {'imie': 'Radek', 'wiek': 39}

print(dict.keys())  # wyswietla klucze dict_keys(['imie', 'wiek'])
print(dict.values())  # wyswietla wartosci dict_values(['Radek', 39])
print(dict.items())  # wyswietla pary, dict_items([('imie', 'Radek'), ('wiek', 39)])

dict.update({'date': '12-12-2023'})
print(dict)  # {'imie': 'Radek', 'wiek': 39, 'date': '12-12-2023'}

dictionary = {'x': 2}
print(dictionary)  # {'x': 2}
dictionary.update([('y', 3), ('z', 0)])  # przekazanie poprzez liste krotek
print(dictionary)  # {'x': 2, 'y': 3, 'z': 0}

dict2 = {'imie': 'name', 'kot': 'cat'}
print(dict2['imie'])  # name

print("Mamy w słowniku", dict2.keys())  # Mamy w słowniku dict_keys(['imie', 'kot'])
key = input("Podaj słowo do przetłumaczenia")  # input - pobierz dane od uzytkownika
# input zwraca typ str
print(dict2[key.lower().replace(" ", "")])

a = int(input("podaj pierwsza liczbe"))
b = int(input("podaj drugą liczbe"))
print(a + b)
