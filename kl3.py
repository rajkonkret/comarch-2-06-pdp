class Car:
    """
    Klasa samochód
    """

    def __init__(self, model, year=2000):
        self.model = model
        self.year = year
        # pola prywatne
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def licznik(self):
        print("Prędkośc wynosi", self.__predkosc, "km/h")

    def hamuj(self):
        self.__predkosc -= 10

    # metoda prywatna
    def __zmien_bieg(self):
        print("zmiana biegu")


car1 = Car("Honda", 2023)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# print(car1.predkosc)
car1.licznik()  # Prędkośc wynosi 50 km/h
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()  # Prędkośc wynosi 0 km/h
