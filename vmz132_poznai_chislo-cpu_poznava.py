import random
import time

computerGuess = random.randint(1, 20)
humanInput = input("Enter a number from 1 to 20: ")

while humanInput != computerGuess:
	print("The computer tried to guess your number but guessed incorrectly. It guessed: " + str(computerGuess))
	time.sleep(1)
	computerGuess = random.randint(1, 20)

print("The computer guessed your number! It guessed: " + str(computerGuess))
