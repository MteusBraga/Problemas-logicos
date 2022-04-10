/*
Dizemos que uma matriz inteira Anxn  é uma matriz de permutação se em cada linha e em cada coluna houver n-1 elementos nulos e um único elemento igual a 1.
Exemplo:

A matriz abaixo é de permutação:



Observe que




não é de permutação.

Dada uma matriz inteira Anxn, verificar se A é de permutação.
*/

#include <stdio.h>

int main() {
  int i, j, n, somaL[5], somaC[5], per=1;
  scanf("%d", &n);
  int matriz[n][n];
  for (i=0;i<n;i++){
    for(j=0;j<n;j++){
      scanf("%d[^\n]", &matriz[i][j]);
    }
  }
  for(i=0; i<n;i++){
    somaL[i]=0;
    somaC[i]=0;
  }
  for (i=0;i<n;i++){
    for(j=0;j<n;j++){
      somaL[i]=somaL[i]+matriz[i][j];
      somaC[j]=somaC[j]+matriz[i][j];
      printf("%d ", matriz[i][j]);
    }
    printf("\n");
  }
  for (i=0;i<n;i++){
    if(somaL[i]!=1 || somaC[i]!=1)
      per=0;
  }
  if(per==1)
    printf("True");
  else
    printf("False");
  
  return 0;
  
}