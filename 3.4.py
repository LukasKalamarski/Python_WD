def mono(a, b):
    if(a>0): 
        print("Funkcja jest rosnaca")
    elif(a<0): 
        print("Funkcja jest malejaca")
    else: 
        print("Funkcja jest stala")

print("y = a x + b")
a = input("Wpisz a: ")
b = input("Wpisz b: ")
print(mono(a, b))