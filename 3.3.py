lista = {'cukier': 'kilogramy', 'bulki': 'sztuki', 'banany': 'kiscie', 'jablka': 'sztuki', 'chleby': 'sztuki'}
print(lista)
nlista = [zakup for zakup, typ in lista.items() if typ == "sztuki"]
print(nlista)