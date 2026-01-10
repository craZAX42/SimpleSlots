# slot_logic.py
# v0.1 - Console based app.
# We'll build most of the logic here.
# Input and output will be through the terminal at first (input() and print()).

# To run and test in VSCode, use the "Run Python File in Dedicated Terminal" button.
# This allows you to input values and hit "Enter" to send them back to the code.

import sys

# TODO: Fill out a menu to print with options for the user.
# Available options:
#	[1]: Pull lever
#	[2]: Check earnings
#	[3]: Reset earnings
#	[4]: Leave slots
def print_menu():
    pass

# TODO: Determine what happens when you pull the lever.
def pull_lever():
    pass

# TODO: Print out how much the user has won so far.
def check_earnings():
    pass

# TODO: Reset the user's earnings to 0.
def reset_earnings():
    pass

# TODO: Quit the program
def leave_slots():
    sys.exit()
    pass

def main():
    # print('Starting slot logic...\n')
    
	while True:
		print_menu()
		
		choice = input("Choice: ")
		if choice == 4:
			leave_slots()
    
if __name__ == '__main__':
    main()