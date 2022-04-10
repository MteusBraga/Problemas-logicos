matriz=[]
soma=0
n=int(input())
for i in range(n):
    linha=[]
    linha=input().split()
    matriz.append(float(linha[i]))
for c in range(len(matriz)):
    soma+=matriz[c]
#print(f'tr(A) = ({matriz[]})') 