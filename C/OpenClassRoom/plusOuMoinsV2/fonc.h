#if !defined(FONC_PLUS_OU_MOINS)
#define FONC_PLUS_OU_MOINS
//--------------------------------------------------------------------------------------------
//librairie utiliser
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//--------------------------------------------------------------------------------------------
//Prototypes des fonctions
void initRandNbr(void);
void showMenu(char *menuChoiceLevel);
void convertChoiceShowMenu(char *levelChoice, int *levelChoiceConverted);
void flushBuffer(void);
//--------------------------------------------------------------------------------------------
#endif