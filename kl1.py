# klasy
# klasa - szablon
# obiekt - wypełniony szablon

class Human:
    """
    klasa opisujaca człowieka
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def podaj_wiek(self):
        print("Mam", self.wiek, "lat")


print(Human.__doc__)  # klasa opisujaca człowieka
print(print.__doc__)
cz1 = Human()  # obiekt klasy Human
print(cz1)  # <__main__.Human object at 0x104bbe510>
print(cz1.__doc__)
print(cz1.plec)  # k
print(cz1.imie)
cz1.imie = "Radek"
cz1.wiek = 49
print(cz1.imie)
print(cz1.wiek)
cz1.plec = "m"
cz1.powitanie()
# stworzyc drugiego człowieka, nadac mu cechy
cz1.podaj_wiek()
cz2 = Human()
cz2.imie = "Marysia"
cz2.powitanie()
