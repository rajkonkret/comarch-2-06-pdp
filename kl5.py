class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


# dziedziczenie po klasie Pojazd
class Samochod(Pojazd):
    """
    Samochod
    """

    def __init__(self, kolor, marka):
        super().__init__(kolor)
        self.marka = marka

    def info(self):
        super().info()
        print(f"Marka: {self.marka}")


pojazd = Pojazd("Biały")
pojazd.info()  # Kolor: Biały

samochod = Samochod("Czerwony", "Toyota")
samochod.info()  # Marka: Toyota
