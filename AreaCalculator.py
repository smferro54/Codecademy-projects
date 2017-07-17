# A calculator than can compute the area of a given shape, as selected by the user. The calculator will be able to determine the area of the following shapes:
# Circle
# Triangle

from math import pi
from time import sleep
from datetime import datetime
now = datetime.now()
print("Calculator is starting up")
Curr = "Current date is {}/{}/{} {}:{}".format(now.month, now.day, now.year, now.hour, now.minute)
print(Curr)
sleep(1)
hint = "Don't forget to include the correct units! \nExiting..."
option = input("Enter C for Circle or T for Triangle ->").upper()
while (option == "C" or option == "T") is False:
  	option = input("Try again, enter C for Circle or T for Triangle ->").upper()
if option == 'C':
	while True:
		try:
			radius = float(input("Enter radius ->"))
			break
		except ValueError:
			print('That was not a valid number, try again')
	area = pi*radius**2
	print('The pie is baking...')
	sleep(1)
	print("%.2f \n%s" % (area,hint))
elif option == 'T':
	while True:
		try:
			base = float(input("Enter base ->"))
			break
		except ValueError:
			print('That was not a valid number, try again')
	while True:
		try:
			height = float(input("Enter height ->"))
			break
		except ValueError:
			print('That was not a valid number, try again')
	area = base*height/2
	print('Uni Bi Tri...')
	sleep(1)
	print("%.2f \n%s" % (area,hint))
else:
	print("Invalid choice, exiting...")
  
  