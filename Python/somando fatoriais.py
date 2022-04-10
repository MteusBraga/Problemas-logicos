#nao anotei a descricao (._. )
print("-"*45)
print("Digite o numero que dejesa saber seu fatorial")
print("-"*45)
n  =0
acum= 1
cont=0
while True:
    num=int(input("Digite um numero: "))
    if num==-1:
        break
    for c in range(num,0,-1):
        acum*=c
    print(acum)
    acum=1