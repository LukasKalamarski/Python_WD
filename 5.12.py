# -*- coding: utf-8 -*-
class Mies:
    def reverse(self):
        lista = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień']
        for i in range(0, 12, 1):
            yield lista[i]
dem = Mies().reverse()
for i in range(12):
    print(next(dem))