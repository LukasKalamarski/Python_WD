class nazakupy:
    def __init__(self, nazwa, cena, ilosc, miara):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc
        self.miara = miara
    def wyswietl_produkt(self):
        print(self.nazwa)
        print(self.cena)
        print(self.ilosc)
        print(self.miara)
    def ile_produktu(self):
        print (self.nazwa, self.miara, self.ilosc)
    def ile_kosztuje(self):
        cena = self.ilosc * self.cena
        print (self.nazwa, 'kosztuje', cena, 'zl')

zakupy = nazakupy("piwo", 5, 2, 'butelka')
zakupy.ile_kosztuje()