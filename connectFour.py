#! /usr/bin/env python2
import sys
import pickle
"""
	Python code that allows user to play a game of connect four
	Game features include saving, loading, and starting a new game
	@author Andrew Olesak
	@version March 3, 2017
	If there are any issues with the following code, please email olesaka@mail.gvsu.edu
	The use of this code is for the public domain
"""


class ConnectFour(object):
	# create instance variables 

	# create game parameters and dimensions for the board
	height = 7
	width = 7
	connect = 4
	player = 0
	# create a list of the two different game character pieces
	piece = []
	# create a list of a lists variable for the game board
	board = [[]]

	"""
		Function sets the dimensions of the two dimensional array
		for the game board
	"""
	def create_board(self):
		# create the board with a list of listss
		self.board = [[i for i in range(self.width)] for j in range(self.height)]
		return


	"""
		Constructor sets values to instance variables
	"""
	def __init__(self):

		# set the piece list as each of the two chip types
		self.piece = ['X', 'O']
		# call a function that uses lambda to dynamically 
		# allocate the board as a list of lists
		self.create_board()
		return 


	"""
		Function determine if command line argument were given 
		and change values if necessary
	"""
	def command_setup(self):
		# declare the following local variables
		previous = ""
		filename = ""
		# Try block used in case of parsing issue
		# previous keeps track of what command was entered
		try:
			for i in sys.argv:
				# if the previous command was '-s', the current
				# one is the height and width
				if previous=="-s":
					# the board must have dimensions of at least 4
					if int(i)>3:
						self.height = int(i)
						self.width = int(i)
				# if the previous command was '-h', the current 
				# one is the height
				if previous=="-h":
					# the board must have a height of at least 4
					if int(i)>3:
						self.height = int(i)
				# if the previous command was '-w', the current
				# one is the width
				if previous=="-w":
					# the board must have width of at least 4
					if int(i)>3:
					 self.width = int(i)
				# if the previous command was '-c', the current
				# one is the number of pieces to connect
				if previous == "-c":
					# the board must have connections to win
					# of at least 3
					if int(i)>2:
						self.connect = int(i)
				# if the previous command was '-l', the current 
				# on is the filename
				if previous=="-l":
					filename = str(i)
				previous = i

			# check to make sure that the number of connections to
			# win doesn't exceed the smallest dimension of the board
			if self.height<self.width:
				# height is smallest, so check if connect is larger
				# if so, set default
				if self.connect>self.height:
					self.connect = 4
					print "Sorry, the number of connections was too big"
					print "A default win was set at four connections to win"
			else:
				# width is smallest so check if connect is larger
				# if so, set default
				if self.connect>self.width:
					self.connect = 4
					print "Sorry, the number of connections was too big"
					print "A default win was set at four connections to win"
		# exception handler to catch any issues while interpresting
		# user input
		except Exception:
			print "Sorry, you didn't enter all of the data correctly"
			print "Some defaults may be applied"

		self.create_board()
		return filename


	"""
		Function prints the board neatly to the screen and
		labels the columns appropriately
	"""
	def print_board(self):

		# print out the column numbers
		tens = 1
		print " ",
		for i in range(self.width):
			if (i+1)%10==0:
				print str(tens),
				tens+=1
			else:
				print " ",
		print ""
		print " ",
		for i in range(self.width):
			print (i+1)%10,
		print ""

		# print out the board
		for i in range(self.height):
			print " ",
			for j in range(self.width):
				print self.board[i][j],
			print ""
		return


	"""	
		Function resets the board to a blank board using a lambda function
	"""
	def new_board(self):
		self.board = map(lambda x: map(lambda y: '*', x), self.board)
		return

	"""
		Function adds a chip to the given column if it is not already full
		@return true if the chip was added successfully, otherwise return false
	"""
	def add_chip(self, column):
		#check for within range
		if column<0 or column>=self.width:
			return False

		# loop through the board and check to see if 
		# the column is full, otherwise add the piece
		# and return true
		for i in range(self.height-1, -1, -1):
			if self.board[i][column]=='*':
				self.board[i][column]=self.piece[self.player]
				return True
		return False


	"""	
		Function checks to see if there is a winner for the current player
		@return true if there is a winner, otherwise false
	"""
	def check_for_winner(self):

		# loop through each spot on the board
		for row in range(self.height):
			for col in range(self.width):
				# check to see if the spot contains the piece
				# of the given player
				if self.board[row][col]==self.piece[self.player]:
					# check for horizontal win to the right 
					# of the piece if and only if it is within
					# the dimensions of the board
					if col+self.connect<=self.width :
						for i in range(1, self.connect):
							if self.board[row][i+col]== self.piece[self.player]:
								if i==self.connect-1 :
									return True
								continue
							else:
								break;
					# check for vertical win downward from the current
					# spot if and only if it it within the dimensions 
					# of the board
					if row+self.connect<=self.height:
						for i in range(1, self.connect):
							if self.board[row+i][col]==self.piece[self.player]:
								if(i==self.connect-1):
									return True
								continue
							else:
								break;

					# check for diagonal win downward to the right from current
					# piece if and only if it is within the dimensions of the board
					if row+self.connect<=self.height and col+self.connect<=self.width:
						for i in range(1, self.connect):
							if self.board[row+i][col+i]==self.piece[self.player]:
								if(i==self.connect-1):
									return True
								continue
							else:
								break;

					# check for diagonal win downward to the left from current 
					# pice if and ony if it is within the dimensions of the board
					if row+self.connect<=self.height and col-self.connect+1>=0:
						for i in range(1, self.connect):
							if self.board[row+i][col-i]==self.piece[self.player]:
								if(i==self.connect-1):
									return True
								continue
							else:
								break;

		# if no win condition was found, return false
		return False

	"""
		Function writes the contents of a given buffer to a given filename
		@param filename the name of the file
		@param buffer a list that contains all of the game info
	"""
	def save_game(self, filename, game):

		try:
			#open the file to write to
			file = open(filename, 'w')
			# use pickle to save the object
			pickle.dump(game, file)
			# close the file
			file.close()

		# exception handler for any issues that might go wrong with saving the game
		except (pickle.PicklingError, pickle.PickleError, Exception):
			print "Sorry, something went wrong with the file."
			return False

		return True

	"""
		Function reads the contents from a given file and places them in a buffer
		@param filename the name of the file
		@param buffer the list that will contain the game info
	"""
	def load_game(self, filename):

		try:
			# open the file to load game from
			file = open(filename, 'rb')
			# use pickle get the game info in object form
			game = pickle.load(file)
			# close the file
			file.close()

		# exception handler for any issues that might go wrong with the game
		except (pickle.UnpicklingError, pickle.PickleError, Exception):
			print "Sorry, something went wrong with the file."
			# return "None" because of invalid file read
			return None

		# except IOError:
		# 	print "Sorry, something went wrong with the file you provided."
		# 	return None 
		#  return the retrived game object
		return game

	
	"""	
		Function switches the current player to the other player
	"""
	def switch_player(self):

		# if the current player is 0 for the index of the 
		# game pieces switch to 1, otherwise switch to 0	
		if(self.player==0):
			self.player=1
		else:
			self.player=0
		return


	"""	
		Function prints the game commands to the screen
	"""
	def print_commands(self):
		print "***Game Commands***"
		print ""
		print "Type 'n' for a new game"
		print "Type 's' to save the current game"
		print "Type 'l' to load a previously saved game"
		print "Type 'c' to view the commands list again"
		print "Enter a column number in the correct range to complete a turn"
		print ""
		return

	"""
		Function prints who the current player is
	"""
	def print_player(self):

		# use the player index to identify who's turn it is
		if(self.player==0):
			print "It is player one's turn"
		else:
			print "It is player two's turn"

"""
	Main function runs a while loop that allows the two players to interact 
	with a connect four game through the command line.  
"""
def main():


	# start the while loop to play the game
	#*********************
	print "Welcome to Connect Four"
	print "\n"
	# create a game object to interact with
	game = ConnectFour()
	# print the list of commands to the screen for the users to see
	game.print_commands()
	# check to see if any arguments were given for the game parameters
	# and set them if so
	filename = game.command_setup()
	# if a filename was given, load the game from it
	# or let the users know if something went wrong
	if filename != "":
		loaded_game = game.load_game(filename)
		if loaded_game==None:
			print "A default board has been created"
		else:
			game = loaded_game
	else:
		# if no game was loaded, set the board to a new game
		game.new_board()
	# print the board and the current player to the screen
	game.print_board()
	game.print_player()
	# ask for a column or command and read in user input
	print "Please enter a column or command:"
	input = sys.stdin.readline()

	# continue to loop and play the game until a 'q' is entered to quit
	while (input[0]!='q'):
		# if a new line character is read, no data was entered 
		# and it is still the current player's turn
		if (input[0]=='\n'):
			input = sys.stdin.readline()
			continue
		# if 'n' is entered, reset the board for a new game
		# with the same game parameters and ask for a column or command
		elif (input[0]=='n'):
			game.new_board()
			game.player = 0;
			print "***New Game***"
			game.print_board()
			game.print_player()
			print "Please enter a column or command:"
			input = sys.stdin.readline()
			continue
		# if 'c' is entered, display the list of commands
		# used to control the game
		elif (input[0]=='c'):
			game.print_commands()
			print "Please enter a column or command:"
			input = sys.stdin.readline()
			continue
		# if 's' is entered, save the current game state to a given
		# file and allow to continue the current game
		elif(input[0]=='s'):
			# ask for a filename
			print "Please enter a filename"
			input = raw_input()
			# save the current game state to the given file
			game.save_game(input, game)
			# print the board and current player and ask 
			# for a column or command
			game.print_board()
			game.print_player()
			print "Please enter a column or command:"
			input = sys.stdin.readline()
			continue
		# if 'l' is entered, load a game state from a given file
		# and display the newly loaded board to the screen to play
		elif(input[0]=='l'):
			# ask for a filename
			print "Please enter the name of the file you would like to load from:"
			input = raw_input()
			loaded_game = game.load_game(input)
			# check to see if the return game object is of type 'None'
			if loaded_game==None:
				# the loaded game was 'None', so let the user know and ask for input
				print "Please enter a column, command, or enter 'l' if you would still like to load a game"
				input = raw_input()
				continue
			else:
				# the game was successfully loaded, so assign it to the current object
				# being used and print the board and current player along with
				# asking for a column or command
				game = loaded_game
				game.print_board()
				game.print_player()
				print "Please enter a column or command:"
				input = sys.stdin.readline()
				continue
		# if none of the above are entered, assume a column was entered and 
		# check to see if the chip can be added to the board
		else:
			# check to make sure that an integer was entered
			try:
				temp = int(input)
				if temp>game.width:
					print "Sorry, please enter a valid column"
					input = sys.stdin.readline()
					continue
				# if exception found, let the user know and ask for new input
			except Exception:
				print "Sorry, please enter a valid column"
				input = sys.stdin.readline()
				continue
			# valid input was found, so try to add the chip to the board
			if game.add_chip(int(input)-1)==False:
				# if column is already full, let the user know and ask for input
				print "Sorry, that column is already full"
				input = sys.stdin.readline()
				continue
			# if a chip was dropped into the board, check to see if there 
			# is a winner and let the users know if there is
			if game.check_for_winner()==True:
				game.print_board()
				if(game.player==0):
					print "Player one has won the game!"
				else:
					print "Player two has won the game!"
				# once a game has been one, the users must elected to
				# load a new game from a previously saved file, start a new
				# game, or quit the game
				print "Please enter 'n' for a new game, 'q' to quit', or 'l' to load a saved game"
				input = raw_input()
				while input[0]!='q' and input[0]!='l' and input[0]!='n':
					print "Please enter either an 'n', 'q', or 'l''"
					input = sys.stdin.readline()
				continue
			# if not winner was found, continue the game by printing
			# the board and current player.  Then ask for input
			# for the next player's turn
			game.print_board()
			game.switch_player()
			game.print_player()
			print "Please enter a column or command:"
			input = sys.stdin.readline()
			

# call the main function to run the game
if __name__=="__main__":
	main()


	
