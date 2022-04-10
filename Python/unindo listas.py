'''Faça um programa para ler duas listas de valores inteiros e gerar uma terceira lista que seja a união das duas listas informadas pelo usuário.

As listas devem ter pelo menos 1 elemento. Caso contrário, deve ser exibida a mensagem "Erro - A lista deve ter pelo menos 1 elemento."'''

num=int(input())
lista=[]
if num > 0:
    for i in range(num):
        lista.append(int(input()))
        print(lista[i], end=' ')
else:
    print('Erro - A lista deve ter pelo menos 1 elemento.')
    
num2=int(input())
lista2=[]

if num2 > 0:
    for c in range(num2):
        lista2.append(int(input()))
        print(lista2[c], end=' ')
else: 
    print('Erro - A lista deve ter pelo menos 1 elemento.')