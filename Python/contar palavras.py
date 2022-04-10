#Fazer um programa para ler uma string e calcular o número de palavras que ele contém. Exemplo: casa amarela, o número de palavras é 2.

texto=input().strip()
cont=0
for i in range(len(texto)):
    if texto[i]==' ':
        cont+=1
print(cont+1)