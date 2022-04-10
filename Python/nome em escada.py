#Faça um programa que solicite o nome do usuário e imprima o nome em formato de escada.

nome=input().upper()
cont=0
for i in range(len(nome)):
    cont+=1
    
    print(nome[:cont])