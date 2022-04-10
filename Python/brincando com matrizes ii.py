'''Escreva umprograma que leia uma matriz 3 x 3 de inteiros da entrada padrão e calcule a média de todos seus valores positivos, o menor valor lido, o valor delta e a soma de todos os elementos que não estão na diagonal principal.

O delta é igual a 1 se o menor valor for par e 0 se for ímpar.'''
matriz=[]
menor_val=[]
diagonal=[]
lista_sem_diagonal=[]
soma_posi = som_val_fora_diag = delta = cont = 0
for i in range(3):
    linha=[]
    for c in range(3):
        elemento=int(input(f'Digite o elemento {c+1} da linha {i+1}: '))
        linha.append(elemento) 
        menor_val.append(elemento)
        if i==c:
            diagonal.append(elemento)
        if elemento>=0:
            cont+=1
            soma_posi+=elemento
    matriz.append(linha)
    linha=[]
    
print(f'{soma_posi/cont:.2f}', end=' ')
menor_val.sort()

print(menor_val[0], end=' ')
if menor_val[0]%2==0:
    delta=1
    print(delta, end=' ')
else:
    print(delta, end=' ')
lista_sem_diagonal=matriz[0]+matriz[1]+matriz[2]
for k in range(3):
    lista_sem_diagonal.remove(diagonal[k])
for l in range(len(lista_sem_diagonal)):
    som_val_fora_diag+=lista_sem_diagonal[l]
print(som_val_fora_diag, end='')