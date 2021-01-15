#!/bin/bash

while [[ $answer != "y" ]] && [[ $answer != "n" ]]; do
	echo -e "Le fichier $2 existe deja dans le fichier output.\n"
	read -p "Voulez vous supprimer se fichier ? taper 'Y' pour le supprimer " -n 1 answer
	echo -e "\n"

	#Converstion de la reponse en petit caractere
	answer=`echo "${answer,,}"`
	echo -e "$answer\n"
done