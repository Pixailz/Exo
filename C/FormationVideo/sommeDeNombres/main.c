#include <stdio.h>
/*
    EXERCICE C #3
    [Révision : boucles]
    >   Ecrire un programme qui calcule la somme des entiers d'un
        nombre à un autre (maximum : entre 1 et 1 000)

    >   Indications :
        - prévoir le cas où "min" serait plus grand que "max" et quitter
        le programme si cela arrive.
        - prévoir le cas où "min" serait plus petit que 1 et "max" plus grand
        que 1 000.
*/
int main (void)
{
    int min = 0, max = 0;

    printf("Entrez le minimum\n->");
    scanf("%d", &min);
    printf("Entrez le maximum\n->");
    scanf("%d", &max);
    
    if (min > max){
        printf("Le minimum %d est superieur au maximum %d", min, max);
        return -1;
    }
    else if (min < 1){
        printf("Le minimum %d est inferieur a 1.\n", min);
        return -1;
    }
    else if (max > 1000){
        printf("Le maximum %d est superieur a 1 000\n", max);
        return -1;
    }
    else
    {
        printf("L'Ecart entre %d et %d est de %d.", min, max, max - min);
        return 0;
    }
}