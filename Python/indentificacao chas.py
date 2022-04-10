"""Degustação de chá às cegas é a habilidade de identificar o chá usando somente os sentidos do paladar e do olfato.

Como parte do Incrível Campeonato de Puristas bebedores de Chá (ICPC), um programa de TV local organizou uma degustação. Durante o programa, cada competidor recebe uma chícara do mesmo chá. Eles podem cheirar e experimentar para tentar identificar o tipo de chá, que pode ser: (1) chá-branco; (2) chá-verde; (3) chá-preto; ou (4) chá de ervas. Ao final, as respostas são verificadas para saber o número de respostas corretas.

Dado o tipo de chá atual e as respostas dos participantes, determine a quantidade de competidores que acertaram a resposta."""

cont=0
tipo=int(input())
lista=[]
lista=input().split()
for i in range(len(lista)):
    lista[i]=int(lista[i])
    if lista[i]==tipo:
        cont+=1
print(cont)