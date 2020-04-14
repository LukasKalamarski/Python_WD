class Fib:
    def __init__(self, ile):
        self.ile = ile
    def reverse(self):
        lista = [1, 1]
        for i in range(2, self.ile+2, 1):
            lista.append(lista[i-1]+lista[i-2])
            yield lista[i-2]
dem = Fib(12).reverse()
for i in range(12):
    print(next(dem))