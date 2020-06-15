 #In this Tic-Tac-Toe application, I'll be listening funtions that we'll be using.
# And this funtions will basically give/tell:

'''
1. Check for Winner.
- check rows
- check columns
- check diagonals
2. Check Tie(that is, if there's a winner)
3. Flip player
4. Handle turns
'''

# --------------- Global Variables -------------

# Game Board
board = ["–", "–", "–",
		 "–", "–", "–",
		 "–", "–", "–"]

# If game is still going
game_still_going = True 

# Who won? Or tie?
winner = None

# Who's turn is it?'
current_player = 'X'

# Display board
def display_board():
	print(board[0] + " I " + board[1] + " I " + board[2])
	print(board[3] + " I " + board[4] + " I " + board[5])
	print(board[6] + " I " + board[7] + " I " + board[8])

# Play a game of Tic Tac Toe
def play_game():

	# Display initial board
	display_board()

	while game_still_going:

		# Handle a single turn of an arbitrary player
		handle_turn(current_player)

		# Check if the game has ended
		check_if_game_over()

		# Flip to the other player
		flip_player()

   # The game has ended
 
if winner == 'X' or winner == 'O':
	print(winner + " won!")
elif winner == None:
	print("It's a Tie!")


def handle_turn(player):

	print(player + "'s turn.")
	position = input("Choose a position from 1-9: ")
	
	if position not in ["1", "2", "3", "4", "5","6", "7", "8", "9"]:
		position = input("Invalid input. Choose a position from 1-9: ")
		
	position = int(position) - 1

	board[position] = player

	display_board()


def check_if_game_over():

	global check_if_game_over
	global check_for_winner
	global check_if_tie

	return

def check_for_winner():
    
	# Set up global variables
	global winner

	# check rows
	row_winner = check_rows()
	# check columns
	column_winner = check_columns()
	# check diagonals
	diagonal_winner = check_diagonals()
	if row_winner:
		winner = row_winner
	elif column_winner:
		winner = column_winner
	elif diagonal_winner:
		winner = diagonal_winner
	else:
		winner = None
	return

def check_rows():
	
	# Set up global variables
	global game_still_going

	# Check if any of the rows have all the same value
	row_1 = board[0] == board[1] == board[2] != "–"
	row_2 = board[3] == board[4] == board[5] != "–"
	row_3 = board[6] == board[7] == board[8] != "–"

	# If any row does have a match, flag that there is a win
	if row_1 or row_2 or row_3:
		game_still_going
	# Return the winner (X or O)
	if row_1:
		return board[0]
	elif row_2:
		return board[3]
	elif row_3:
		return board[6]
	return

def check_columns():
	# Set up global variables
	global game_still_going
	# Check if any of the rows have all the same value
	column_1 = board[0] == board[1] == board[2] != "–"
	column_2 = board[3] == board[4] == board[5] != "–"
	column_3 = board[6] == board[7] == board[8] != "–"
	# If any column does have a match, flag that there is a win
	if column_1 or column_2 or column_3:
		game_still_going = False
	if column_1:
		return board[0]
	elif column_2:
		return board[1]
	elif column_2:
    		return board[2]
	return

def check_diagonals():
	# Set up global variables
	global game_still_going
	# Check if any of the diagonals have all the same value
	diagonals_1 = board[0] == board[4] == board[8] != "–"
	diagonals_2 = board[6] == board[4] == board[2] != "–"
	# If any diagonal does have a match, flag that there is a win
	if diagonals_1 or diagonals_2:
		game_still_going = False
	# Return the winner (X or O)
	if diagonals_1:
		return board[0]
	elif diagonals_2:
		return board[6]
	return


'''
def check_if_tie():

    global game_still_going

if "–" not in board:
    game_still_going = False

	return
'''

def flip_player():

	global current_player
	# if the current player was x, then change it to O
	if current_player == 'X':
		current_player = 'O'
		# if the current player was O, then change it to X
	elif current_player == 'O':
		current_player = 'X'
	return
	

play_game()