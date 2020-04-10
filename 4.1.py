import sys
podz4 = [ i for i in range(20) if i % 4 == 0]
plik = open("test.txt", "w")
podz4 = str(podz4)
plik.write(podz4)
print(podz4)
plik.close()