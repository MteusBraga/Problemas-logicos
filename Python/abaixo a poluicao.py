'''Devido aos altos índices de poluição, uma cidade resolveu multar as casas que possuem mais de 2 veículos em R$ 12.89 por mês por cada veículo extra. Escreva um programa que receba como entrada a quantidade de veículos de várias residências, até que seja informado o valor 999, e exiba o total mensal arrecadado com as multas, e a quantidade de casas multadas.'''

sv=0 #soma veiculos
sm=0 #total de multas
qtd_veic=0
multa=12.89
sub=-2
while True:
    qtd_veic=int(input("Digite a quantidade de carros: "))
    if qtd_veic==999:
        break
    if qtd_veic>2:
        sm+=float((qtd_veic+sub)*multa)
    else:
        sv+=qtd_veic
        
        

print("Total de Multa arrecadada: ",sm)
print("Fim")
    