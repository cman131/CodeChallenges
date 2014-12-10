import copy

class Board:
	def __init__(self):
		self.board = [[0,0,0],[0,0,0],[0,0,0]]
	def getAIMove(self):
		val = (0,0)
		for x in range(3):
			for y in range(3):
				if(self.board[x][y]==0):
					val = (x,y)
					b = Board()
					b.board = copy.deepcopy(self.board)
					b.board[x][y] = 'X'
					if(b.isWon()):
						return (x,y)
		return val
	def isWon(self):
		for i in range(3):
			if(self.board[1][i]!=0 and
			self.board[1][i]==self.board[0][i] and
			self.board[1][i]==self.board[2][i]):
				return True
			if(self.board[i][1]!=0 and
			self.board[i][1]==self.board[i][0] and
			self.board[i][1]==self.board[i][2]):
				return True
		if(self.board[1][1]!=0 and (
			(self.board[0][0]==self.board[1][1] and
			self.board[0][0]==self.board[2][2])
		or	(self.board[0][2]==self.board[2][0] and
			self.board[0][2]==self.board[1][1])
		)):
			return True
	def printOut(self):
		print("|"+str(self.board[0][0])+"|"+str(self.board[0][1])+"|"+str(self.board[0][2])+"|")
		print("|"+str(self.board[1][0])+"|"+str(self.board[1][1])+"|"+str(self.board[1][2])+"|")
		print("|"+str(self.board[2][0])+"|"+str(self.board[2][1])+"|"+str(self.board[2][2])+"|\n")
	def play(self):
		player = False
		while(not self.isWon()):
			x = int(input("X: "))
			y = int(input("Y: "))
			print("\n")
			while(self.board[y][x]!=0):
				x = int(input("X: "))
				y = int(input("Y: "))
				print("\n")
			self.board[y][x] = "P"
			self.printOut()
			if(self.isWon()):
				player = True
				break
			turn = self.getAIMove()
			self.board[turn[0]][turn[1]] = "X"
			self.printOut()
		print("You win!" if player else "You lose.")
borad = Board()
borad.play()
