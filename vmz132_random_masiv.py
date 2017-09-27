import random

size = 50
oneToAHundred = [0] * size

for index in range(size):
	oneToAHundred[index] = random.randint(0, 100)

for index in range(size):
	print(oneToAHundred[index])
