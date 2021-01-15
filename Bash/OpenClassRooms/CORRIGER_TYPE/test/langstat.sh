#!/bin/bash
if [ -z $1 ]
then
echo 'veuillez indiquer votre fichier'
elif [ $1 != "dico.txt" ]
then
echo 'votre fichier n est pas dico.txt'
# si le 2eme parametre est i alors le résultat serait inversé
if [[ $2 = "i" ]]
then 
echo 'le résultat est inversé'
    for var in `echo {A..Z}`
    do
    echo "`grep -c $var $1` - $var" 

    done | sort -n
else
  for var in `echo {A..Z}`
    do
    echo "`grep -c $var $1` - $var" 

    done | sort -nr
fi
elif [ $1 = "dico.txt" ] 
then 
echo 'votre fichier est bien dico.txt'

if [[ $2 = "i" ]]
then 
echo 'le résultat est inversé'
    for var in `echo {A..Z}`
    do
    echo "`grep -c $var $1` - $var" 

    done | sort -n
else
    for var in `echo {A..Z}`
    do
    echo "`grep -c $var $1` - $var" 

    done | sort -nr
fi
fi


