/*
Como sempre temos aqui uma história sem sentido, então:

Arthur estava entediado quando a Entidade sussurrou no seu ouvido, que tal uma aposta? Arthur como um bom apostador aceitou e ainda sugeriu a aposta: Dada uma matriz quadrada, cada um escolheria um conjunto da matriz para somar e obter um resultado. Porém, Rodrigo que estava passando na rua ao lado ouviu a voz da Entidade e já ficou animado. Entrou no quarto de Arthur pela janela e perguntou o que estava acontecendo e logo resolveu entrar na aposta também.

Os conjuntos escolhidos por eles foram:

Arthur: Linhas pares
Entidade: Colunas ímpares
Rodrigo: Diagonal principal
Faça um programa que receba uma matriz quadrada, some os valores das linhas pares, os valores das colunas ímpares, os valores da diagonal principal e com isso imprima o vencedor da aposta e a soma dos valores que corresponde ao seu conjunto. Lembre-se que pode ocorrer um empate duplo ou triplo. */

#include <stdio.h>

int main(void) {
  int i, j, n, matriz[5][5];
  int p_arthur=0, p_entidade=0, p_intr=0;
  scanf("%i", &n);
  for(i=0;i<n;i++){
    for (j=0;j<n;j++){
      scanf("%i", &matriz[i][j]);
    }
  }
  for (i=0; i<n; i++){
    for (j=0;j<n;j++){
      if(j%2!=0)
        p_entidade+=matriz[i][j];
      if(i%2==0)
        p_arthur+=matriz[i][j];
      if (i==j)
        p_intr+=matriz[i][j];
    }
  }
  if(p_arthur > p_entidade && p_arthur> p_intr){
      printf("Arthur venceu!\n");
      printf("Resultado: %i", p_arthur);
  }
  else if(p_entidade > p_arthur && p_entidade > p_intr){
      printf("A entidade venceu!\n");
      printf("Resultado: %i",p_entidade);
  }
  else if(p_intr > p_arthur && p_intr > p_entidade){
      printf("O intrometido venceu!\n");
      printf("Resultado: %i", p_intr);
  }
  else{
      printf("Empate!\n");
      if(p_arthur==p_entidade || p_arthur==p_intr)
        printf("Resultado: %i", p_arthur);
      else if(p_entidade==p_arthur || p_entidade==p_intr)
        printf("Resultado: %i", p_entidade);
      else if(p_intr==p_arthur||p_intr==p_entidade)
        printf("Resultado: %i", p_intr);
      else
        printf("Resultado: %i", p_arthur);
  }
  
  return 0;
}