'''Você receberá um array de inteiros e deve realizar deslocamentos à esquerda.

Por exemplo, o array:

1 2 3 4 5

Com dois deslocamentos à esquerda, ficaria:

3 4 5 1 2

Perceba que todos os elementos foram deslocados de duas posições.'''
lista=[]
n=int(input())

for i in range(n):
    lista.append(int(input()))


rotacao=int(input())
lista=lista[rotacao:]+lista[:rotacao]


for c in range(len(lista)):
    print(lista[c])