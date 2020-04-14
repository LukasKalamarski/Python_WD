import itertools
lista = range(1, 11)
for k in [3]:
    for sublist in itertools.combinations(lista, k):
        print(sublist)