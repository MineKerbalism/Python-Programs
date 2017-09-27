import random
import time

humanWins = 0
computerWins = 0

while True:
	computerChoice = random.randint(1, 3)
	humanChoice = input("Enter: 1 - rock, 2 - scissors, 3 - paper ")
	if humanChoice == computerChoice:
		print("Draw!")

	if humanChoice == 1:
		if computerChoice == 2:
			print("You win! The computer chose scissors.")
			humanWins = humanWins + 1
		if computerChoice == 3:
			print("You lose! The computer chose paper.")
			computerWins = computerWins + 1

	if humanChoice == 2:
		if computerChoice == 3:
			print("You win! The computer chose paper.")
			humanWins = humanWins + 1
		if computerChoice == 1:
 			print("You lose! The computer chose rock.")
 			computerWins = computerWins + 1

	if humanChoice == 3:
		if computerChoice == 1:
			print("You win! The computer chose rock")
			humanWins = humanWins + 1
		if computerChoice == 2:
			print("You lose! The computer chose scissors")
			computerWins = computerWins + 1

	print("The current result is: " + str(humanWins) + " wins for the player, and " + str(computerWins) + " wins for the computer. ")
	time.sleep(2)
	endGame = input("Do you want to continue playing? Type 1 - yes or 2 - no: ")

	if endGame == 1:
		print("Ok, continuing your game.")

	if endGame == 2:
		print("Ending game.")
		print("The end result is: " + str(humanWins) + " wins for the player, and " + str(computerWins) + " wins for the computer. ")
		break
