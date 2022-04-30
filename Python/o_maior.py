a, b, c=input("Digite os valores").split()
a=int(a)
b=int(b)
c=int(c)
if(a>b):
    if (a > c):
        print(f"{a} eh maior")
    else:
        print(f'{c} eh maior')
else:
    if(b > c):
        print(f"{b} eh maior")
    else:
        print(f"{c} eh maior")