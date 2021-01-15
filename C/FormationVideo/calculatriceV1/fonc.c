#include <stdio.h>
#include "fonc.h"

int choiceD(char choiceOp){
    if (choiceOp == '1'){
        printf("Addition selectionner\n");
        return 1;
    }
    else if (choiceOp == '2'){
        printf("Soustraction selectionner\n");
        return 2;
    }
    else if (choiceOp == '3'){
        printf("Multiplication selectionner\n");
        return 3;
    }
    else if (choiceOp == '4'){
        printf("Division selectionner\n");
        return 4;
    }
    else if (choiceOp == 'q' || choiceOp == 'Q'){
        return 5;
    }
    else{
        printf("\nEntrez un nombre valide.\n");
        return 0;
    }
}
int nbrChecker(int nbr1, int nbr2){
    if (nbr1 < -1000 || nbr1 > 1000 || nbr2 < -1000 || nbr2 > 1000){
        printf("Entrer un nombre compris en -1 000 et 1 000.\n");
        return 0;
    }
    else{
        return 1;
    }
}

void flushBuffer(void){
    int c = 0;
    while(c != '\n' && c != EOF)
        c = getchar();
}