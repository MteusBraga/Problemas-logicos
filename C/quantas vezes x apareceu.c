/*Leia 10 números inteiros.

Depois leia mais um número inteiro x.

Sua missão é imprimir quantas vezes x apareceu entre os 10 primeiros inteiros lidos.*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main() {
    int vetor[10], x ,cont;
    for (int i=0; i<10;i++)
        scanf("%d",&vetor[i]);
    scanf("%d", &x);
    for (int i=0; i<10;i++)
        if (vetor[i]==x)
            cont++;
    printf("%d", cont);  
}