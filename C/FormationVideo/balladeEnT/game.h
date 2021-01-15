#if !defined(__GAME__H__)
#define __GAME__H__
//--------------------------------------------------------------------------------------------
// Macro pour la taille de l'espace de jeu (modifiables)
	#define MAX_ROWS 2
	#define MAX_COLS 2
//--------------------------------------------------------------------------------------------
	#define MAX_I MAX_ROWS * 2
	#define MAX_J MAX_COLS * 2
//--------------------------------------------------------------------------------------------
// Protoypes des fonctions
	void gameManager(void);
	void initArea(char gameArea[][MAX_J], int *playerI, int *playerJ);
	void showArea(char gameArea[][MAX_J]);
	void showMenu(char *moveCommand);
	void updateArea(char gameArea[][MAX_J], char *moveCommand, int *playerI, int *playerJ);
	void moveUp(char gameArea[][MAX_J], int *playerI, int *playerJ);
	void moveDown(char gameArea[][MAX_J], int *playerI, int *playerJ);
	void moveLeft(char gameArea[][MAX_J], int *playerI, int *playerJ);
	void moveRight(char gameArea[][MAX_J], int *playerI, int *playerJ);
	void flushBuffer(void);
//--------------------------------------------------------------------------------------------
#endif