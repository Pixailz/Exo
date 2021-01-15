#include <stdio.h>

void ordonnerTableau(int tableau[], int tailleTableau);

int main(void){
    int tableau[4] = {15, 81, 22, 13};
    int i;
    for (i = 0; i < 4; i ++){
        printf("[%d]\n", tableau[i]);
    }
    ordonnerTableau(tableau, 4);
    printf("\n");
    for (i = 0; i < 4; i ++){
        printf("[%d]\n", tableau[i]);
    }
    return 0;
}

void ordonnerTableau(int tableau[], int tailleTableau){
    int i, j, temp = 0;
    for (i = 0; i < tailleTableau; i++){
        for (j = 0; j < tailleTableau; j++){
            if(tableau[j] > tableau[j + 1]){
                temp = tableau[j];
                tableau[j] = tableau[j + 1];
                tableau[j + 1] = temp;
                temp = 0;
            }
        }
    }
}