import time
import random

poziciya_1 = 0
poziciya_2 = 0
poziciya_3 = 0
poziciya_4 = 0
daljina_pole = 50
entered = False

while True:
	zar = random.randint(1, 6)
	if entered == False and zar == 6:
		entered = True
	
	if poziciya_1 + zar <= daljina_pole:
		poziciya_1 = poziciya_1 + zar
	
	zar = random.randint(1, 6)
	if entered == False and zar == 6:
		entered = True	
	
	if poziciya_2 + zar <= daljina_pole:
		poziciya_2 = poziciya_2 + zar

	zar = random.randint(1, 6)
	if entered == False and zar == 6:
		entered = True	
	
	if poziciya_3 + zar <= daljina_pole:
		poziciya_3 = poziciya_3 + zar

	zar = random.randint(1, 6)
	if entered == False and zar == 6:
		entered = True	
	
	if poziciya_4 + zar <= daljina_pole:
		poziciya_4 = poziciya_4 + zar

	if entered == True:
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
			
			print(simvol_za_izvejdane),

		print("Number rolled: " + str(zar))

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


