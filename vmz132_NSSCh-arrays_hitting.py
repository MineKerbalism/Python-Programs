import random
import time

daljina_pole = 50
broy_igrachi = 8
tekusht_igrach = 0
pozicii = [0]*8
simvol_igrachi = ['I', 'A', 'T', 'V', 'N', 'F', 'G', 'D']

while True:
	zar = random.randint(1, 6)

	if pozicii[tekusht_igrach] >= 0:
		sledIliPredi = input("Would you like to see the number you rolled (say True or False): ")
		if sledIliPredi == True:
			print("Player " + simvol_igrachi[tekusht_igrach] + " threw " + str(zar))
			napredIliNazad = input("Would you like to go forward or backward (say 0 for forward and 1 for backward): ")
			if napredIliNazad == 0:
				zar = zar
			if napredIliNazad == 1:
				zar = -zar
		if sledIliPredi == False:
			print("Ok, we will not show you what you rolled.")
			napredIliNazad = input("Would you like to go forward or backward (say 0 for forward and 1 for backward): ")
			if napredIliNazad == 0:
				zar = zar
			if napredIliNazad == 1:
				zar = -zar

	if pozicii[tekusht_igrach] < 0:
		pozicii[tekusht_igrach] = 0

	
	if pozicii[tekusht_igrach] + zar <= daljina_pole:
		nova_poziciya = pozicii[tekusht_igrach] + zar
		for index_stari_pozicii in range(broy_igrachi):
			if nova_poziciya == pozicii[index_stari_pozicii]:
				pozicii[index_stari_pozicii] = 0
		pozicii[tekusht_igrach] = nova_poziciya
		print("Player " + simvol_igrachi[tekusht_igrach] + " threw " + str(zar) + " and is now on position " + str(pozicii[tekusht_igrach]))


	for tekushta_poziciya in range(1, daljina_pole + 1):
		simvol_za_izvejdane = '_'
		for index_igrach in range(broy_igrachi):
			if tekushta_poziciya == pozicii[index_igrach]:
				simvol_za_izvejdane = simvol_igrachi[index_igrach]
		
		print(simvol_za_izvejdane),
	print
	time.sleep(2)

	if pozicii[tekusht_igrach] >= daljina_pole:
		print("Player " + simvol_igrachi[tekusht_igrach] + " won the game!")
		break

	sledvasht_igrach = tekusht_igrach + 1
	if sledvasht_igrach == broy_igrachi:
		sledvasht_igrach = 0
	tekusht_igrach = sledvasht_igrach