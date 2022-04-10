def partida(j1, j2):
    global p1
    global p2
    global e
    if j1=='papel' and j2=='pedra':
        p1+=1
    elif j1=='pedra' and j2=='tesoura':
        p1+=1
    elif j1=='tesoura' and j2=='papel':
        p1+=1
        
    elif j2=='papel' and j1=='pedra':
        p2+=1
    elif j2=='pedra' and j1=='tesoura':
        p2+=1
    elif j2=='tesoura' and j1=='papel':
        p2+=1
    else:
        e+=1
    
def resultado(p1, p2, e=0):
    if p1 > p2:
        print('MARIA')
    elif p2>p1:
        print('MIGUEL')
    else:
        print('MIGUEL')
    
#main
p1=p2=e=0
for i in range(5):
    jog1=str(input()).lower()
    jog2=str(input()).lower()
    partida(jog1, jog2)
r=resultado(p1, p2, e)
print(r)