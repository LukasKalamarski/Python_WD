class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y
       

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalty):
    def __init__(self, x):
        self.x=x
        self.y=x
    def __add__(self, k):
        k1 = Kwadrat(self.x)
        k2 = Kwadrat(k)
        wynik = k1.obwod() + k2.obwod()
        kw = Kwadrat(wynik)
        return kw

kw = Kwadrat(5)
print("x = {}".format(kw.__add__(8).x))
print("y = {}".format(kw.__add__(8).y))