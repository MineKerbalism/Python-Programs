import random
import time

daljina_pole = 50
broy_igrachi = 8
tekusht_igrach = 0
pozicii = [1, 5, 3, 8, 9, 7, 4, 12]
simvol_igrachi = ['i', 'a', 't', 'v', 'n', 'f', 'g', 'd']

for tekushta_poziciya in range(1, daljina_pole + 1):
	simvol_za_izvejdane = '_'

	for index_igrach in range(broy_igrachi):
		if tekushta_poziciya == pozicii[index_igrach]:
			simvol_za_izvejdane = simvol_igrachi[index_igrach]

while True:
	zar = random.randint(1, 6)
	if pozicii[tekusht_igrach] + zar <= daljina_pole:
		nova_poziciya = pozicii[tekusht_igrach] + zar
		pozicii[tekusht_igrach] = nova_poziciya
	
	if pozicii[tekusht_igrach] >= daljina_pole:
		print("Player " + simvol_igrachi[tekusht_igrach] + " won the game!")
		break

	sledvasht_igrach = tekusht_igrach + 1
	if sledvasht_igrach == broy_igrachi:
		sledvasht_igrach = 0
	tekusht_igrach = sledvasht_igrach

	
	print(simvol_za_izvejdane),
	time.sleep(2)