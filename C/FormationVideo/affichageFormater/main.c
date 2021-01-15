/*
EXERCICE C #1
[Révision : affichage/saisie, variables]
> Ecrire un programme qui demande un nombre entier a l'utilisateur
  et affiche le valeur de la saisie en octal et hexadecimal

> Indications : 
  - Formater en Octal     -> %o
  - Formater en hexadecimal  -> %x ou %X
*/
#include <stdio.h>

int main(void)
{
  int nombre = 0;
  printf("Saisissez un nombre entier\n");
  scanf("%d", &nombre);
  printf("le nombre %d vaux : %x en hexa\n", nombre, nombre);
  printf("le nombre %d vaux : %o en octet\n", nombre, nombre);
  return 0;
}
