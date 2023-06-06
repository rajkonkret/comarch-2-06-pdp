# wielodziedziczenie

class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(A, B):
    """
    Klasa C, dziedziczy po  A i B
    """

    def method(self):
        # super().method()
        # print("Metoda z kalsy C")
        B.method(self)


a = A()
a.method()

b = B()
b.method()
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
c = C()
c.method()
