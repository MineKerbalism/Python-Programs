import random

randomNumber = random.randint(1, 20)
myNumber = input("Enter a number from 1 to 20: ")
while randomNumber != myNumber:
	print("You are not correct!")
	myNumber = input("Try again! Enter a number from 1 to 20: ")
	
print("You guessed the number!")