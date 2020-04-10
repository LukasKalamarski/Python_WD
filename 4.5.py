class ciag:
    def __init__(self, x0, r, n):
        self.x0 = x0
        self.r = r
        self.n = n
        self.lista = [x for x in range(self.x0, self.r, self.n)]
    def wyswietl_dane(self):
        print(self.lista)
    def pobierz_elementy(self):
        self.lista.append(input())
    def pobierz_parametry(self):
        self.x0 = input()
        self.r = input()
        self.n = input()
    def policz_sume(self):
        wynik = 0
        for i in range(len(self.lista)):
            wynik = wynik + self.lista[i]
        return wynik
    def policz_elementy(self):
        return len(self.lista)
ciag1 = ciag(0, 10, 1)
# ciag1.pobierz_elementy()
# ciag1.wyswietl_dane()
# print(ciag1.policz_sume())
# print(ciag1.policz_elementy())
# ciag1.pobierz_parametry()
# print(ciag1.lista)