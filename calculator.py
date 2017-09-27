print("------==<CALCULATOR>==------")

answer = 0
times_used = 0

while True: 
	if times_used > 0:
		use_previous = raw_input("Do you want to use the previous answer as your first number? ")
		first_number = input("Type a number: ")
		operation = raw_input("What operation: ").lower()
		second_number = input("Type a second number: ")
	elif times_used ==0  :
		first_number = input("Type a number: ")
		operation = raw_input("What operation: ").lower()
		second_number = input("Type a second number: ")		

	if use_previous == "yes" and times_used > 0:

		if operation == "+":
			answer = answer + second_number
			print("Answer = " + str(answer))
			times_used = times_used + 1

		elif operation == "x" or operation == "*":
			answer = answer * second_number
			print("Answer = " + str(answer))
			times_used = times_used + 1

		elif operation == "/":
			answer = answer / second_number
			print("Answer = " + str(answer))
			times_used = times_used + 1

		elif operation == "-":
			answer = answer - second_number
			print("Answer = " + str(answer))
			times_used = times_used + 1

	else:

		if operation == "+":
			answer = first_number + second_number
			print("Answer = " + str(answer))
			times_used = times_used + 1

		elif operation == "x" or operation == "*":
			answer = first_number * second_number
			print("Answer = " + str(answer))
			times_used = times_used + 1

		elif operation == "/":
			answer = first_number / second_number
			print("Answer = " + str(answer))
			times_used = times_used + 1

		elif operation == "-":
			answer = first_number - second_number
			print("Answer = " + str(answer))
			times_used = times_used + 1

