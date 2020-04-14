class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadzerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


adrian = Menadzer("Adrian", "Mikulski", 12000)
adelajda = Pracownik("Adelajda", "Lydka", 6000)
# print(isinstance(adrian, Osoba))
# print(isinstance(adrian, Pracownik))
# print(isinstance(adrian, Menadzer))
# print(isinstance(adelajda, Osoba))
# print(isinstance(adelajda, Pracownik))
# print(isinstance(adelajda, Menadzer))
print(issubclass(Pracownik, Pracownik))
print(issubclass(Pracownik, Menadzer))
print(issubclass(Menadzer, Pracownik))
print(issubclass(Menadzer, Osoba))
# print(jozek.przedstaw_sie())
# print(adrian.przedstaw_sie())