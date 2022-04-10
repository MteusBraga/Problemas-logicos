/*Valquíria trabalha em uma padaria e foi roubada ontem. Seus clientes ficaram com pena e resolveram organizar uma vaquinha para comprar um novo celular para ela. Escreva um programa que receba como entrada o valor doado por cada cliente, até que seja informado um valor negativo, e exiba o total arrecadado e o valor médio doado por eles. */
#include <stdio.h>
int main(){
    float total, doacao, media;
    int cont=0;
    printf("Insira os valores das doacoes:\n");
    while (1){
        scanf("%f", &doacao);
        if(doacao<0)
            break;
        total+=doacao;
        cont++;
        
    }
    if(cont==0)
        media=0;
    else
        media=total/cont;
    printf("Total arrecadado: %.2f\n", total);
    printf("Valor medio da doacao: %.2f", media);
    return 0;
}