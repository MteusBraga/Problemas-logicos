#include <stdio.h>
#include <stdlib.h>

exibir(){
    printf("0 - Voto em branco\n");
    printf("1 - Voto em Joao\n");
    printf("2 - Voto em Maria\n");
    printf("3 - Voto em Pedro\n");
    printf("4 - Voto em Luis\n");
    printf("5 - Voto em Ana\n");
    printf("6 - Voto em Luiza\n");
    printf("7 - Voto em Silvia\n");
    printf("8 - Voto em Andre\n");
}
int main() {
    int vet[30];
    int i=0;
    char continuar[1];
    while(1){
        exibir();
        printf("Digite o numero: \n");
        scanf("%i", &vet[i]);
        printf("Continuar? [S/N][^\n]");
        scanf("%s", &continuar);
        printf("%s", continuar);
        if(continuar=="s"){
            //continue;
        }
        else{
            break;
        }
        i++;
    }
}



