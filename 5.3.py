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
    def __gt__(self, k):
        k1 = Kwadrat(self.x)
        k2 = Kwadrat(k)
        return int(k1.x) > int(k2.x)
    def __ge__(self, k):
        k1 = Kwadrat(self.x)
        k2 = Kwadrat(k)
        return int(k1.x) >= int(k2.x)
    def __le__(self, k):
        k1 = Kwadrat(self.x)
        k2 = Kwadrat(k)
        return int(k1.x) <= int(k2.x)
    def __lt__(self, k):
        k1 = Kwadrat(self.x)
        k2 = Kwadrat(k)
        return int(k1.x) < int(k2.x)

kw = Kwadrat(4)
print(kw.__gt__(4))
print(kw.__ge__(4))
print(kw.__lt__(4))
print(kw.__le__(4))