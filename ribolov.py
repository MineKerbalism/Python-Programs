import random
import time

user_choice = 0
fish = 0
prime_time = 0
time = 0



while True:
	if user_choice == 2:
		break
	
	strenght = random.randint(1, 4)
	timer = random.randint(1, 4)
	
	user_action = input("Please load on some bait to continue by entering 1. ")	
	
	if user_action == 1:
		user_throw = input("Now throw with 2 and let's see what we can catch! ")
		if user_throw == 2:
			print("And now we wait...")
			time.sleep(3.00)
		while True:
			struggle = 0
			time = time + 1
			prime_time = prime_time + 1 
		
			if time == timer:
				struggle = input("Oh, something's on!Pull!!! ")
				time.sleep(3.00)
				if struggle == strenght:
					print("You caught something!")
					fish = fish + 1
					user_choice = input("Up for another game? Choose 1 for yes and 2 for no: ")
					if user_choice == 1:
						print("Ok, let's do it!")
						time = 0
						break
					elif user_choice == 2:
						if fish == 0:
							print("You caught " + str(fish) + " fish. Maybe next time! Ok, see you!")
						else:
							print("Ok, see you next time! By the way you caught " + str(fish) + " fish. Sweet!")
					time = 0
					break
				else:
					print("Bad luck, it got away!")
					user_choice = input("Up for another game? Choose 1 for yes and 2 for no: ")
					if user_choice == 1:
						print("Ok, let's do it!")
						time = 0
						break
					elif user_choice == 2:
						if fish == 0:
							print("You caught " + str(fish) + " fish. Maybe next time! Ok, see you!")
						else:
							print("Ok, see you next time! By the way you caught " + str(fish) + " fish. Sweet!")
							time = 0
							break
			elif timer == 4:
				print("Looks like we got an empty pond today!")
				user_choice = input("Up for another game? Choose 1 for yes and 2 for no: ")
				if user_choice == 1:
					print("Ok, let's do it!")
					time = 0
					break
				elif user_choice == 2:
					if fish == 0:
						print("You caught " + str(fish) + " fish. Maybe next time! Ok, see you!")
					else:
						print("Ok, see you next time! By the way you caught " + str(fish) + " fish. Sweet!")
					time = 0
					break