import time

moya_poziciya = 0
daljina_pole = 50

while True:
	for tekushta_poziciya in range(1, daljina_pole + 1):
		if tekushta_poziciya == moya_poziciya:
			print("i"),
			time.sleep(0.1)
		else:
			print("_" + str(tekushta_poziciya)),
			time.sleep(0.1)
	print("")
	moya_poziciya = moya_poziciya + 1
	if moya_poziciya >= daljina_pole:
		break

