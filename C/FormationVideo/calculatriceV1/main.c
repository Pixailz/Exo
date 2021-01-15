/*
    Exercice C #4
    [Révision : jusqu'à la programmation modulaire]
    > Ecrire un programme de calculatrice simple pour 2 nomnbre :
        - afficher un menu principal proposant les 4 types de calcul (+, -, * et /) ou de quitter
        - une fois le calcul choisi, demander la saisie de 2 nombres et afficher le resultat.
        - rediriger vers le menu principal.

    > Indications :
        - utiliser au maximum de fonctions (pour optimiser votre code et eviter les repetitions).
        - verifier que la saisie au menu est correct, sinon redemander une saisie.
        - verifier qie les nombre saisis sont compris entre -1000 et 1000.
        - compiler avec la commande -> gcc *.c - main (donnera un executable main ou main.exe)
*/
#include <stdio.h>
#include "fonc.h"

int main (void){
    char choiceOp ='0', flusher ='0';
    int loopPass = 1;
    while(loopPass == 1){
        int nbr1 = 0, nbr2 = 0, resultat = 0, nbrsChecked = 0, choiceDecrypted = 0;
        do{
            printf("_____CalculatriceV1_____\n");
            printf("1. Addition\n2. Soustraction\n3. Multiplications\n4. Division\nEntrer Q pour quitter\nCHOICE->");
            scanf("%c", &choiceOp);
            flushBuffer();
            printf("\n");
            choiceDecrypted = choiceD(choiceOp);
            if (choiceDecrypted == 5)
                return 0;
        }while (choiceDecrypted == 0);
        do{
            printf("Entrer un premier chiffre\nCHOICE->");
            scanf("%d", &nbr1);
            flushBuffer();
            printf("Entrer un deuxieme chiffre\nCHOICE->");
            scanf("%d", &nbr2);
            flushBuffer();
            printf("\n");
            nbrsChecked = nbrChecker(nbr1, nbr2);
        }while (nbrsChecked == 0);
        if (choiceDecrypted == 1)
            printf("%d + %d = %d\n", nbr1, nbr2, nbr1 + nbr2);
        if (choiceDecrypted == 2)
            printf("%d - %d = %d\n", nbr1, nbr2, nbr1 - nbr2);
        if (choiceDecrypted == 3)
            printf("%d x %d = %d\n", nbr1, nbr2, nbr1 * nbr2);
        if (choiceDecrypted == 4 && nbr2 != 0){
            printf("%d / %d = %d\n", nbr1, nbr2, nbr1 / nbr2);
        }
        else if (nbr2 <= 0){
            printf("Vous ne pouvez pas diviser par zero ou moins ;)\n");
            return -1;
        }
    }
}