#This program prompts the user to select rock, paper or scissors, and then determines a winner.
from random import randint
from time import sleep
OPTIONS = ["R","P","S"]
LOSER = "You lose!"
WINNER = "You Win!"
def decide_winner(user_choice,computer_choice):
	print("The user chose %s" % (user_choice))
	print("Computer selecting...")
	sleep(1)
	print("The computer chose %s" % (computer_choice))
	user_choice_index = OPTIONS.index(user_choice)
	computer_choice_index = OPTIONS.index(computer_choice)
	if user_choice_index == computer_choice_index:
		print("It's a tie!")
	elif user_choice == "R" and computer_choice == "S":
		print(WINNER)
	elif user_choice == "P" and computer_choice == "R":
		print(WINNER)
	elif user_choice == "S" and computer_choice == "P":
		print(WINNER)
	elif user_choice_index > 3:
		print("Invalid choice")
		return
	else:
		print(LOSER)
    
def play_RPS():
	print("This is Rock, Paper, Scissors!")
	user_choice = input("Select R for Rock, P for Paper, or S for Scissors:").upper()
	sleep(1)
	computer_choice = OPTIONS[randint(0,len(OPTIONS)-1)]
	decide_winner(user_choice,computer_choice)
play_RPS()
