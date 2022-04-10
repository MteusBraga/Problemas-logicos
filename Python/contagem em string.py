''' Eu sou fanático pela letra a. Para mim, é muito importante saber quantas vezes a letra a aparece em qualquer texto. Você pode me ajudar? Crie um programa que leia um texto qualquer e me diga quantas vezes a letra a aparece nele.

OBS: desconsidere acentos, como ã e à.'''

texto=input().upper()
cont=0
for i in range(len(texto)):
    if texto[i]=='A':
        cont+=1
print(cont)