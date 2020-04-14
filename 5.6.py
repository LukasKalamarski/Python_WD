class Wspak:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
dem = Wspak("11_04_2020")
den = Wspak("MacBook-Pro")
det = Wspak("DuDuHastMich")
print(dem.__iter__())
for i in range(len(dem.data)):
    print(dem.__next__())
print(den.__iter__())
for i in range(len(den.data)):
    print(den.__next__())
print(det.__iter__())
for i in range(len(det.data)):
    print(det.__next__())
