#Faça um programa que leia 3 números inteiros e imprima o valor intermediário (entre o menor e o maior número). Suponha que os números são diferentes.
lista=[]
for i in range(3):
    lista.append(int(input()))
lista.sort()
print(lista[1])