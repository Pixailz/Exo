/*
    EXERCICE C #7
    [Révision : jusqu'a la séance 13 - chaînes de caractères]

    1> Ecrire une fonction qui compte le nombre de caractères d'une chaînes (comme strlen de <string.h>)
    2> Ecrire une fonction qui compte le nombre d'occurences d'un caractères (ex : 'a') dans une chaîne

    Indications :
        - pour la partie n°2, vous utiliserez la fonction ecrite e, partie n°1.
        - pensez a mettre vos variables en lecture seul constantes (ex : const int myData = 10).
*/
#include <stdio.h>

//Vos fonctions
// strLength();
// countOccurenceOf();
void flushBuffer(void);

int main(void){
    char chaine[256];
    printf("->");
    scanf ("%d", chaine);
    flushBuffer();
    printf("\n");
    int i;
    int count = 0;

    for (i = 0; i <= 256; i++){
        if (chaine[i] == '\0'){
            break;
        }
        printf("%c", chaine[i]);
    }

    printf("\n\n\n\n\n\n%d", count);

    //Taille de chaînes
    //strLength();
    
    //Nombre d'occurence de 'e'
    //countOccurenceOf();

    return 0;
}

//BufferFlusher

void flushBuffer(void){
    int c = 0;
    while(c != '\n' && c != EOF)
        c = getchar();
}
