#include <iostream>

void primos(int n){
  int i, j, cont=0;
  for(i=1;i<n+1;i++){
    for(j=1;j<n+1;j++){
      if(i%j==0){
        cont++;
       // std::cout<<"Cont = "<<cont<<std::endl;
      }
    }
    if(cont<=2) std::cout<<i<<" primo"<<std::endl;
    else std::cout<<i<<" nao"<<std::endl;
    cont=0;
  }
}

int main() {
  int n = 29;
  primos(n);
  return 0;
}