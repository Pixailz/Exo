#include <stdio.h>

double moyenneTableau(int tableau[], int tailleTableau);

int main(void){
	double moyenne = 0;
	int tableau [4] = {15, 25, 30, 12};
	moyenne = moyenneTableau(tableau, 4);
	printf("%.2f", moyenne);
	return 0;
}

double moyenneTableau(int tableau[], int tailleTableau){
	int i;
	double somme = 0, moyenne = 0;
	for (i = 0; i < tailleTableau; i++){
		somme += tableau[i];
	}
	moyenne = somme / tailleTableau;
	return moyenne;
}