board = [
	['X', 'X', 'X'],
	['O', 'X', 'O'],
	['O', 'O', 'X']
]
 
for row in range(3):
	print(board[row])
 
winner = ''

# TODO 1 : check rows
 
found = False
row = 0
while (not found and row<len(board)):
	if (board[row][0]==board[row][1] and board[row][0]==board[row][2] and board[row][0]!=" "):
		found = True
		winner = board[row][0]
	else:
		row+=1

# TODO 2 : check columns

found = False
col = 0
while (not found and col<len(board[0])):
	if (board[0][col]==board[1][col] and board[0][col]==board[2][col] and board[0][col]!=" "):
		found = True
		winner = board[0][col]
	else:
		col+=1

# TODO 3: check diagonals

if (board[0][0]==board[1][1] and board[0][0]==board[2][2]) or (board[0][2]==board[1][1] and board[0][2]==board[2][0]):
	winner=board[1][1]
 
# # TODO 4: report the result

if winner == '':
	print('No winner')
else:
    print(winner, 'has won')
