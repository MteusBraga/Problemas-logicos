'''Com o aumento do uso dos computadores a teoria das matrizes está cada vez mais sendo aplicada em áreas como, Engenharia, Matemática, dentre outras.

Assim o desafio é você criar um programa que peça ao usuário a quantidade de linhas e colunas de uma matriz que ele quer. Em seguida, inserir os elementos da matriz e imprimir a saída esperada.'''

col_lin=[]
col_lin=input().split()
diag_prin=[]
diag_secun=[]
cont_neg=-1
som_prin = som_secun = menor = maior = 0
for x in range(2):
    col_lin[x]=int(col_lin[x])
matriz=[]
for i in range(col_lin[0]):
    linha=[]
    for j in range(col_lin[1]):
        elemento=int(input())
        linha.append(elemento)
        
        if elemento>0: #Contador dos numeor positivos
            maior+=1
        else: #Contador dos numeros negativos
            menor+=1
        if i==j:
            diag_prin.append(elemento)
    
    if col_lin[0] == col_lin[1]: #Diagonal secundaria, adicionar a partir do ultimo elemento da linha
        diag_secun.append(linha[cont_neg])
        cont_neg-=1
            
    matriz.append(linha)
    linha=[]
    
for c in range(len(diag_prin)): #Soma dos numeros da diagonal principal
    som_prin+=diag_prin[c]
for k in range(len(diag_secun)): #Soma dos numeros da diagonal secundaria
    som_secun+=diag_secun[k]

print('Matriz formada:') #Mostrar a matriz(sem colchetes e virgulas e sem espaco no final)
for z in range(len(matriz)):
    print(*matriz[z], sep=' ')
    

if col_lin[0] != col_lin[1]: #Se nao for matriz quadrada nao tem diagonal principal e secundaria
    print('A diagonal principal e secundaria nao pode ser obtida.')
else: #Se sim...
    print(f'A diagonal principal e secundaria tem valor(es) {som_prin} e {som_secun} respectivamente.')
print(f'A matriz possui {menor} numero(s) menor(es) que zero.')
print(f'A matriz possui {maior} numero(s) maior(es) que zero.')