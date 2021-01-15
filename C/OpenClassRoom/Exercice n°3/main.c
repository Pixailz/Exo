#include <stdio.h>

void copie(int tableauOriginal[], int tableauCopie[], int tailleTableau);

int main(void){
    int tailleTableau = 4, i;
    int tableauOriginal[4] = {15, 25, 30, 12};
    int tableauCopie[4] = {0};
    for (i = 0; i < tailleTableau; i ++){
        printf("[%d] | (%d)\n", tableauOriginal[i], tableauCopie[i]);
    }
    copie(tableauOriginal, tableauCopie, tailleTableau);
    printf("\n\n");
    for (i = 0; i < tailleTableau; i ++){
        printf("[%d] | (%d)\n", tableauOriginal[i], tableauCopie[i]);
    }
    return 0;
}

void copie(int tableauOriginal[], int tableauCopie[], int tailleTableau){
    int i;
    for (i = 0; i < tailleTableau; i ++){
        tableauCopie[i] = tableauOriginal[i];
    }
}