import random

size = 6
tiraj = [0] * size
lyubimo_chislo = 21

for index in range(size):
	tiraj[index] = random.randint(0, 49)

if tiraj[index] == lyubimo_chislo:
	print("Your number has been picked in the TOTO! It's index is: " + str(index))
	print("The TOTO numbers were: ")
	for index in range(size):
		print(tiraj[index])
else:
	print("Your number was not picked in the TOTO.")
	print("The TOTO numbers were: ")
	for index in range(size):
		print(tiraj[index])
