'''O objetivo dessa tarefa é aprender a manipular listas em Python. Deve-se apresentar um programa que leia até 5 notas de um determinado aluno e as guarde em uma lista.

Em seguida, o programa deve exibir cada nota lida indicando sua posição na lista.'''
lista=[]
num_notas=int(input())
soma=0
cont=0
if num_notas>5 or num_notas<=0:
    print('Numero de notas invalido.')
else:
    for i in range(num_notas):
        cont+=1
        lista.append(float(input()))
        print(f'Nota {cont}: {lista[i]}')
        soma+=lista[i]
        
    media=soma/cont   
    print(f'Media: {media:.2f}')