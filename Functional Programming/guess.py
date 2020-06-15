secret_number = 9


def guess_game():
	easy, normal, hard = 5, 3, 2
	print('''
Welcome to the Guessing game! Select a Level..''')

	choose = input("Select an option (E)asy, (N)ormal, (H)ard: ")

	if choose.upper() == "E":
		print("You have selected Easy mode.")
		guess = int(input('Guess: '))
		easy -= 1
		print(f"Wrong! Try again..\nYou have {easy} remaining.")

	while easy < 5:
		guess = int(input('Guess: '))
		easy -= 1
		if easy < 5:
			print(f"Wrong! Try again..\nYou have {easy} remaining")
		if guess <= 0:
			print("GAME OVER! YOU HAVE NO TRAILS LEFT!!")
		elif guess == secret_number:
			print('CONGRATULATIONS. YOU WON!!')

	if choose.upper() == "N":
		print("You have selected Normal mode.")
		guess = int(input('Guess: '))
		normal -= 1
		print(f"Wrong! Try again..\nYou have {normal} remaining")

		while normal < 3:
			normal -= 1
			if normal < 0:
				print(f"Wrong! Try again..\nYou have {normal} remaining")
			elif guess == secret_number:
				print('CONGRATULATIONS. YOU WON!!')
			elif normal == 0:
				print("GAME OVER! YOU HAVE NO TRAILS LEFT!!")
			else:
				pass

	if choose.upper() == "H":
		print("You have selected Hard mode.")
		guess = int(input('Guess: '))
		hard -= 1
		print(f"Wrong! Try again..\nYou have {hard} remaining")

	while hard < 2:
		guess = int(input('Guess: '))
		hard -= 1
		if guess < hard:
			print(f"Wrong! Try again..\nYou have {hard} remaining")
		elif guess == secret_number:
			print('CONGRATULATIONS. YOU WON!!')
		elif hard == 0:
			print("GAME OVER! YOU HAVE NO TRAILS LEFT!!")
		else:
			break



guess_game()