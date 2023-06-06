# funkcja zwracająca wynik

def dodaj(a, b):
    return a + b  # odeslij wynik


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(6, 7))
print(dodaj(dodaj(4, 5), 6))
print(oblicz_vat(1000))  # 1230.0 float
print(oblicz_vat(1000, 7))  # 1070.0

zm = oblicz_vat(1000)  # float
if zm == 1230:
    print("Prawidłowo")
