#!/bin/bash
fct_menu ()
{
echo
echo "Choisissez une option [1-2]"
echo
echo "1 : programme Calcule IP"
echo "2 : programme Calculatrice"
echo "veuillez choisir :"

read optionmenu
	case $optionmenu in
	1)
		echo "lancement du programme 1"
		mainIp.py& ; exit;;
	2)
		echo "lancement du programme 2"
		mainCal.py& ; exit;;
	*)
		echo "erreur de frappe"
		fct_menu;;
		esac
}
fct_menu