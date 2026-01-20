# slot_logic.py
# v0.1 - Console based app.
# We'll build most of the logic here.
# Input and output will be through the terminal at first (input() and print()).

# To run and test in VSCode, use the "Run Python File in Dedicated Terminal" button.
# This allows you to input values and hit "Enter" to send them back to the code.

# Kavika's TODO
# [] print multiple slots at a time
# [] think of more menu options

# Jordan's TODO
# [X] print_menu()
# [X] earnings functionality - print current earnings, reset earnings, maybe a way to lose earnings? (Cost of spinning)

# Eventually TODO
# [] Add a bet amount with min/max (or no limit) JACKPOT_MULTIPLIER * bet_amount
# [] Add more variability to the ALLOWED_SLOTS (different rarities with different payouts)
# [] Menu repeats itself after each action until user exits, make it only display when the user wants to see it
# [] Always display the current token amount when the user is playing
# [] 

import sys
import time
import random
from os import system
import threading

ALLOWED_SLOTS = ["X", "$", "#", "@", "%"]
IN_SLOT_MODE = False
JACKPOT_MULTIPLIER = 100 # current odds are 1 in 125 so payout needs to be less than the odds
current_tokens = 0 # Ideally the user's tokens would be stored in a user profile or database (can go negative if they owe the casino)

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
#	[2]: Check tokens
#	[3]: Add to tokens
#	[4]: Leave slots
def print_menu():
	print("=== SLOT MACHINE MENU ===")
	print("1: Pull lever")
	print("2: Check tokens")
	print("3: Add to tokens")
	print("4: Cash out or pay balance")
	print("5: Leave slots")

def printSlotGrid():
	pass

def new_token_balance():
	print(f'You now have {current_tokens} tokens!')

def spin_slot():
	global IN_SLOT_MODE # allow function to edit global variable
	IN_SLOT_MODE = True
	global current_tokens
	print("Press Enter to stop slots...")
	while not stop_slot_event.is_set():
		slot_line = generateSlotLine()
		print(slot_line, end="\r", flush=True)
		was_set = stop_slot_event.wait(1) # Time inbetween slot lines
		if was_set:
			print(f"The slot you stopped on: {slot_line}.")
			is_winner = len(set(slot_line)) == 1
			if is_winner:
				current_tokens += JACKPOT_MULTIPLIER # add mulitplier or bet amount later
				print("\nYOU GOT A JACKPOT!!\n")
				new_token_balance()
			else:
				current_tokens -= 1 # add mulitplier or bet amount later
				print("\nBetter luck next time :)\n")
				new_token_balance()
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

def check_tokens():
    print(f'You currently have {current_tokens} tokens!')

# TODO: Cash out or pay balance if negative (basically resets tokens to 0).
def cashout_or_pay_balance():
	global current_tokens
	if current_tokens > 0:
		print(f'You cashed out {current_tokens} tokens. Enjoy your winnings!')
	elif current_tokens < 0:
		print(f'You owe the casino {current_tokens} tokens. Please settle your balance.')
	else:
		print('You have no tokens to cash out or owe.')
	current_tokens = 0

# TODO: Add tokens to the user's balance. 
def add_to_tokens():
	global current_tokens
	amount = input("Enter amount of tokens to add: ")
	if (not amount.isnumeric()) and (int(amount) < 0):
		print("Amount must be a number and greater than 0!") 
		return
	current_tokens += int(amount)
	new_token_balance()

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
			check_tokens()
		elif choice == "3":
			add_to_tokens()
		elif choice == "4":
			cashout_or_pay_balance()
		elif choice == "5":
			leave_slots()

if __name__ == "__main__":
    start_new_input_thread()
    main()