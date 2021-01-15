#include "fonc.h"

void initRandNbr(void){
    srand(time(NULL));
}

void showMenu(char *levelChoice){
    printf("1 : Facile\n2 : Moyen\n3 : Difficile\n4 : Personalises ;)\n");
    scanf("%c", levelChoice);
    flushBuffer();
    convertChoiceShowMenu(levelChoice);
}

void convertChoiceShowMenu(char *levelChoice, int *levelChoiceConverted){
    if (*levelChoice == 'q' || *levelChoice == 'Q'){
        levelChoiceConverted = 1; 
    }
    else if (*levelChoice == '1'){

    }
    else if (*levelChoice == '2'){

    }
    else if (*levelChoice == '3'){

    }
    else if (*levelChoice == '4'){

    }
}

void flushBuffer(void){
    int c = 0;
    while(c != '\n' && c != EOF)
        c = getchar();
}