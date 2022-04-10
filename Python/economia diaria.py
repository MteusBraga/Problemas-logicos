'''Poliana resolveu economizar dinheiro para comprar um carro.

Ela traçou como meta depositar um valor X em seu cofrinho no primeiro dia da semana, e ir guardando a cada manhã o valor do dia anterior acrescido de pelo menos R$ 0,50. Mas será que ela vai conseguir fazer isso todos os dias?

Para saber se o plano de Poliana vai dar certo, escreva um programa que receba como entrada o valor inicial depositado, e em seguida os valores depositados a cada dia. Ao final, exiba o total poupado e quantas vezes Poliana conseguiu cumprir sua meta.

Dica: é preciso sempre comparar o valor do dia com o do dia anterior'''

soma=0
cont=0
dia_anterior=0
for i in range(7):
    valor=float(input())
    if valor > dia_anterior:
        cont+=1
    dia_anterior=valor
    soma+=valor
print(f'R$ {soma:.2f}')
print(cont-1)