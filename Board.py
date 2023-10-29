from tkinter import Tk, Canvas, Frame, Label ,Button
from PIL import Image, ImageTk
from MiniGame_One import MiniGame_One 
from MiniGame_Two import MiniGame_Two 
from Player import *
import random


pos = 0
boardsize=24
qsize=6
# Constants for window size and grid setup
ROWS,COLS = 7,7 #delimite how many squares you want to have
WIDTH, HEIGHT = 100,100
#size = (WIDTH,HEIGHT)
SQUARE_SIZE = 100  # the size of the square is width divided by number of rows 

SQUARE_SIZE_X = WIDTH // COLS 
SQUARE_SIZE_Y = WIDTH // COLS 

# Define color constants
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)


class EndTurnButton(Button):
	def __init__(self,root,player_positions,my_button_move):
		super().__init__(root,text="End Turn ",command=self.on_button_click,width=10,height=3)
		self.player_positions=player_positions
		self.my_button_move=my_button_move

	def on_button_click(self):
		self.grid_remove()
		self.my_button_move.grid(row=ROWS // 2, column=COLS // 2)
		board.labelPlayer(board.get_current_player_index())

class PlayButton(Button):
	def __init__(self, root,player_positions):
		# Call the constructor of the base class (Button)
		super().__init__(root, text="Play ", command=self.on_button_click,width=10,height=3)
		self.gameWon = False
		self.button_move = ButtonMove(root,player_positions,False,text="Move")
		self.button_move.grid(row=ROWS//2, column=COLS//2)
		self.player_positions=player_positions
		self.endTurn = False
		self.row=0
		self.col=0
		
	def notMove(self,row,colum):
		self.row=row
		self.col=colum
		if row == 0 and colum == 1 :
			self.button_move.grid_remove()
		if row == 0 and colum == 2 :
			self.button_move.grid_remove()
		if row == 0 and colum == 3 :
			self.button_move.grid_remove()
		if row == 0 and colum == 4 :
			self.button_move.grid_remove()
		if row == 6 and colum == 1 :
			self.button_move.grid_remove()
		if row == 6 and colum == 2 :
			self.button_move.grid_remove()
		if row == 6 and colum == 3 :
			self.button_move.grid_remove()
		if row == 6 and colum == 4 :
			self.button_move.grid_remove()

	def on_button_click(self):
		if self.row == 0 and self.col == 1:
			self.MiniGame_One()
		if self.row == 0 and self.col == 2:
			self.MiniGame_One()
		if self.row == 0 and self.col == 3:
			self.MiniGame_One()
		if self.row == 0 and self.col == 4:
			self.MiniGame_One()
		if self.row == 6 and self.col == 1 :
			self.MiniGame_Two()
		if self.row == 6 and self.col == 2 :
			self.MiniGame_Two()
		if self.row == 6 and self.col == 3 :
			self.MiniGame_Two()
		if self.row == 6 and self.col == 4 :
			self.MiniGame_Two()
	
	def MiniGame_Two(self):
		game_Two = MiniGame_Two()
		game_Two.Play_Mini()
		if game_Two.getWon():
			self.grid_remove()
			self.button_move.grid(row=ROWS//2, column=COLS//2)
		if game_Two.getLost():
			self.button_move.grid_remove()
			self.grid_remove()
			self.button_move.getEndButton().grid(row=ROWS//2, column=COLS//2)
			board.swap_current_four_players()
			
	def MiniGame_One(self):	
		#check if the player won or lost the mini-game
		game_one = MiniGame_One()	
		game_one.Play_Mini()
		if game_one.getWon():
			self.grid_remove()
			self.button_move.grid(row=ROWS//2, column=COLS//2)
		if game_one.getLost():
			self.button_move.grid_remove()
			self.grid_remove()
			self.button_move.getEndButton().grid(row=ROWS//2, column=COLS//2)
			board.swap_current_four_players()
			#print("current player "+str(board.get_current_player_index()))

	def getendTurn(self):
		return self.endTurn

class ButtonMove(Button):
	def __init__(self, root,player_positions,endTurn,text="Play "):
		# Call the constructor of the base class (Button)
		super().__init__(root, text=text, command=self.on_button_click,width=10,height=3)
		self.player_positions = player_positions
		self.endTurn = endTurn
		self.button_End = EndTurnButton(root,player_positions,self)

	def getEndButton(self):
		return self.button_End 

	def on_button_click(self):
		#pos = 0
		#boardsize=24
		#qsize=6
		roll=random.randrange(1,6)
		#roll=1   
		global pos, boardsize, qsize # Add player_positions to the list of global variables
		
		pos=(pos+roll)%boardsize
		#print(pos)
		fliped=(pos>=(qsize*2))
		temp=pos%(qsize*2)
		if fliped:
			temp=(qsize*2)-temp
		fi,si=0,0
		if temp < qsize:
			fi=0
			si=temp%qsize
		elif temp == qsize*2:
			fi=qsize
			si=qsize
		else:
			fi=temp%qsize
			si=qsize
		if fliped:
			if board.get_current_player_index()==1:
				self.player_positions[0] = (si,fi)  #player_One position update
				board.move_player(si,fi,1)
			elif board.get_current_player_index()==2:
				board.player_positions[1] = (si,fi)  #player_two position update
				board.move_player(si,fi,2)
			elif board.get_current_player_index()==3:
				board.player_positions[2] = (si,fi)  #player_three position update
				board.move_player(si,fi,3)
			else:
				self.player_positions[3] = (si,fi)  #player_four position update
				board.move_player(si,fi,4)
		else:
			if board.get_current_player_index()==1:
				board.player_positions[0] = (fi,si)  #player_One position update
				board.move_player(fi,si,1)
			elif board.get_current_player_index()==2:
				board.player_positions[1] = (fi,si)  #player_two position update
				board.move_player(fi,si,2)
			elif board.get_current_player_index()==3:
				board.player_positions[2] = (fi,si)  #player_three position update
				board.move_player(fi,si,3)
			else:
				board.player_positions[3] = (fi,si)  #player_four position update
				board.move_player(fi,si,4)
			
		#print(self.player_positions)

class Board:
	def __init__(self,root):
		self.root=root
		# list containing multiple tuples each tuple represent the position of the player on the board
		self.player_positions = [(0, 0), (0, 6), (6, 6), (6, 0)] 
		self.image_path = "images\playerOne.png"
		self.original_image = Image.open(self.image_path)
		self.resized_image = self.original_image.resize((SQUARE_SIZE-50, SQUARE_SIZE-50))
		self.image = ImageTk.PhotoImage(self.resized_image)

		self.image_path_Two = "images\playerTwo.png"
		self.original_image_Two = Image.open(self.image_path_Two)
		self.resized_image2 = self.original_image_Two.resize((SQUARE_SIZE-50, SQUARE_SIZE-50))		   
		self.image_Two = ImageTk.PhotoImage(self.resized_image2)

		self.image_path_Three = "images\playerThree.png"
		self.original_image_Three = Image.open(self.image_path_Three)
		self.resized_image_Three = self.original_image_Three.resize((SQUARE_SIZE-50, SQUARE_SIZE-50))		   
		self.image_Three = ImageTk.PhotoImage(self.resized_image_Three)

		self.image_path_Four = "images\playerFour.png"
		self.original_image_Four = Image.open(self.image_path_Four)
		self.resized_image_Four = self.original_image_Four.resize((SQUARE_SIZE-50, SQUARE_SIZE-50))		   
		self.image_Four = ImageTk.PhotoImage(self.resized_image_Four)
		
		self.board = [] # Initialize an empty list to represent the game board.
		#self.player_positions = player_positions 	
		self.red_left = self.white_left = 12 
		self.squares = [[None for _ in range(COLS)] for _ in range(ROWS)]
		self.create_board(0,0)
		self.draw_squares()
		self.notMove = False
		self.player_row_One, self.player_col_One = 0, 0
		self.player_row_Two, self.player_col_Two = 0, 6
		self.player_row_Three, self.player_col_Three = 6, 6
		self.player_row_Four, self.player_col_Four = 6, 0
		#root.bind("<Key>", self.on_key_press)
		self.gameWon = False
		self.buttonPlay= PlayButton(root,self.player_positions)
		self.current_player_index = 1
		self.label = Label(root, text="Turn Player 1", bg="#D3D3D3",padx=10, pady=10)
		self.labelTwo = Label(root, text="Blue", bg="#D3D3D3",padx=10, pady=10)
		self.labelPlayer(self.current_player_index)

	def get_current_player_index(self):
		return self.current_player_index

	def swap_current_player(self):
		# Toggle the current player's index (0 to 1, 1 to 0)
		self.current_player_index = 2 if self.current_player_index == 1 else 1

	def swap_current_four_players(self):
		if  self.current_player_index == 4:
			self.current_player_index = 4 if self.current_player_index == 1 else 1
		elif self.current_player_index == 3:
			self.current_player_index = 3 if self.current_player_index == 4 else 4
		elif self.current_player_index == 2:
			self.current_player_index = 2 if self.current_player_index == 3 else 3
		elif self.current_player_index == 1:
			self.current_player_index = 1 if self.current_player_index == 2 else 2
		else :
			print ("Not a player")
		return self.current_player_index

	def getPlayButton(self):
		return self.buttonPlay
	'''	
	def on_key_press(self, event):
		x_coordinate = self.player_positions[0][1]
		y_coordinate = self.player_positions[0][0]

		if len(self.player_positions) >= 2:
			x_coordinate_Player2 = self.player_positions[1][0]
			y_coordinate_Player2 = self.player_positions[1][1]

		if event.keysym == "d":
			x_coordinate += 1
		if event.keysym == "a":
			x_coordinate -= 1
		

	# Create a new tuple with the updated coordinates
		self.player_positions = ((y_coordinate, x_coordinate))
		board.move_player(y_coordinate, x_coordinate)
		self.buttonPlay.notMove(y_coordinate,x_coordinate)
		self.player_row = x_coordinate
		self.player_col = y_coordinate
	'''
			
	def getPlayerColorTwo(self):
		return self.image_Two

	def getPlayerColorThree(self):
		return self.image_Three
	
	def getPlayerColorFour(self):
		return self.image_Four

	def GetBoard(self):
		return self
	
	def draw_squares(self):
		for rows in range(ROWS):
			for col in range (COLS):
				if  col == 0 or (rows < 1) or col == COLS-1 or rows>ROWS-2:
					if col in range (rows%2==0,COLS,2): 
						colorBg="red"
					else:
						colorBg="black"
				else:
					colorBg="white"
				rect = Canvas(root, width=SQUARE_SIZE, height=SQUARE_SIZE, bg=colorBg)
				rect.grid(row=rows, column=col)
				self.squares[rows][col]=rect
				frame = Frame(root, bg="yellow", width=100, height=100)
				frame.grid(row=ROWS//2, column=COLS//2)
		self.draw()
	
	def create_board(self,row,col):
		for row in range(ROWS):
			self.board.append([])
			for col in range(COLS):
				if (row, col) in self.player_positions:
					self.board[row].append(Player(row, col,self.image,self))
					self.board[row].append(Player(row, col,self.image_Two,self))
					self.board[row].append(Player(row, col,self.image_Three,self))
					self.board[row].append(Player(row, col,self.image_Four,self))
				else:
					self.board[row].append(0)
		
	def move_player(self,new_row,new_col,player):
		if not self.notMove and player==1:
			if 0 <= new_row < ROWS and 0 <= new_col < COLS:				
				self.player_row_One = new_row
				self.player_col_One = new_col
				self.redraw_board()
				self.MiniGameOne(self.player_row_One,self.player_col_One)
				
		if not self.notMove and player==2:
			self.player_row_Two = new_row
			self.player_col_Two = new_col	
			if 0 <= new_row < ROWS and 0 <= new_col < COLS:				
				self.player_row_Two = new_row
				self.player_col_Two = new_col
				self.redraw_board()
				self.MiniGameOne(self.player_row_Two,self.player_col_Two)

		if not self.notMove and player==3:
			self.player_row_Three = new_row
			self.player_col_Three = new_col	
			if 0 <= new_row < ROWS and 0 <= new_col < COLS:				
				self.player_row_Three = new_row
				self.player_col_Three = new_col
				self.redraw_board()
				self.MiniGameOne(self.player_row_Three,self.player_col_Three)

		if not self.notMove and player==4:
			self.player_row_Four = new_row
			self.player_col_Four = new_col	
			if 0 <= new_row < ROWS and 0 <= new_col < COLS:				
				self.player_row_Four = new_row
				self.player_col_Four = new_col
				self.redraw_board()
				self.MiniGameOne(self.player_row_Four,self.player_col_Four)	
	# ... (other methods) ...

	def redraw_board(self):
		# Redraw the board with updated player position
		for row in range(ROWS):
			for col in range(COLS):
				if  col == 0 or (row < 1) or col == COLS-1 or row>ROWS-2:
					if col in range (row%2==0,COLS,2): 
						colorBg="red"
					else:
						colorBg="black"
				else:
					colorBg="white"
				rect = self.squares[row][col]
				rect.config(bg=colorBg)
				rect.delete("all")
				
				#player 1
				canvas_widget=self.squares[self.player_row_One][self.player_col_One]#control movement player one
				canvas_widget.create_image(50, 50, anchor="nw", image=self.image)
	
				#player 2
				rect = self.squares[0][6]
				canvas_widget=self.squares[self.player_row_Two][self.player_col_Two]    #control movement player 2
				canvas_widget.create_image(0, 50, anchor="nw", image=self.image_Two)

				#player 3
				rect = self.squares[row][col]
				rect = self.squares[6][6]
				canvas_widget=self.squares[self.player_row_Three][self.player_col_Three]    #control movement player 3
				canvas_widget.create_image(0, 0, anchor="nw", image=self.image_Three)
	
				#player 4
				rect = self.squares[row][col]
				rect = self.squares[6][0]
				canvas_widget=self.squares[self.player_row_Four][self.player_col_Four]    #control movement player 4
				canvas_widget.create_image(50, 0, anchor="nw", image=self.image_Four)
				#self.labelPlayer(self.current_player_index)
	
	def labelPlayer(self,currentPlayer):
			if currentPlayer==1:
				self.label.grid(row=1, column=1,columnspan=2,sticky='nw')
				self.labelTwo.grid(row=1, column=1,columnspan=2,sticky='sw')
				self.labelTwo.config(text="Blue")
			elif currentPlayer==2:
				self.label.grid(row=1, column=5,columnspan=2,sticky='nw')
				self.labelTwo.grid(row=1, column=5,columnspan=2,sticky='sw')
				self.labelTwo.config(text="Green")
			elif currentPlayer==3:
				self.label.grid(row=5, column=5,columnspan=2,sticky='nw')
				self.labelTwo.grid(row=5, column=5,columnspan=2,sticky='sw')
				self.labelTwo.config(text="Red")
			elif currentPlayer==4:
				self.label.grid(row=5, column=1,columnspan=2,sticky='nw')
				self.labelTwo.grid(row=5, column=1,columnspan=2,sticky='sw')
				self.labelTwo.config(text="Yellow")
			self.label.config(text="Turn Player "+str(self.current_player_index))
	#def playerDisplay(self,canvas,):
	def draw(self):
		for self.player_row in range(ROWS):
			for self.player_col in range(COLS):
				#start the list
				player = self.board[self.player_positions[0][1]][self.player_positions[0][0]]
				if player != 0:
					#draw players on places on the board with value not zero
					player.draw(self.squares[self.player_positions[0][1]][self.player_positions[0][0]],1)
					player.draw(self.squares[self.player_positions[1][0]][self.player_positions[1][1]],2)
					player.draw(self.squares[self.player_positions[2][0]][self.player_positions[2][1]],3)
					player.draw(self.squares[self.player_positions[3][0]][self.player_positions[3][1]],4)
	
	def MiniGameOne(self,row,col):
		x_coordinate = row
		y_coordinate = col	
		self.buttonPlay.notMove(x_coordinate,y_coordinate)
		self.buttonPlay.grid(row=ROWS//2, column=COLS//2,columnspan=1)
			
root = Tk()
board = Board(root)	
def play():
	root.title("Board")
	root.winfo_toplevel().positionfrom("user")
	root.mainloop()	
	return board
