class Slowa:
    def __init__ (self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    def sprawdz_czy_palindrom(self):
        j = len(self.s1)-1
        for i in range(len(self.s1)/2):
            if(self.s1[i] != self.s1[j]):
                return 0
            j= j-1
        return 1
    def sprawdz_czy_metagramy(self):
        w = 0
        for i in range(len(self.s1)):
            if(self.s1[i] != self.s2[i]):
                w= w+1
        if(w==1): return 1
        else: return 0
    def sprawdz_czy_anagramy(self):
        for i in range(len(self.s1)):
            w = 0
            for j in range(len(self.s2)):
                if(self.s1[i]==self.s2[j]):
                    w=w+1
                if(j == len(self.s2)-1 and w==0):
                    return 0
        return 1
    def wyswietl_wyrazy(self):
        print(self.s1)
        print(self.s2)


slowa = Slowa('mata', 'tama')
# print(slowa.sprawdz_czy_palindrom())
# print(slowa.sprawdz_czy_metagramy())
# print(slowa.sprawdz_czy_anagramy())
print(slowa.wyswietl_wyrazy())