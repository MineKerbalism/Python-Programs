number1 = input("What is the first number: ")
number2 = input("What is the second number: ")
operation = input("What is the operation you want to have: ")
if operation == Multiplication:
	answer = number1 * number2
if operation == Division:
	answer = number1 / number2
if operation == Addition:
	answer = number1 + number2
if operation == Subtraction:
	answer = number1 - number2
print("The answer is: " + str(answer))