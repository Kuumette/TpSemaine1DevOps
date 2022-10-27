#!/bin/bash
# fct_menu ()
# {
echo
echo "Choisissez une option [1-2]"
echo
echo "1 : programme Calcule IP"
echo "2 : programme Calculatrice"
echo "veuillez choisir :"

read optionmenu
	case $optionmenu in
	"1" )
		echo "lancement du programme 1"
		python3 mainIp.py ;;
		
	"2" )
		echo "lancement du programme 2"
		python3 mainCal.py ;;
	
	esac
	# if [ $optionmenu == 1 ]; then
	# 	#echo "1"
	# 	python3 mainIp.py 
	# elif [ $optionmenu == 2 ]; then
	# 	echo "2"
	# 	python3 mainCal.py
	# fi
# }
# fct_menu
