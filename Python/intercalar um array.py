#Você deve intercalar dois arrays de números inteiros.
num=int(input())
lista=[]
lista2=[]
lista3=[]
cont=0
for i in range(num):
    lista.append(int(input()))
for c in range(num):
    lista2.append(int(input()))

for k in range(num):
    print(lista[k])
    print(lista2[k])