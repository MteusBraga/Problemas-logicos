'''Escrever um programa que lê um número N. Este N é o tamanho de um array.

Em seguida, leia cada um dos N números do array, encontre o menor elemento desse array, a sua posição dentro do array e imprima essas informações.

Considere que o array começa na posição 0'''

num=int(input())
lista=[]
lista=input().split()
copia=lista[:]
for i in range(len(copia)):
    copia[i]=int(copia[i])
copia.sort()

print(f'Menor valor: {copia[0]}')

for c in range(len(lista)):
    lista[c]=int(lista[c])
    if lista[c] == copia[0]:
        print(f'Posicao: {c}')