#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
using namespace std;

string shuffle(string word);

int main()
{
	//declarations des familles
	string shuffled(""), word(""), userWord(""), choice("");
	bool retry;
	int chanceMax(0), chanceCurrent(0), difficulty(0);
	do
	{
		int difficulty=1, chanceMax=0, chanceCurrent=0;
		srand(time(0));//initialisations du nombre alea
		zcout<<"Saisissez un mot : ";
		cin>>word; //cin du mot a chercher
		system("CLS");//effacage du mot ;)
			bool valideparlastreet(true);
			while(valideparlastreet)
			{
				bool diffcultyChoiceP(false);
				cout<<"1 : Facile"<<endl<<"2 : Moyen"<<endl<<"3 : Difficile"<<endl<<"Choix : ";
				cin>>difficulty;
				cout<<difficulty;
				if (difficulty==1)
				{
					chanceMax=15;
					chanceCurrent=15;
					valideparlastreet=false;
				}
				else if (difficulty==2)
				{
					chanceMax=10;
					chanceCurrent=10;
					valideparlastreet=false;
				}
				else if (difficulty==3)
				{
					chanceMax=5;
					chanceCurrent=5;
					valideparlastreet=false;
				}
				else
				{
					cout<<endl<<"Entrez un nombre valide"<<endl;
					system("PAUSE>NUL");
				}
			}
		shuffled=shuffle(word); //appelle de la super fonctions qui tue
		do
		{
			cout<<"("<<chanceCurrent<<"/"<<chanceMax<<") "<<"Qu'elle est ce mots : "<<shuffled<<endl; //affichage coup restant, coup max et du mot melanger
			cin>>userWord;
			chanceCurrent--; //decrementation du nombre de "vie"
			if (userWord==word) //si l'user a bon
			{
				cout<<"Bravo !"<<endl;
				cout<<"Le mot mystere etais : "<<word<<endl;
			}
			else if (chanceCurrent==1 && chanceCurrent!=0) //si il ne reste plus qu'une seul vie a l'user
			{
				cout<<"Le mot "<<shuffled<<" ne veux pas dire "<<userWord<<""<<endl<<"ATTENTION, il ne vous reste plus qu'un seul essais..";
				system("PAUSE>NUL");
				system("CLS");
			}
			else if (chanceCurrent>0 && chanceCurrent!=1) //si l'user perd une vie
			{
				cout<<"Le mot "<<shuffled<<" ne veux pas dire "<<userWord<<endl<<"Vous perdez 1 vie, il ne vous reste plus que : "<<chanceCurrent<<" essaie.";
				system("PAUSE>NUL");
				system("CLS");
			}
			else //sinon
			{
				cout<<"Vous n'avez plus d'essais .."<<endl<<"Le mot etais : "<<word<<"."<<endl;
			}
		//boucle jeux
		}while (userWord!=word && chanceCurrent!=0);
		cout<<"voulez-vous rejouez ? (r) : ";
		cin>>choice;
		if (choice=="r"||choice=="R") //ça coule de source
		{
			retry=true;
		}
		else
		{
			retry=false;
		}
		system("CLS");
	}while(retry);
}
string shuffle(string word) // et je melange je melange je melange je melange je melange 
{
	string melange;
	int position(0);
	while (word.size()!=0)
	{
		position=rand()%word.size();
		melange+=word[position];
		word.erase(position,1);
	}
	return melange;
}