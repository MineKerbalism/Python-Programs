import time
import random

moya_poziciya = 0
daljina_pole = 50
entered = False

while True:
	zar = random.randint(1, 6)
	if entered == False and zar == 6:
		entered = True
	if moya_poziciya + zar <= daljina_pole:
		moya_poziciya = moya_poziciya + zar
	print("Number rolled: " + str(zar))
	if entered == True:
		for tekushta_poziciya in range(1, daljina_pole + 1):
			if tekushta_poziciya == moya_poziciya:
				print("i"),
				time.sleep(0.1)
			else:
				print("_" + str(tekushta_poziciya)),
				time.sleep(0.1)

		if moya_poziciya == daljina_pole:
			break
			print("You win!")

