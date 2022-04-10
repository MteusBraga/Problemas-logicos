'''José está prestes a inaugurar seu supermercado. Ele acredita que o cidadão brasileiro é capaz de pagar suas compras sozinho, sem precisar de um funcionário para conferir se o que ele está pagando corresponde aos produtos que ele está levando.

Para isso ele vai precisar de um programa que irá ler o dia da semana, o preço do produto, a opção do produto ("prata" ou "ouro") e o nome.

Se a compra estiver sendo realizada na segunda, terça ou quarta e a opção do produto for "ouro", o preço do produto ficará pela metade.

Se a compra estiver sendo realizada na quinta ou sexta e o preço estiver entre R 10.00𝑒𝑅  100.00, o preço será reduzido para um terço do valor original.

Se a compra estiver sendo realizada no sábado e a opção for prata, o preço do produto será o triplo.

Em qualquer outro caso, o preço será o dobro.'''

dia=input()
preco=float(input())
tipo=input()
produto=input()
if dia =='seg' or dia=='ter' or dia=='qua':
    if tipo=='ouro':
        print(f'O preco do produto {produto} no dia {dia} eh {preco/2:.2f}')
    else:
        print(f'O preco do produto {produto} no dia {dia} eh {preco*2:.2f}')
        
elif dia=='qui' or dia=='sex':
    if preco>=10 and preco<=100:
        print(f'O preco do produto {produto} no dia {dia} eh {preco/3:.2f}')
    else:
        print(f'O preco do produto {produto} no dia {dia} eh {preco*2:.2f}')
    
        
elif dia=='sab' and tipo =='prata':
    triplo=preco*3
    print(f'O preco do produto {produto} no dia {dia} eh {preco*3:.2f}')
else: 
    print(f'O preco do produto {produto} no dia {dia} eh {preco*2:.2f}')