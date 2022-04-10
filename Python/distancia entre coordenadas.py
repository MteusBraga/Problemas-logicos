'''A distância entre os pontos A e B é a medida do segmento que tem os dois pontos como extremidade. Por se tratar de dois pontos quaisquer, representaremos as coordenadas desses pontos de maneira genérica.

Fonte: Brasil Escola

Dessa forma para calcular a distância entre dois pontos faz-se necessário utilizar a seguinte fórmula (distância euclidiana):

Escreva um programa que leia um conjunto de N pares de pontos representados por suas coordenadas X e Y, mostrando como resultado a distância euclidiana entre cada um destes pontos.

A distância euclidiana tem que ser calculada por uma função chamada distancia, a qual recebe como parâmetros as coordenadas Xa, Ya, Xb e Yb, retornando como resultado a distância entre os pontos A e B'''

def distancia(Xa, Ya, Xb, Yb):
    d=(((Xb-Xa)**2)+((Yb-Ya)**2))**(1/2)
    print(f'{d:.2f}')

    
    
#main
c=[]
n=int(input())
for i in range(n):
    c=input().split()
    for n in range(len(c)):
        c[n]=int(c[n])
    distancia(c[0], c[1], c[2], c[3])