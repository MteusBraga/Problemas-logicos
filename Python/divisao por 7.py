'''Seven é uma menina muito curiosa e gosta muito das aulas de matemática. A professora passou uma atividade para saber se um número é divisível por 7, porém os números eram muito grandes e ela queria uma outra forma de determinar isto. Após algum tempo pensando, descobriu que se pegar o último dígito de qualquer número inteiro, multiplicar por 5 e adicionar à parte restante do número (sem o último dígito), obterá um novo número. Se este número for divisível por 7, o número original também é. Agora ela precisa de sua ajuda para implementar este algoritmo seguindo seu raciocínio e ajudar na atividade de casa.'''


while True:
    n=int(input("digite um numero: "))
    r= ((n//1%10)*5)+(n//10)
    if n==0:
        break
    if r%7==0: 
        print("S")
    else:
        print("N")