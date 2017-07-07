# using python version 3.6.1
import random

# initialize variables
play = True
wins = 0
losses = 0
ties = 0
money = 50

while play:
	print('you have $' + str(money)) 
	uc = input("Choose r, p or s ")
	cc = random.choice(['r', 'p', 's'])

	if uc == cc:
		ties += 1
		print('you tied with the computer!')
	elif (uc == 'r' and cc == 's') or (uc == 'p' and cc == '') or (uc == 'p' and cc == ''):
		wins += 1
		money += 10
		print('you beat the computer!')
	else:
		losses += 1
		money -= 10
		print('computer beat you')

	print('-----------------')
	print('you have $' + str(money)) 
	print('wins :' + str(wins))
	print('losses :' + str(losses))
	print('ties :' + str(ties))
	print('-----------------')

	if money >= 5:
		play = input("play again? y or n ") == "y"
	else:
		print('You do not have enough money! You are done.')
		play = False