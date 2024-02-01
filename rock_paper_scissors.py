import random
output = random.randint(1, 3)

user_input = input("Enter rock, paper, scissors: ")

if user_input == "rock":
	if output == 1:
		print("Rock")
		print("Tie game!")
	elif output == 2:
		print("Paper")
		print("You lost!")
	else:
		print("Scissors")
		print("You win!")

if user_input == "paper":
	if output == 2:
		print("Paper")
		print("Tie game!")
	elif output == 1:
		print("Rock")
		print("You win!")
	else:
		print("Scissors")
		print("You lost!")

if user_input == "scissors":
	if output == 3:
		print("Scissors")
		print("Tie game!")
	elif output == 1:
		print("Rock")
		print("You win!")
	else:
		print("Paper")
		print("You lost!")