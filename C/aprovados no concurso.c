/*O IBGE realizou um concurso para contratar pessoas para trabalhar no censo. Cada candidato fez uma prova de português com 50 questões, outra de matemática com 35 questões, e uma prova de redação.

Para ser aprovado, era necessário acertar pelo menos 80% da prova de português, 60% da prova de matemática, e ter nota igual ou superior a 7 na redação.

Escreva um programa que receba como entrada, para cada candidato, a quantidade de questões certas em português e em matemática, e também a nota na redação, e depois exiba quantos candidatos foram aprovados.*/

#include <stdio.h>

int main() {
    int mat, por, cont;
    float red;
    while (1){
        scanf("%d", &por);
        scanf("%d", &mat);
        scanf("%f", &red);
        if(por<0 || mat <0 || red<0)
            break;
        if(por >= 50*0.8 && mat >= 35*0.6 && red >=7)
            cont++;
        
    }
    printf("%d", cont);
    return 0;
}
