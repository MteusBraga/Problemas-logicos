#include <stdio.h>
#include <stdlib.h>

int main(){
    char cpf[50];
    int vet[50];
    while(1){
        printf("Digite seu CPF:\n");
        scanf("%s", &cpf);
        
        int n = sizeof(cpf)/sizeof(char);
        printf("%d", n);
        /*if(n!=11){
            printf("ERRO: tamanho invalido!\n");
        }
        else{
            if(isdigit(cpf)){
                printf("%c", cpf[0]);
                break;
            }
            
        }*/
    }
    return 0;
}