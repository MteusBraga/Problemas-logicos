'''Escreva um programa que recebe informações de várias figuras geométricas e, em seguida, imprime um resumo das características (área e comprimento) dessas figuras. O programa pode receber até 3 tipos de figuras: quadrado, retângulo e círculo, identificados pela primeira letra da figura. Caso as dimensões da figura forem negativas, o resultado do cálculo das características será -1. O programa encerrará quando o usuário digitar sair no tipo da figura.

Use funções para modularizar seu programa. Faça uma função para cada cálculo de característica de uma figura. Faça também uma função para imprimir o resumo final.

Obs.: Use pi = 3.14 e o resultado com 2 casas decimais de aproximação.'''

def area(tipo):
    if tipo=='c':
        r=int(input())
        ac=3.14*(r**2)
        lac.append(ac)
    elif tipo=='q':
        l=int(input())
        aq=l**2
        laq.append(aq)
    else:
        larg=int(input())
        c=int(input())
        ar=larg*c
        lar.append(ar)
        
        
def maior(lista):#maior valor de uma lista
    maiorN=0
    for i in range(len(lista)):
        if lista[i]>maiorN:
            maiorN=lista[i]
    return maiorN
    maiorN=0
        
#main 
cont=0
cont_c=0
lac = []
laq = []
lar = []

while True:
    t=str(input()).lower() 
    if t=='c':
        cont_c+=1
    if t=='sair':
        break
    cont+=1
    area(t)
per=(cont_c/cont)*100
mc=maior(lac)
mr=maior(lar)
mq=maior(laq)
print(f'Maior circulo: {mc:.2f}')
print(f'Maior retangulo: {mr:.2f}')
print(f'Maior quadrado: {mq:.2f}')
print('Quantidade de figuras ', cont)
print(f'Percentual de circulos: {per:.2f}')