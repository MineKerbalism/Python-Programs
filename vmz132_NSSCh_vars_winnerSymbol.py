import time
import random

poziciya_1 = 0
poziciya_2 = 0
poziciya_3 = 0
poziciya_4 = 0
daljina_pole = 50

while True:
	zar_1 = random.randint(1, 6)
	if poziciya_1 + zar_1 <= daljina_pole:
		poziciya_1 = poziciya_1 + zar_1
	
	zar_2 = random.randint(1, 6)
	if poziciya_2 + zar_2 <= daljina_pole:
		poziciya_2 = poziciya_2 + zar_2

	zar_3 = random.randint(1, 6)
	if poziciya_3 + zar_3 <= daljina_pole:
		poziciya_3 = poziciya_3 + zar_3

	zar_4 = random.randint(1, 6)
	if poziciya_4 + zar_4 <= daljina_pole:
		poziciya_4 = poziciya_4 + zar_4

		for tekushta_poziciya in range(1, daljina_pole + 1):
			simvol_za_izvejdane = "_"

			if tekushta_poziciya == poziciya_1:
				simvol_za_izvejdane = "A"
			if tekushta_poziciya == poziciya_2:
				simvol_za_izvejdane = "I"
			if tekushta_poziciya == poziciya_3:
				simvol_za_izvejdane = "T"
			if tekushta_poziciya == poziciya_4:
				simvol_za_izvejdane = "V"
			
			if simvol_za_izvejdane != "_":
				time.sleep(0.2)
			else:
				time.sleep(0.01)

			print(simvol_za_izvejdane),

		print("'A' rolled: " + str(zar_1)),
		print("'I' rolled: " + str(zar_2)),
		print("'T' rolled: " + str(zar_3)),
		print("'V' rolled: " + str(zar_4))

		if poziciya_1 == daljina_pole:
			print("'A' wins!")
			break
		if poziciya_2 == daljina_pole:
			print("'I' wins!")
			break
		if poziciya_3 == daljina_pole:
			print("'T' wins!")
			break
		if poziciya_4 == daljina_pole:
			print("'V' wins!")
			break


