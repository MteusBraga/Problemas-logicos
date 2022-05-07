matriz=[]
n=int(input())
soma_ou_media=input().lower()

soma=0
cont=0

for i in range(12):
    linha=[]
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)
    linha=[]

for i in range(12):
    for j in range(12):
        if(i==n):
            cont=cont+1
            soma=soma + matriz[i][j]
if(soma_ou_media=="s"):
    print(f"{soma:.1f}")
else:
    media=soma/cont
    print(f"{media:.1f}")

