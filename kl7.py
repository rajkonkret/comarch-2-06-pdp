from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod
    def wydaj_odgłos(self):
        pass


class Orzel(Ptak):
    """
    klasa Orzeł
    """

    def wydaj_odgłos(self):
        print("piiiiiiiiii")

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
        self.gatunek = gatunek

    def wydaj_odgłos(self):
        print("kokokoko")

    def latam(self):
        print(f"Tu", self.gatunek, "Ja nie latam")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


# or1 = Ptak("Orzeł", 20)
# or1.latam()
# or1.wydaj_odgłos()
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()

or2 = Orzel("orzel", 20)
or2.latam()
or2.wydaj_odgłos()
or2.poluj()

kur2 = Kura("kura")
kur2.wydaj_odgłos()
kur2.latam()
kur2.dziobanie()
# 15:20

