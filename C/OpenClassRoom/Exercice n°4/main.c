#include <stdio.h>

void maximumTableau(int tableau[], int tailleTableau, int valeurMax);

int main (void){
    int tableau[4] = {15, 25, 30, 12};
    int i;
    for (i = 0; i < 4; i ++){
        printf("[%d]\n", tableau[i]);
    }
    maximumTableau(tableau, 4, 15);
    printf("\n");
    for (i = 0; i < 4; i ++){
        printf("[%d]\n", tableau[i]);
    }
    return 0;
}

void maximumTableau(int tableau[], int tailleTableau, int valeurMax){
    int i;
    for (i = 0; i < tailleTableau; i++){
        if (tableau[i] > valeurMax)
            tableau[i] = 0;
    }
}