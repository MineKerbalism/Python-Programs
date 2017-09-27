import random

randomNumber = random.randint(1, 20)
myNumber = input("Enter a number from 1 to 20: ")
count = 0
while count < 2:
	if myNumber != randomNumber:
		print("You guessed incorrectly!")
		myNumber = input("Try again: ")
		count = count + 1
	else:
		print("You guessed correctly!")
		break

print("Incorrect! You can only guess 3 times. You ran out of tries! The correct number was: " + str(randomNumber))