#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MIN 1
#define DEFAULT_NBR_MAX 10

//--------------------------------------------------------------------------------------------
//Prototypes des fonctions
int gameManager(void);
void initRandNbr();
void convertChoiceShowMenu(char choice, int *choiceConverted);
void initNbrMystere(int *nbrMax, int *nbrMystere, int *choiceConverted);
void game(int *nbrMystere, int *retry, int *nbrMax);
void showCount(int *count);
void getChoice(int *choice);
void flushBuffer(void);

//--------------------------------------------------------------------------------------------
//
int main(void){
    gameManager();
    return 0;
}

//--------------------------------------------------------------------------------------------
//
int gameManager(void){
    int retry = 0;
    do{
        char choice = '0';
        int choiceConverted = 0, nbrMax = DEFAULT_NBR_MAX, nbrMystere = 0;
        initRandNbr();
        do{
            printf("1 : Facile (entre 1 et 100)\n2 : Moyen (entre 1 et 1000)\n3 : Difficile (entre 1 et 10 000)\n4 : Personalises ;)\nq : Quitter\n->");
            scanf("%c", &choice);
            flushBuffer();
            convertChoiceShowMenu(choice, &choiceConverted);
            if (choiceConverted == 99)
                return 0;
        }while(choiceConverted == 0);

        initNbrMystere(&nbrMax, &nbrMystere, &choiceConverted);

        do{
            game(&nbrMystere, &retry, &nbrMax);
            if (retry == 0){
                initNbrMystere(&nbrMax, &nbrMystere, &choiceConverted);
            }
            else if (retry == 2){
                return 0;
            }
        }while(retry == 0);
    }while(retry == 1);
}

//--------------------------------------------------------------------------------------------
//
void initRandNbr(){
    srand(time(NULL));
}

//--------------------------------------------------------------------------------------------
//
void convertChoiceShowMenu(char choice, int *choiceConverted){
    if (choice == 'q' || choice == 'Q'){
        *choiceConverted = 99; 
    }
    else if (choice == '1'){
        *choiceConverted = 1;
    }
    else if (choice == '2'){
        *choiceConverted = 2;
    }
    else if (choice == '3'){
        *choiceConverted = 3;
    }
    else if (choice == '4'){
        *choiceConverted = 4;
    }
    else{
        printf("Entrez un un choix correct\n");
        *choiceConverted = 0;
    }
}

//--------------------------------------------------------------------------------------------
//
void initNbrMystere(int *nbrMax, int *nbrMystere, int *choiceConverted){
    if (*choiceConverted == 1){
        *nbrMax = 100;
    }    
    if (*choiceConverted == 2){
        *nbrMax = 1000;
    }    
    if (*choiceConverted == 3){
        *nbrMax = 10000;
    }    
    if (*choiceConverted == 4){
        int tmpMax = 0;
        do{
            printf("Saisissez un nombre entre 1 et 1000000000\n->");
            scanf("%d", &tmpMax);
            flushBuffer();
            if (tmpMax > 1 && tmpMax <= 1000000000){
                *nbrMax = tmpMax;
                printf("Le nombre aleatoire sera entre 1 et %d\n", *nbrMax);
            }
            else{
                printf("Saisis incorrect.\n");
                tmpMax = 0;
            }
        }while (tmpMax == 0);       
    } 
    *nbrMystere = (rand() % (*nbrMax - MIN + 1)) + MIN;
}

//--------------------------------------------------------------------------------------------
//
void game(int *nbrMystere, int *retry, int *nbrMax){
    int count = 0, choice = 0;
    char choiceRetry = '0';
    do{
        printf("(%d) Le chiffre se trouve entre 1 et %d\n->", count, *nbrMax);
        scanf("%d", &choice);
        flushBuffer();
        count++;
        if (choice < *nbrMystere){
            printf("c'est plus grand\n");
        }
        else if (choice > *nbrMystere){
            printf("C'est plus petit\n");
        }
        else{
            int winPass = 0;
            do{
                printf("Bravo vous avez GAGNER en %d coups\n", count);
                printf("Voulez vous :\nR : rejouez\nQ : quitter\nM : Menu\n->");
                scanf("%c", &choiceRetry);
                flushBuffer();
                if (choiceRetry == 'r' || choiceRetry == 'R'){
                    *retry = 0;
                    winPass = 1;
                }
                else if (choiceRetry == 'm' || choiceRetry == 'M'){
                    *retry = 1;
                    winPass = 1;
                }
                else if (choiceRetry == 'q' || choiceRetry == 'q'){
                    *retry = 2;
                    winPass = 1;
                }
                else{
                    printf("Saisis incorrect.\n");
                }
            }while (winPass == 0);
        }
    }while (choice != *nbrMystere);
}

//--------------------------------------------------------------------------------------------
//
void flushBuffer(void){
    int c = 0;
    while(c != '\n' && c != EOF)
        c = getchar();
}
/*
    ici la foncion flushBuffer permet qu'apres un scanf();
    a la fin d'une boucle, lorsque l'ont veux redemander
    un scanf() tout se passe bien sans erreur de saisie 
    renvoyer par convertChoiceShowMenu().
*/