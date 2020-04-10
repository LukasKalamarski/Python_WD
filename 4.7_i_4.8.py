class Robaczek:
    def __init__ (self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
    def idz_w_gore(self, ilosc_krokow):
        self.y = self.y + ilosc_krokow
    def idz_w_dol(self, ilosc_krokow):
        self.y = self.y - ilosc_krokow
    def idz_w_lewo(self, ilosc_krokow):
        self.x = self.x - ilosc_krokow
    def idz_w_prawo(self, ilosc_krokow):
        self.x = self.x + ilosc_krokow
    def pokaz_gdzie_jestes(self):
        print(self.x)
        print(self.y)
    def __del__(self):
        print("game over")
rob = Robaczek(10, 10, 4)
rob.idz_w_gore(3)
rob.idz_w_dol(10)
rob.idz_w_lewo(15)
rob.idz_w_prawo(2)
rob.pokaz_gdzie_jestes()