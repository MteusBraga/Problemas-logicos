'''Descrição Serão dados n números correspondendo as notas da turma de alunos de uma escola. Escreva um programa que leia essas notas e calcule quantas estão mais de 10% acima da média e quantas estão menos de 10% abaixo da média.'''
lista=[]
num=int(input())
soma=0
cont=0
contAcima=0
contAbaixo=0
for i in range(num):
    lista.append(float(input()))
    soma+=lista[i]
    cont+=1
media=soma/cont
for i in range(len(lista)):
    if lista[i]>media*1.1:
        contAcima+=1
    if lista[i]<media*0.9:
        contAbaixo+=1
   
print(f'{media:.2f}')
print(contAcima)
print(contAbaixo)