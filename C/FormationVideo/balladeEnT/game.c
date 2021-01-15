#include <stdio.h>
#include "game.h"
void gameManager(void){
	char cmd = 'm';
	int pX = 1, pY = 1;

	char gameArea[MAX_I][MAX_J];
	char *moveCommand = &cmd; 
	int *playerI = &pX, *playerJ = &pY;

	initArea(gameArea, playerI, playerJ);

	do{
		initArea(gameArea, playerI, playerJ);
		showArea(gameArea);
		showMenu(moveCommand);
		updateArea(gameArea, moveCommand, playerI, playerJ);
	}while(*moveCommand != 'q');
}

//------------------------------------------------------------------------------

void initArea(char gameArea[][MAX_J], int *playerI, int *playerJ){
	int i, j;
	for(i = 0; i < MAX_I; i++)
		for(j = 0; j < MAX_J; j++)
			if(i == 0 || i == MAX_I - 1 || j == 0 || j == MAX_J - 1)
				gameArea[i][j] = '0';
			else
				gameArea[i][j] = ' ';

	gameArea[*playerI][*playerJ] = 'T';
}

//------------------------------------------------------------------------------

void showArea(char gameArea[][MAX_J]){
	int i, j;
	printf("\n");
	for(i = 0; i < MAX_I; i++)
		for(j = 0; j < MAX_J; j++)
			if(j == 0 && i > 0)
				printf("\n%c", gameArea[i][j]);
			else
				printf("%c", gameArea[i][j]);
	printf("\n\n");
}

//------------------------------------------------------------------------------

void showMenu(char *moveCommand){
	printf("Deplacer votre personnage :\n");
	printf("u - Aller en haut\nd - Aller en bas\nl - Aller a gauche\nr - Aller a droite\nq - Quitter le jeux\n");
	printf("---------------------\n> ");
	scanf("%c", moveCommand);
	flushBuffer();
}

//------------------------------------------------------------------------------

void updateArea(char gameArea[][MAX_J], char *moveCommand, int *playerI, int *playerJ){
	switch(*moveCommand){
		case 'q':
			printf("Au revoir !\n");
			break;
		case 'u':
			moveUp(gameArea, playerI, playerJ);
			break;
		case 'd':
			moveDown(gameArea, playerI, playerJ);
			break;
		case 'l':
			moveLeft(gameArea, playerI, playerJ);
			break;
		case 'r':
			moveRight(gameArea, playerI, playerJ);
			break;
		default:
			printf("Commande incorrecte !\n");
			break;
	}
}

//------------------------------------------------------------------------------

void moveUp(char gameArea[][MAX_J], int *playerI, int *playerJ){
	if(*playerI == 1)
		return;
	gameArea[*playerI][*playerJ] = ' ';
	(*playerI)--; 
	gameArea[*playerI][*playerJ] = 'T';
}

//------------------------------------------------------------------------------

void moveDown(char gameArea[][MAX_J], int *playerI, int *playerJ){
	if(*playerI == MAX_I - 2)
		return;
	gameArea[*playerI][*playerJ] = ' ';
	(*playerI)++; 
	gameArea[*playerI][*playerJ] = 'T';
}

//------------------------------------------------------------------------------

void moveLeft(char gameArea[][MAX_J], int *playerI, int *playerJ){
	if(*playerJ == 1)
		return;
	gameArea[*playerI][*playerJ] = ' ';
	(*playerJ)--; 
	gameArea[*playerI][*playerJ] = 'T';
}

//------------------------------------------------------------------------------

void moveRight(char gameArea[][MAX_J], int *playerI, int *playerJ){
	if(*playerJ == MAX_J - 2)
		return;
	gameArea[*playerI][*playerJ] = ' ';
	(*playerJ)++; 
	gameArea[*playerI][*playerJ] = 'T';
}

//------------------------------------------------------------------------------

void flushBuffer(void){
	int c = 0;
	while(c != '\n' && c != EOF)
		c = getchar();
}