'''
Created on 12 de out de 2017

@author: Hugo
'''
entrada1 = raw_input().split(" ")
entrada2 = raw_input().split(" ")

lista = []
Npostos = int(entrada1[0])
distanciaIM = int(entrada1[1])
total = 42195
contador = 0
for i in entrada2:
    k = int(i)
    lista.append(k)


for i in range(len(lista)-1):
    a = lista[i]
    b = lista[i+1]
    if b-a > distanciaIM:
        contador += 1
    
if contador != 0:
    print("N")
else:
    print("S")
    
