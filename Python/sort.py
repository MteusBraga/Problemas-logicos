a, b, c=input().split()
a=int(a)
b=int(b)
c=int(c)
lista=[a,b,c]
clone=[]
for i in range(3):
    clone.append(lista[i])
lista.sort()
for i in range(3):
    print(lista[i])
print("")
for i in range(3):
    print(clone[i])


