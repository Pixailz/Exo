#include <stdio.h>
#include "fonc.h"

int main(void){
    //--------------------------------------------------------------------------------------------
    /*
       c1 = Variable reponse de showMenu()
       c1 = Variable reponse de convertChoice()
    */
    char c1 = '0';
    char *levelChoice = &c1;
    int c1Converted = 0;
    int *levelChoiceConverted = &c1Converted;

    //--------------------------------------------------------------------------------------------
    //commande a faire pour un nombre aleatoires ;)
    initRandNbr();
    //--------------------------------------------------------------------------------------------
    //afficher le menu et demander un choix
    showMenu(levelChoice);
    printf("%d", c1Converted);
    return 0;
}