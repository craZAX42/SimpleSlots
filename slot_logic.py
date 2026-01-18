# slot_logic.py
# v0.1 - Console based app.
# We'll build most of the logic here.
# Input and output will be through the terminal at first (input() and print()).

# To run and test in VSCode, use the "Run Python File in Dedicated Terminal" button.
# This allows you to input values and hit "Enter" to send them back to the code.

import sys
import time
import random
from os import system
import threading

ALLOWED_SLOTS = ["X", "$", "#", "@", "%"]
IN_SLOT_MODE = False

# Create an Event object that acts as a flag
stop_slot_event = threading.Event()

def start_new_input_thread():
	input_thread = threading.Thread(target=user_input_listener, daemon=True)
	input_thread.start()

def user_input_listener():
	"""Runs in a separate thread to listen for user input."""
	while not stop_slot_event.is_set():
		if IN_SLOT_MODE:
			if sys.stdin in [sys.stdin]: # Check if input is available (works on most systems)
				user_input = input() # get input
				#print(f"Input: {user_input}")
				if not user_input:
					stop_slot_event.set()
					break

# TODO: Fill out a menu to print with options for the user.
# Available options:
#	[1]: Pull lever
#	[2]: Check earnings
#	[3]: Reset earnings
#	[4]: Leave slots
def print_menu():
    pass

def printSlotGrid():
	pass

def spin_slot():
	global IN_SLOT_MODE # allow function to edit global variable
	IN_SLOT_MODE = True
	print("Press Enter to stop slots...")
	while not stop_slot_event.is_set():
		slot_line = generateSlotLine()
		print(slot_line, end="\r", flush=True)
		was_set = stop_slot_event.wait(1) # Time inbetween slot lines
		if was_set:
			print(f"The slot you stopped on: {slot_line}.")
			is_winner = len(set(slot_line)) == 1
			if is_winner:
				print("\nYOU GOT A JACKPOT!!\n")
			else:
				print("\nBetter luck next time :)\n")
			break
	
	# system("clear||cls")
	IN_SLOT_MODE = False
	stop_slot_event.clear()
	start_new_input_thread()
	return

def generateSlotLine():
	# Generate a list symbols from the ALLOWED_SLOTS
	return [ALLOWED_SLOTS[random.randint(0, len(ALLOWED_SLOTS)-1)] for i in range(3)]


# TODO: Determine what happens when you pull the lever.
def pull_lever():
	spin_slot()

# TODO: Print out how much the user has won so far.
def check_earnings():
    pass

# TODO: Reset the user's earnings to 0.
def reset_earnings():
    pass

# TODO: Quit the program
def leave_slots():
    sys.exit()

def main():
	while True:
		print_menu()
		choice = input("Choice: ")
		# print(f"Choice was {choice}. Type is {type(choice)}")
		if not choice.isnumeric():
			print("Choice must be a number!")
			continue
		if choice == "1":
			pull_lever()
		elif choice == "2":
			pass
		elif choice == "3":
			pass
		elif choice == "4":
			leave_slots()

if __name__ == "__main__":
    start_new_input_thread()
    main()