class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print('Jadę pojazdem')


class Car(Vehicle):
    def drive(self):
        print('Jadę samochodem')


class Bike(Vehicle):
    def drive(self):
        print("Jadę rowerem")


class HybridCar(Car, Bike):
    def drive(self):
        super().drive()
        Bike.drive(self)
        print("Jadę samochodem hybrydowym")


car1 = Car("Polonez")
car1.drive()

rower = Bike("Giant")
rower.drive()

hyb = HybridCar("Toyota")
hyb.drive()

print(HybridCar.__mro__)  # pokazuje kolejnosc dziedziczenia

# (<class '__main__.HybridCar'>, <class '__main__.Car'>, <class '__main__.Bike'>, <class '__main__.Vehicle'>, <class 'object'>)
