/*
  EXERCICE C #2
  [Révision : jusqu'à la séance 6]
      >Écrire un programme de rendus de monnaies.
      En saisissant le montant total des achats 
      puis la somme donnée, indiquer la monnaie
      a rendre(en billet de 20€, 10€ et 5€ et
      pièces de 2€ et 1€)
     
    >Indication :
      - S'aassurer que la somme donnée est bien
      supérieur a la somme fes achats
      - Gerer le cas ou on aurait payé un 
      montant egal aux achats
      - Rendre le moins de billets/pièces 
      possible (25€ de monnaie -> 1 billet de
      20€ + un billet de 5€)
      - L'opérateur % (modulo) ser utile pour 
      cette exercice
*/
#include <stdio.h>
int main(void)
{
  int retry = 1;
  char retryQuestion = 'Y';
  while(retry == 1){
    int purchases = 0, amoutPaid =0, result = 0;
    int bill20 = 0, bill10 = 0, bill5 = 0, coin2 = 0, coin1 = 0;
    printf("Entrez le total des achat\n->");
    scanf("%d", &purchases);
    printf("Entrez la monnaie donnée\n->");
    scanf("%d", &amoutPaid);
    if (amoutPaid < purchases){
      printf("Vous n'avez pas assez donnée d'argent :(\n");
      return -1;
    }
    else if(amoutPaid == purchases){
      printf("Pas de monnaie a rendre\n");
      return 0;
    }
    else{
      result = amoutPaid - purchases;
      bill20 = result / 20;
      result %= 20;
      bill10 = result / 10;
      result %= 10;
      bill5 = result / 5;
      result %= 5;
      coin2 = result / 2;
      result %=2;
      coin1 = result / 1;
      result %=1;
      printf("\n______MONNAIE A RENDRE______\n");
      if (bill20 > 0)
        printf("Billet(s) de 20 euros : %d x 20 : %d\n", bill20, bill20*20);
      if (bill10 > 0)
        printf("Billet(s) de 10 euros : %d x 10 : %d\n", bill10, bill10*10);
      if (bill5 > 0)
        printf("Billet(s) de 5 euros : %d x 5 : %d\n", bill5, bill5*5);
      if (coin2 > 0)
        printf("Piece(s) de 2 euros : %d x 2 : %d\n", coin2, coin2*2);
      if (coin1 > 0)
        printf("Piece(s) de 1 euros : %d x 1 : %d\n", coin1, coin1*1);
      printf("Appuyer sur \"Q\" pour quittez\n");
      scanf("%c", &retryQuestion);
      if (retryQuestion == 'Q' || retryQuestion == 'q'){
        retry = 0;
      }
    }
  }
}