lista=[]
for i in range(3):
    lista.append(float(input(f"Valor {i+1}: ")))

lista.sort(reverse=True)
print(lista)
a=lista[0]
b=lista[1]
c=lista[2]
if(a >= b+c):
    print("NAO FORMA TRIANGULO")
else:
    if(a**2==(b**2) + (c**2)):
        print("TRIANGULO RETANGULO")
    elif(a**2 > (b**2)+(c**2)):
        print("TRIANGULO OBTUSANGULO")
    elif(a**2 < (b**2)+(c**2)):
        print("TRIGANGULO ACUTANGULO")

    if(a==b and b==c):
        print("TRIANGULO EQUILATERO")
    elif(a!=b and b!=c):
        print("TRIANGULO ESCALENO")
    else:
        print("TRIANGULO ISOCELES")
