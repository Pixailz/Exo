#!/bin/bash

#Verification de la syntaxe de la commande
if [ -z $1 ] || [ -z $2 ]; then
	echo -e "Usage : $0 [TEXT] [OUTPUT_TEXT]"
	exit 0
fi

#Verification de la disponibilite du fichier dans le dossier output
if [ -e output/$2 ]; then
	echo -e "Le fichier $2 existe deja dans le fichier output."
	while [[ $answer != "y" ]] && [[ $answer != "n" ]]; do
		read -p "Voulez vous supprimer se fichier ? (Y/N) " -n 1 -s answer

		#Convertion $answer de majuscule a minuscule
		answer=`echo "${answer,,}"`

		#Suppression du fichier en fonction du choix
		if [[ $answer = "n" ]]; then 		#SI l'utilisateur a choisi de ne pas le supprimer
			echo -e "\nLe fichier $2 ne peux pas etre créé car il existe deja."
			exit 1
		elif [[ $answer = "y" ]]; then 		#SI l'utilisateur veux supprimer le fichier
			echo -e "\nSuppression du fichier output/$2"
			rm -Rf output/$1
		else 								#SI l'utilisateur rentrer un mauvais choix
			echo -e "\nChoix incorrect" 
		fi
	done
fi

#Verification de l'existance du fichier $1
if [ ! -f $1 ]; then
	echo -e "Le fichier $1 n'existe pas"
	exit 0
fi

#Création fichier tmp/ if not exist
if [ ! -e tmp/ ]; then
	echo -e "Creation fichier tmp"
	mkdir tmp/
fi

#Netoyyage potentiel lancement antecedent
rm -Rf tmp/*

for letter in {A..Z}; do

	#Contage occurence + mise en forme + stockage dans un fichier count
	touch tmp/count
	uniq -c $1 | grep -e "$letter" > tmp/count

	#Mise en forme et stockage dans fichier counted
	touch tmp/counted
	echo "$letter - `wc tmp/count -l | cut -d " " -f 1`">> tmp/counted
done

#Affichage 
cat tmp/counted

#Exportation en fonction du 2eme parametre
echo -e "Exportation des resultat dans output/$2 en cours .."
cat tmp/counted > output/$2

#Nettoyage du fichier temporaire
echo -e "Nettoyage fichier temporaire en cours .."
rm -Rf tmp/

#Affichage message de fin
echo -e "DONE !"
