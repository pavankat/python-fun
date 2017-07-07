board = [['_','_','_'], ['_','_','_'], ['_','_','_']]
win = False
tie = False

def printBoard():
	print(board[0])
	print(board[1])
	print(board[2])

def computerChooose():
	# use the minimax algorithm
	# http://neverstopbuilding.com/minimax


print('you are X\'s and the computer is O\'s')
printBoard()

while (not win or  not tie):
	# use a tuple so I can take the input and put them in x and y. 
	# take in the input (as a string), remove commas, remove spaces, map over each element in the string and typecast to integer then convert to tuple so the results go into x and y
	userChoice = input('choose a row and column. 1,1 will get you the top left choice. 3,3 will get you the bottom right choice.').replace(',','').replace(' ', '')
	x, y = tuple(map(int, userChoice))

	# subtract 1 from x and y b/c lists start at 0 and not at 1
	if board[x-1][y-1] == '_':
		board[x-1][y-1] = 'X'
	else:
		print('can\'t pick that one')

	printBoard()