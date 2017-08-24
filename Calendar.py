#This basic calendar program allows the user to view her schedule, add events, update events and delete existing events.
from time import sleep, strftime
USER_NAME = raw_input("What is your name? ")
calendar = {}
def welcome():
  print("Welcome " + USER_NAME)
  print('The calendar is opening')
  sleep(1)
  print(strftime("%A %B %d %Y"))
  print(strftime("%H:%M:%S"))
  sleep(1)
def start_calendar():
  welcome()
  start = True
  while start == True:
    user_choice = raw_input('Choose A to Add, U to Update, V to View, D to Delete, X to Exit: ')
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print("There are no events on the calendar")
      else:
        print(calendar)
    elif user_choice == 'U':
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print('Update succesful!')
      print(calendar)
    elif user_choice == 'A':
      event = raw_input('Enter event: ')
      date = raw_input('Enter date (MM/DD/YYYY): ')
      if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print("You entered an invalid date")
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again.upper()
        if try_again == 'Y':
          continue
        else:
          break
      else:
        calendar[date] = event
        print("The event was succesfully added!")
        print(calendar)
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print("The calendar is empty")
      else:
        event = raw_input('What event?')
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print("The event was succesfullly deleted")
          else:
            print("An incorrect event was specified")
    elif user_choice == "X":
    	start = False
    else:
      print("An invalid command was entered")
      break
      
start_calendar()