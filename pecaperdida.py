entrada1 = int(input())
entrada2 = input()
lista = entrada2.split(' ')
lista2 = []
lista3 = []
contador = 0
for i in lista:
    k = int(i)
    lista2.append(k)
for j in range(entrada1 - 1):
    contador += 1
    lista3.append(contador)
for x in lista3:
    if x not in lista2:
        print(x)
