#! /bin/bash

#Declaration de la fonction help
showHelp (){
	echo -e "Usage : $0 [dico.txt] [Options]"
	echo -e "Les parametre ne doit pas depasser 4 options "
	echo -e "  -o <file>: Exporter les stats"
	echo -e "  -t: Ajoute une tabulation, se qui aligne les stats"
}

#Affichage de la page help si -h est specifier pour $1
if [[ $1 == "-h" ]]; then
	showHelp
	exit 1
fi

#Verifie si $1 n'a pas été specifié ET si $1 est "dico.txt"
#+ page help
if [ -z $1 ] || [ $1 != dico.txt ]; then
	showHelp	
	exit 2
fi

#Initialisation des variable sur FALSE
tab="0"
out="0"
out2="0"

#Verification si le scripts a bien 4 ou moins de parametres
if [ $# -le 4 ]; then

	#Verifie $2
	if [[ $2 == -t ]]; then
		tab="1"
	elif [[ $2 == -o ]]; then 
		out="1"
		out2="3"
	fi

	#Verifie $3
	if [[ $3 == -t ]]; then
		tab="1"
	elif [[ $3 == -o ]]; then
		out="1"
		out2="4"
	fi
else
	showHelp
	exit 1
fi

#Si counted et sorted exist alors supprimer les mois
#Par exemple si le programme plante au lancement dernier il reste
#Des residus dans counted et l'affichage se vois fausser
if [ -e counted ] || [ -e sorted ]; then
	echo -e "Suppression de fichier residuel."
	rm -Rf counted sorted
else 
	echo -e "Pas de fichier residuel."
fi

#Sauvegarde des stats dans counted
echo -e "Comptage..."
for letter in {A..Z}; do
	echo -e "`grep "$letter" dico.txt | wc -l ` - $letter" >> counted
done

#Triage
echo -e "Triage..."
sort -rn counted -o sorted

#Affichage resultat
cat sorted

#Suppression ficher temporaire
echo -e "Suppression des fichier temporaire."
rm -Rf counted sorted