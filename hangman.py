# using python version 3.6.1
import random

# initialize variables
words = ['ape', 'cat', 'dog', 'bird']
guessedLetters = []
win = False
play = True
wins = 0
losses = 0
guesses = 0
money = 50

# take the string word and convert it into an array of undercore strings with trailing spaces 
def initWordBlanks(word):
	# the only way to do anonymous functions in python is to use lambda
	# for example squaring each element is done by doing:
		# lambda x: x**2.
	blanks = map(lambda x: ' _ ', range(len(word)))
	return ''.join(blanks) #then convert the array into a string

def drawWord(word, guessedLets):
	drawnWord = ''
	for let in word:
	    if let in guessedLets:
	        drawnWord += let
	    else:
	    	drawnWord += ' _ '
	return drawnWord	

while (play):
	# reset guessedLetters to empty list
	guessedLetters = []

	# reset win to false
	win = False

	# choose a word
	word = random.choice(words)

	# make a list of letters in the word
	wordLetters = list(word)
	
	# make guesses 4 more than the word the length
	guesses = len(wordLetters) + 4

	print('you have $' + str(money)) 
	print('guesses left: ' + str(guesses))
	print(initWordBlanks(word))

	while (win == False) and (guesses > 0) and (money >= 5): 
		uc = input("Guess a letter. ")

		if (uc in guessedLetters):
			print('you already guessed: ' + uc)
		else:
			guessedLetters.append(uc)
			
			if uc in wordLetters:
				money += 5
				print('you got it')
			else:
				print('you did not get it')
				guesses -= 1
				money -= 5

			drawnWord = drawWord(word, guessedLetters)

			# if the drawnWord is equal to the word then the player has won this round
			win = drawnWord == word

			print('')
			print('')
			print('-----------------')
			print(drawnWord)
			print('you have $' + str(money)) 
			print('guesses left: ' + str(guesses))
			print('guessed letters: ' + str(guessedLetters))
			print('-----------------')

	if win:
		money += 15
		print('You won!')
	elif guesses == 0:
		money -= 15
		print('You lost')

	print('you have $' + str(money)) 

	if money >= 5:
		play = input("Want to play again? Type y or n. ") == 'y'
	else:
		play = False
		print('You do not have enough money to play this game.')
else:
	print('you have $' + str(money)) 
	print('you have won ' + str(wins) + ' times') 
	print('you have lost ' + str(losses) + ' times') 