class Dom:
    """
    To jest kalsa dom
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def zmien_metraz(self):
        wybor = int(input("Podaj nowy metraz"))
        self.__metraz = wybor
        print("Metraż wynosi", self.__metraz)

    def zmien_liczba_okien(self):
        wybor = int(input("Podaj nową liczbę okien"))
        self.__liczba_okien = wybor
        self.podaj_liczba_okien()

    def zmien_kolor(self):
        wybor = input("Podaj nowy kolor")
        self.__kolor = wybor
        self.podaj_kolor()
        self.__farba()

    def podaj_metraz(self):
        print("Metraż wynosi", self.__metraz)

    def podaj_kolor(self):
        print("Mamy kolor", self.__kolor)

    def podaj_liczba_okien(self):
        print("Liczba okien wynosi", self.__liczba_okien)

    def __farba(self):
        print("Skończyła sie farba")


dom1 = Dom(156, "czerwony", 8)
dom1.podaj_metraz()
dom1.zmien_metraz()
dom1.podaj_kolor()
dom1.podaj_liczba_okien()
dom1.zmien_liczba_okien()
dom1.zmien_kolor()
