
def somaDiv(num):
    soma=0
    for c in range(num,0,-1):
        if num%c==0:
            soma+=c
    return soma
#main
maior=0
maior_n=0
for i in range(5):
    n=int(input())
    if maior < somaDiv(n):
        maior=somaDiv(n)
        maior_n=n
print(maior_n)