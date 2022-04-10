#nao anotei a descricao (._. )
a=0
n=0
while True:
    glic=int(input())
    if glic==0:
        break
    n+=glic
    a+=1
media=n/a
if media < 110:
    print("Glicose normal")
elif media>=200:
    print("Glicose muito Alta")
else:
    print("Glicose alterada")