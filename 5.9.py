class Parz:
    def __init__(self, data):
        self.data = data

    def reverse(self):
        for index in range(0, len(self.data), 1):
            if(index%2==0):
                yield self.data[index]
sl = "NeverTooLate"
dem = Parz(sl).reverse()
for i in range(len(sl)):
    print(next(dem))