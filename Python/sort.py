lista=[]
clone=[]
for i in range(3):
    lista.append(int(input()))
    clone.append(lista[i])
lista.sort()
for i in range(3):
    print(lista[i])
print("")
for i in range(3):
    print(clone[i])


