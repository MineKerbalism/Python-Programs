import random
import time


computerGuess = random.randint(1, 1000)
attempts = 0
minimum = 1
maximum = 1000

print("Think of a number from 1 to 1000. The computer will try and guess it in 10 tries.")
time.sleep(5)
while attempts <= 10:
	attempts = attempts + 1
	print("")
	didGuess = input("The computer guessed: " + str(computerGuess) + " Did it guess correctly? If yes, type 1, if no, type 2: ")
	if didGuess == 1:
		print("")
		print("The computer guessed your number. It guessed " + str(computerGuess))
		break
	if didGuess == 2:
		print("")
		upOrDown = input("It seems like the computer is wrong. Is your number higher or lower than what the computer guessed? Type 1 for higher, or 2 for lower: ")
		if upOrDown == 1:
			minimum = computerGuess
			computerGuess = (minimum + maximum) / 2
		if upOrDown == 2:
			maximum = computerGuess
			computerGuess = (maximum + minimum) / 2
		if maximum - minimum <= 1:
			if didGuess == 2:
				print("")
				print("What you are saying is logically impossible. You are lying!")
if didGuess == 2:
	print("")
	print("The computer ran out of tries. It couldn't guess your number.")