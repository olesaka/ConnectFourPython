#! /usr/bin/env python2
import unittest
from connectFour import ConnectFour
"""
	Test class for the connectFour python game
	This test file outline was found at 
	http://pymbook.readthedocs.io/en/latest/testing.html
"""
class TestConnectFour(unittest.TestCase):

	# create three connectFour objects to test and 
	# interact with throughout the file
	game1 = ConnectFour()
	game2 = ConnectFour()
	game2.height = 45
	game2.width = 35
	game3 = ConnectFour()
	game3.height = 250
	game3.width = 400


	def test_create_board(self):
		self.game1.create_board()
		self.game2.create_board()
		self.game3.create_board()
		self.assertEqual(len(self.game1.board[0]), 7)
		self.assertEqual(len(self.game1.board), 7)	
		self.assertEqual(len(self.game2.board[44]), 35)
		self.assertEqual(len(self.game2.board), 45)	
		self.assertEqual(len(self.game3.board[249]), 400)
		self.assertEqual(len(self.game3.board), 250)	
	
	
	def test_newboard(self):
		self.game1.new_board()
		self.game2.new_board()
		self.game3.new_board()
		self.assertTrue(self.game1.board[0][0]=='*')
		self.assertTrue(self.game1.board[6][6]=='*')
		self.assertTrue(self.game2.board[3][15]=='*')
		self.assertTrue(self.game2.board[42][25]=='*')
		self.assertTrue(self.game3.board[112][0]=='*')
		self.assertTrue(self.game3.board[249][399]=='*')
		return

	
	def test_switch_player(self):
		self.game1.player = 0
		self.game1.switch_player()
		self.assertTrue(self.game1.player==1)
		self.game1.switch_player()
		self.assertTrue(self.game1.player==0)
		return


	def test_add_chip1(self):
		self.game1.create_board()
		self.game1.new_board()
		for i in range(self.game1.height):
			self.assertTrue(self.game1.add_chip(2))
		self.assertFalse(self.game1.add_chip(2))
		return


	def test_add_chip2(self):
		self.game2.create_board()
		self.game2.new_board()
		for i in range(self.game2.height):
			self.assertTrue(self.game2.add_chip(0))
		self.assertFalse(self.game2.add_chip(0))
		return


	def test_add_chip3(self):
		self.game3.create_board()
		self.game3.new_board()
		for i in range(self.game3.height):
			self.assertTrue(self.game3.add_chip(399))
		self.assertFalse(self.game3.add_chip(399))
		return


	def test_check_for_winner1(self):
		self.game1.create_board()
		self.game1.new_board()
		self.game1.player = 0
		for i in range(4):
			self.assertFalse(self.game1.check_for_winner())
			self.game1.board[6][i] = 'X'
		self.assertTrue(self.game1.check_for_winner())
		return


	def test_check_for_winner2(self):
		self.game1.create_board()
		self.game1.new_board()
		self.game1.player = 0
		for i in range(3, 7):
			self.assertFalse(self.game1.check_for_winner())
			self.game1.board[0][i] = 'X'
		self.assertTrue(self.game1.check_for_winner())
		return


	def test_check_for_winner3(self):
		self.game2.create_board()
		self.game2.new_board()
		self.game2.player=1
		self.game2.connect = 7
		for i in range(7):
			self.assertFalse(self.game2.check_for_winner())
			self.game2.board[i][34] = 'O'
		self.assertTrue(self.game2.check_for_winner())
		return

	def test_check_for_winner4(self):
		self.game2.create_board()
		self.game2.new_board()
		self.game2.player=1
		self.game2.connect = 7
		for i in range(7):
			self.assertFalse(self.game2.check_for_winner())
			self.game2.board[i][0] = 'O'
		self.assertTrue(self.game2.check_for_winner())
		return


	def test_check_for_winner5(self):
		self.game3.create_board()
		self.game3.new_board()
		self.game3.player=1
		self.game3.connect = 15
		for i in range(235, 250):
			self.assertFalse(self.game3.check_for_winner())
			self.game3.board[i][0] = 'O'
		self.assertTrue(self.game3.check_for_winner())
		return


	def test_check_for_winner6(self):
		self.game3.create_board()
		self.game3.new_board()
		self.game3.player = 0
		self.game3.connect = 15
		for i in range(235, 250):
			self.assertFalse(self.game3.check_for_winner())
			self.game3.board[i][399] = 'X'
		self.assertTrue(self.game3.check_for_winner())
		return

	def test_check_for_winner7(self):
		self.game2.create_board()
		self.game2.new_board()
		self.game2.connect = 7
		self.game2.player=1
		for i in range(28, 35):
			self.assertFalse(self.game2.check_for_winner())
			self.game2.board[44][i] = 'O'
		self.assertTrue(self.game2.check_for_winner())
		return


	def test_check_for_winner8(self):
		self.game2.create_board()
		self.game2.new_board()
		self.game2.connect = 7
		self.game2.player=1
		for i in range(7):
			self.assertFalse(self.game2.check_for_winner())
			self.game2.board[i][0] = 'O'
		self.assertTrue(self.game2.check_for_winner())
		return


	def test_check_for_winner9(self):
		self.game3.create_board()
		self.game3.new_board()
		self.game3.player = 0
		self.game3.connect = 15
		for i in range(15):
			self.assertFalse(self.game3.check_for_winner())
			self.game3.board[i][i] = 'X'
		self.assertTrue(self.game3.check_for_winner())
		return


	def test_check_for_winner10(self):
		self.game3.create_board()
		self.game3.new_board()
		self.game3.player = 1
		self.game3.connect = 15
		for i in range(15):
			self.assertFalse(self.game3.check_for_winner())
			self.game3.board[249-i][i] = 'O'
		self.assertTrue(self.game3.check_for_winner())
		return

	
	def test_check_for_winner11(self):
		self.game1.create_board()
		self.game1.new_board()
		self.game1.player = 1
		for i in range(4):
			self.assertFalse(self.game1.check_for_winner())
			self.game1.board[6-i][6-i] = 'O'
		self.assertTrue(self.game1.check_for_winner())
		return


	def test_check_for_winner12(self):
		self.game1.create_board()
		self.game1.new_board()
		self.game1.player = 0
		for i in range(4):
			self.assertFalse(self.game1.check_for_winner())
			self.game1.board[i][6-i] = 'X'
		self.assertTrue(self.game1.check_for_winner())
		return


	def test_save_load_game1(self):
		self.game1.create_board()
		self.game1.new_board()
		self.game1.player = 0
		self.game1.connect = 4
		for i in range(self.game1.height):
			for j in range(self.game1.width):
				if i%2==0 and j%2==0:
					self.game1.board[i][j] = 'X'
				else:
					self.game1.board[i][j] = 'O'
		self.game1.save_game("test_save1", self.game1)

		game = self.game1.load_game("test_save1")
		self.assertTrue(game.height==7)
		self.assertTrue(game.width==7)
		self.assertTrue(game.player==0)
		self.assertTrue(game.connect==4)
		for i in range(game.height):
			for j in range(game.width):
				if i%2==0 and j%2==0:
					self.assertTrue(game.board[i][j] == 'X')
				else:
					self.assertTrue(game.board[i][j] == 'O')
		return

	def test_save_load_game2(self):
		self.game2.create_board()
		self.game2.new_board()
		self.game2.player = 1
		self.game2.connect = 7
		for i in range(self.game2.height/2):
			for j in range(self.game2.width):
				if j%2==0:
					self.game2.board[i][j] = 'X'
				else:
					self.game2.board[i][j] = 'O'
		self.game2.save_game("test_save2", self.game2)

		game = self.game2.load_game("test_save2")
		self.assertTrue(game.height==45)
		self.assertTrue(game.width==35)
		self.assertTrue(game.player==1)
		self.assertTrue(game.connect==7)
		for i in range(game.height):
			for j in range(game.width):
				if j%2==0 and i<int(game.height/2):
					self.assertTrue(game.board[i][j] == 'X')
				elif i<int(game.height/2):
					self.assertTrue(game.board[i][j] == 'O')
				else:
					self.assertTrue(game.board[i][j] == '*')
		return

	def test_save_load_game3(self):
		self.game3.create_board()
		self.game3.new_board()
		self.game3.player = 0
		self.game3.connect = 26
		for i in range(self.game3.height-3):
			for j in range(self.game3.width):
				if i%3==0 and j%2==0:
					self.game3.board[i][j] = 'X'
				elif (j+i)%4==0:
					self.game3.board[i][j] = 'O'

		self.game3.save_game("test_save3", self.game3)

		game = self.game3.load_game("test_save3")
		self.assertTrue(game.height==250)
		self.assertTrue(game.width==400)
		self.assertTrue(game.player==0)
		self.assertTrue(game.connect==26)
		for i in range(game.height-3):
			for j in range(game.width):
				if i%3==0 and j%2==0:
					self.assertTrue(game.board[i][j]=='X')
				elif (j+i)%4==0:
					self.assertTrue(game.board[i][j] == 'O')
				else:
					self.assertTrue(game.board[i][j]=='*')
		return


if __name__=='__main__':

	# the following code for running every test file above
	# can be found on stack overflow from the link below
	# http://stackoverflow.com/questions/3295386/python-unittest-and-discovery/8335165
	loader = unittest.TestLoader()
	tests = loader.discover('.')
	testRunner = unittest.runner.TextTestRunner()
	testRunner.run(tests)


