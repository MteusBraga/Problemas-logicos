/* Durante a pandemia, você e os seus amigos de um curso da área de TI resolveram marcar um encontro virtual para revisar o conteúdo de programação. Durante a conversa diversos desafios foram sugeridos e nesse momento Severino sugeriu um desafiou que ninguém conseguiu resolver, nem mesmo o próprio Severino. No entanto, como bom aluno você decidiu continuar sozinho tentando resolver o problema. O desafio se chama a soma de todos os vizinhos positivos de uma matriz quadrada. Considera-se como vizinhos neste programa as posições que ficam nos vizinhos adjacentes (superior, inferior, à esquerda e à direita) de uma posição da matriz. Por exemplo, veja a matriz 3x3 abaixo:



●  A posição(0,0) possui dois vizinhos válidas, são elas: (0,1) e (1,0). Por sua vez a posição (0,1), possui três vizinhos sendo dois deles vizinhos válidos: (0,2) e(1,1). Neste caso a posição (0,0) não foi considerado um vizinho válido porque nesta posição possui um valor negativo. A posição (1,1), possui quatro vizinhos válidos, são eles: (1,0), (0,1), (1,2) e (2,1).


Seu objetivo neste programa é percorrer toda a matriz, contar e somar os valores de todos os vizinhos válidos. */

#include <stdio.h>
int main(){
  int i, j, n, matriz[5][5];
  int soma=0, cont=0;
  scanf("%i", &n);
  for(i=0;i<n;i++){
    for (j=0; j<n; j++){
      scanf("%i", &matriz[i][j]);
    }
  }
  for(i=0;i<n;i++){
    for (j=0; j<n; j++){
      if(i==0){//primeira linha
        if(j==0){//c. superior esquerdo
          if (matriz[i][j+1]>=0){ //direita
            soma+=matriz[i][j+1];
            cont++;
          }
          if (matriz[i+1][j]>=0){//baixo
            soma+=matriz[i+1][j];
            cont++;
          }
        }
        else if (j==(n-1)){//c. superior direito
          if (matriz[i][j-1]>=0){//esquerda
            soma+=matriz[i][j-1];
            cont++;
          }
          if (matriz[i+1][j]>=0){//baixo
          soma+=matriz[i+1][j];
          cont++;
          }
        }
        else{
          if (matriz[i][j+1]>=0){ //direita
            soma+=matriz[i][j+1];
            cont++;
          }
          if (matriz[i][j-1]>=0){//esquerda
            soma+=matriz[i][j-1];
            cont++;
          }
          if (matriz[i+1][j]>=0){//baixo
            soma+=matriz[i+1][j];
            cont++;
          }

        }
      }
      else if (i==(n-1)){//ultima linha
        if(j==0){
          if (matriz[i-1][j]>=0){//cima
          soma+=matriz[i-1][j];
          cont++;
          }
          if (matriz[i][j+1]>=0){ //direita
            soma+=matriz[i][j+1];
            cont++;
          }
        }
        else if(j==n-1){//c. inferior direito
          if (matriz[i-1][j]>=0){//cima
              soma+=matriz[i-1][j];
              cont++;
            }
          if (matriz[i][j-1]>=0){//esquerda
            soma+=matriz[i][j-1];
            cont++;
          }
        }
        else{
          if (matriz[i][j+1]>=0){ //direita
            soma+=matriz[i][j+1];
            cont++;
          }
          if (matriz[i-1][j]>=0){//cima
            soma+=matriz[i-1][j];
            cont++;
          }
          if (matriz[i][j-1]>=0){//esquerda
            soma+=matriz[i][j-1];
            cont++;
          }
        }
      }
      else{
        if(j==0){
          if (matriz[i][j+1]>=0){ //direita
            soma+=matriz[i][j+1];
            cont++;
          }
          if (matriz[i+1][j]>=0){//baixo
            soma+=matriz[i+1][j];
            cont++;
          }
          if (matriz[i-1][j]>=0){//cima
            soma+=matriz[i-1][j];
            cont++;
          }
        }
        else if(j==n-1){//meio direita
          if (matriz[i][j-1]>=0){//esquerda
            soma+=matriz[i][j-1];
            cont++;
          }
          if (matriz[i+1][j]>=0){//baixo
            soma+=matriz[i+1][j];
            cont++;
          }
          if (matriz[i-1][j]>=0){//cima
            soma+=matriz[i-1][j];
            cont++;
          }
        }
        else{
          if (matriz[i][j+1]>=0){ //direita
            soma+=matriz[i][j+1];
            cont++;
          }
          if (matriz[i][j-1]>=0){//esquerda
            soma+=matriz[i][j-1];
            cont++;
          }
          if (matriz[i+1][j]>=0){//baixo
            soma+=matriz[i+1][j];
            cont++;
          }
          if (matriz[i-1][j]>=0){//cima
            soma+=matriz[i-1][j];
            cont++;
          }
        }
      }
    }
  }
  printf("%i\n", cont);
  printf("%i\n", soma);
  return 0;
}
