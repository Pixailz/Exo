#include <stdio.h>

int sommeTableau(int tableau[], int tailleTableau);

int main(void){
	int somme = 0;
	int tableau [4] = {15, 25, 30, 12};
	somme = sommeTableau(tableau, 4);
	printf("%d", somme);
}

int sommeTableau(int tableau[], int tailleTableau){
	int i, sommeTemp = 0;
	for (i = 0; i < tailleTableau; i++){
		sommeTemp += tableau[i];
	}
	return sommeTemp;
}