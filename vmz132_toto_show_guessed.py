import random

size = 6
tiraj = [0] * size
moi_chisla = [0] * size
broi_poznati_chisla = 0
poznati_chisla = []

for index in range(size):
	tiraj[index] = random.randint(0, 49)

for index in range(size):
	moi_chisla[index] = input("Enter a number from 0 to 49: ")

for index_vavedeni in range(size):         
    for index_iztegleni in range(size):    
        if moi_chisla[index_vavedeni] == tiraj[index_iztegleni]:
            broi_poznati_chisla = broi_poznati_chisla + 1
            poznati_chisla.extend([moi_chisla[index_vavedeni]])


print("Number of guessed numbers: " + str(broi_poznati_chisla))
print("You guessed correctly the numbers: ")
print(poznati_chisla)
print("The numbers that were picked in the TOTO were: ")

for index in range(size):
	print(" " + str(tiraj[index])),


