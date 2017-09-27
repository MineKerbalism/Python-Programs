import random

size = 6
tiraj = [0] * size
moi_chisla = [0] * size

for index in range(size):
	tiraj[index] = random.randint(0, 49)

for index in range(size):
	moi_chisla[index] = input("Enter a number from 0 to 49: ")