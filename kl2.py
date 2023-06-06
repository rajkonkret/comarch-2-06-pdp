class Human:
    """
    klasa Human opisująca człowieka w Pythonie
    """

    # konstruktor
    def __init__(self, imie, wiek, wzrost, plec="k"):
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print("Nazywam się", self.imie)

    def moj_wiek(self):
        self.powitanie()
        print("Nazywam się", self.imie, "Mam", self.wiek, "lat")

    def moj_wzrost(self):
        print("Nazywam się", self.imie, "Mam", self.wzros, "cm wzrostu")

    def ruszaj(self):
        if self.plec == "m":
            print("Ruszyłem")
        else:
            print("Ryszyłam")


cz1 = Human("Radek", "48", "180", "m")
cz1.powitanie()  # Nazywam się Radek
cz1.moj_wiek()
cz1.ruszaj()
cz2 = Human("Gienia", 34, 190)
cz2.moj_wiek()
cz2.ruszaj()
