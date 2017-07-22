#The program simulates the throw of a pair of dice and then asks the user to guess a number. If the user's guess is greater than the total value of the dice roll, they win.
from random import randint
from time import sleep
def get_user_guess():
  user_guess = int(input("Guess a number: "))
  return user_guess
def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides*2
  print("Maximum possible value is " + str(max_val))
  sleep(1)
  user_guess = get_user_guess()
  if user_guess > max_val:
  	print("Your guess is larger than the maximum possible value")
  	return
  else:
    print("Rolling...")
    sleep(2)
    print("First dice is {:d}".format(first_roll))
    sleep(1)
    print("Second dice is {:d}".format(second_roll))
    sleep(1)
    total_roll = first_roll + second_roll
    print(total_roll)
    print("Result...")
    sleep(1)
    if user_guess > total_roll:
      print("you won!")
    else:
    	print("you lose")
    return
roll_dice(6)