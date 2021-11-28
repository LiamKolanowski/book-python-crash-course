'''
desired game output (from book, page: xxxiii of 508, location 676 of 13854 ):
 
I'm thinking of a number! Try to guess the number I'm thinking of: 25
Too low! Guess again: 50
Too high! Guess again: 42
That's it! Would you like to play again? (yes/no) no
Thanks for playing!
'''

import random

def play_game(npc_number, message_to_user):

	#print(f'THE NUMBER: {npc_number}')
	user_guess = int(input(message_to_user))
	random_number = npc_number
	play_again = 'yes'

	while(1):

		if (user_guess < random_number):
			play_game(random_number, "Too low! Guess again: ")

		elif (user_guess > random_number):
			play_game(random_number, "Too high! Guess again: ")

		else:
			play_again = input("That's it! Would you like to play again? (yes/no) ")
			if (play_again == 'yes'):
				play_game(random.randint(1, 100), "I'm thinking of a number! Try to guess the number I'm thinking of: ")
			else:
				print("Thanks for playing!")
			
		break

		


play_game(random.randint(1, 100), "I'm thinking of a number! Try to guess the number I'm thinking of: ")



