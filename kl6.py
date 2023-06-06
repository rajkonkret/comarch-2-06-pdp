class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Menadzer(Pracownik):
    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.premia + self.pensja


pracownik = Pracownik("JAn", "Kowalski", 5000)
pracownik.przedstaw_sie()
wynagrodzenie_pr = pracownik.oblicz_pensje()
print(f"Wynagrodzenie dla pracownika {pracownik.imie} {pracownik.nazwisko}: {wynagrodzenie_pr}")
# Cześć, jestem JAn Kowalski
# Wynagrodzenie dla pracownika JAn Kowalski: 5000

menago = Menadzer("Anna", "Nowak", 8000, 2000)
menago.przedstaw_sie()
wynagrodzenie_me =  menago.oblicz_pensje()
print(f"Wynagrodzenie dla menadżera {menago.imie} {menago.nazwisko}: {wynagrodzenie_me}")
# Cześć, jestem Anna Nowak
# Wynagrodzenie dla menadżera Anna Nowak: 10000
# 14:55