teksty = "Witaj świecie"
print(teksty)

""" Return a copy of the string converted to uppercase. """
tekst2 = teksty.upper()  # upper() - zamian na duże litery ale w kopii
print(teksty)  # Witaj świecie
print(tekst2)  # WITAJ ŚWIECIE

print(tekst2.lower())  # wypisze tekst małymi literami ale w zmiennej tekst2 ndal bedzie dużymi

print(teksty.removeprefix("Witaj"))  # usuniecie wyrazu na poczatku
print(teksty.removesuffix("świecie"))  # "Witaj "
print(teksty)  # Witaj świecie
liczba = 39
print(39)

encoded_s = teksty.encode('utf-8')  # zakodowanie znaków jako utf-8
print(encoded_s)  # b'Witaj \xc5\x9bwiecie' - zapamietane binarnie

tekst_bajtowy = b"To jest tekst bajtowy"
print(tekst_bajtowy)  # b'To jest tekst bajtowy'
print(type(tekst_bajtowy))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie

print(teksty.count("i"))
print(teksty.count("i", 0, 4))  # ile razy wystepuje "i" w czterech pierwszych znakach wyrazu

imie = "Radek"
tekst_format = f"Mam\t na imie {imie}\n i lubię Pythona"  # fstring - sformtowany string
print(tekst_format)

starszy = "Witaj %s"  # %s w to miejsce mozemy wstawic wartos zmiennej, s - str
print(starszy % imie)  # Witaj Radek
print("Witaj {}!".format(imie))  # Witaj Radek!

print("""
Tekst wielolinijkowy
\ttabulator
    tabulator jawnie
    nowa linia
    """)
print("Tekst \bdalej")  # Tekstdalej
print("Witaj {} {{}} ".format(imie))  # Witaj Radek {}
# 11:30
