from tkinter import Tk, Canvas, Frame, Label ,Button
from PIL import Image, ImageTk
from MiniGame_One import MiniGame_One 
from MiniGame_Two import MiniGame_Two 
from Player import *
import random

# Constants for window size and grid setup
ROWS,COLS = 7,7 #delimite how many squares you want to have
WIDTH, HEIGHT = 100,100
#size = (WIDTH,HEIGHT)
SQUARE_SIZE = 100  # the size of the square is width divided by number of rows 

SIZE=800,800
SQUARE_SIZE_X = WIDTH // COLS 
SQUARE_SIZE_Y = WIDTH // COLS 

# Define color constants
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

class ButtonWon(Button):
	def __init__(self,root):
		super().__init__(root,text="Reset Game",command=self.on_button_click,width=10,height=3)

	def on_button_click(self):
		board.buttonPlay.getButtonMove().getEndButton().grid_remove()
		board.buttonPlay.grid_remove()
		board.buttonPlay.getButtonMove().grid_remove()
		board.reset_game()

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
		self.buttonMove=self.button_move.grid(row=ROWS//2, column=COLS//2)
		self.player_positions=player_positions
		self.endTurn = False
		self.row=0
		self.col=0

	def getButtonMove(self):
		return 	self.button_move

	def getEndButton(self):
		return self.button_move.getEndButton()

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
			board.swap_current_four_players()############################################################
			
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
		self.pos=0
		self.boardsize=24
		self.qsize=6
		self.roll_num=0

	def getEndButton(self):
		return self.button_End 

	
	
	def on_button_click(self):
		roll=random.randrange(1,6)
		#roll=1   
		#global pos, boardsize, qsize # Add player_positions to the list of global variables
		
		self.pos=(self.pos+roll)%self.boardsize
		#self.pos=self.roll(roll)
		#print(self.pos)
		fliped=(self.pos>=(self.qsize*2))
		temp=self.pos%(self.qsize*2)
		if fliped:
			temp=(self.qsize*2)-temp
		fi,si=0,0
		if temp < self.qsize:
			fi=0
			si=temp%self.qsize
		elif temp == self.qsize*2:
			fi=self.qsize
			si=self.qsize
		else:
			fi=temp%self.qsize
			si=self.qsize
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
			self.roll_num=fi
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
			self.roll_num=si
		#labelRoll=Label(root, text="You roll "+str(self.roll_num), bg="#D3D3D3",padx=10, pady=10)
		#labelRoll.grid(row=(ROWS//2)+1, column=COLS//2) 
		#print(self.player_positions)
		#print(roll)
class Board:
	def __init__(self,root):
		self.root=root
		# list containing multiple tuples each tuple represent the position of the player on the board
		self.player_positions = [(0, 0), (0, 6), (6, 6), (6, 0)] 
		self.image_path = "images\playerOne.png"
		self.image=self.resizeImage(self.image_path)
	
		self.image_path_Two = "images\playerTwo.png"
		self.image_Two=self.resizeImage(self.image_path_Two)
		
		self.image_path_Three = "images\playerThree.png"
		self.image_Three = self.resizeImage(self.image_path_Three)
		
		self.image_path_Four = "images\playerFour.png"
		self.image_Four =self.resizeImage(self.image_path_Four)
		
		self.board = [] # Initialize an empty list to represent the game board.
		#self.red_left = self.white_left = 12 
		self.squares = [[None for _ in range(COLS)] for _ in range(ROWS)]
		self.create_board(0,0)
		self.draw_squares()
		self.notMove = False
		self.player_row_One, self.player_col_One = 0, 0
		self.player_row_Two, self.player_col_Two = 0, 6
		self.player_row_Three, self.player_col_Three = 6, 6
		self.player_row_Four, self.player_col_Four = 6, 0
		root.bind("<Key>", self.on_key_press)
		self.gameWon = False
		self.buttonPlay= PlayButton(root,self.player_positions)
		self.current_player_index = 1  #change to one later
		self.label = Label(root, text="Turn Player 1", bg="#D3D3D3",padx=10, pady=10)
		self.labelTwo = Label(root, text="Blue", bg="#D3D3D3",padx=10, pady=10)
		self.labelWin = Label(root, text="You Have Won ", bg="#D3D3D3",padx=10, pady=10)
		self.labelPlayer(self.current_player_index)
		
	def getLabelWon(self):
		return self.labelWin

	def getWonGame(self):
		return self.gameWon

	def getPlayerPosOne(self):
		return self.player_row_One,self.player_col_One

	def resizeImage(self,image_path):
		original_image = Image.open(image_path)
		resized_image = original_image.resize((SQUARE_SIZE-50, SQUARE_SIZE-50))
		return ImageTk.PhotoImage(resized_image)

	def get_current_player_index(self):
		return self.current_player_index

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
	
	#here
	def on_key_press(self, event):
		
		if self.current_player_index == 1:
			if event.keysym == "a":
				self.move_player(self.player_row_One, self.player_col_One-1, 1)
			elif event.keysym == "d":
				self.move_player(self.player_row_One, self.player_col_One+1, 1)
	
		if self.current_player_index == 1:
			if event.keysym == "s" or event.keysym == "S":
				self.move_player(self.player_row_One+1, self.player_col_One, 1)
			elif event.keysym == "w":				
				self.move_player(self.player_row_One-1, self.player_col_One, 1)

		if self.current_player_index == 2:
			if event.keysym == "s":
				self.player_row_Two += 1
				self.move_player(self.player_row_Two, self.player_col_Two, 2)
			elif event.keysym == "w":
				self.player_row_Two -= 1
				self.move_player(self.player_row_Two, self.player_col_Two, 2)
			if event.keysym == "a":
				self.move_player(self.player_row_Two, self.player_col_Two-1, 2)
			elif event.keysym == "d":
				self.move_player(self.player_row_Two, self.player_col_Two+1, 2)

		if self.current_player_index == 3:
			if event.keysym == "d":
				self.player_col_Three += 1
				self.move_player(self.player_row_Three, self.player_col_Three, 3)
			elif event.keysym == "a" or event.keysym == "A":
				self.player_col_Three -= 1
				self.move_player(self.player_row_Three, self.player_col_Three, 3)
			if event.keysym == "s" or event.keysym == "S":
				self.move_player(self.player_row_Three+1, self.player_col_Three, 3)
			elif event.keysym == "w" or event.keysym == "W":
				self.move_player(self.player_row_Three-1, self.player_col_Three, 3)

		if self.current_player_index == 4:
			if event.keysym == "s":
				self.move_player(self.player_row_Four+1, self.player_col_Four, 4)
			elif event.keysym == "w":
				self.move_player(self.player_row_Four-1, self.player_col_Four, 4)
		if self.current_player_index == 4:
			if event.keysym == "d":
				self.move_player(self.player_row_Four, self.player_col_Four+1, 4)
			elif event.keysym == "a":
				self.move_player(self.player_row_Four, self.player_col_Four-1, 4)

	#here		
	def getPlayerColorTwo(self):
		return self.image_Two

	def getPlayerColorThree(self):
		return self.image_Three
	
	def getPlayerColorFour(self):
		return self.image_Four

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
				rectPlayerOne =self.squares[0][0]
				rectPlayerOne.config(bg="blue")
				frame = Frame(root, bg="yellow", width=100, height=100)
				frame.grid(row=ROWS//2, column=COLS//2)
		self.squares[0][6].config(bg="green")
		self.squares[6][6].config(bg="#FFA07A")
		self.squares[6][0].config(bg="yellow")
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
				rect = self.squares[row][col]
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
				self.WonGame()
				
	def ButtonWonOnBoard(self):
		self.labelWin.grid(row=(ROWS//2)-1, column=COLS//2,columnspan=2,sticky='nw')
		Game_Won = ButtonWon(root)
		Game_Won.grid(row=ROWS//2,column=COLS//2)
				
	def WonGame(self):
				
		if self.current_player_index==1 and self.player_row_One == 0 and self.player_col_One == 0:
			self.ButtonWonOnBoard()		
		if self.current_player_index==2 and self.player_row_Two == 0 and self.player_col_Two == 6:
			self.ButtonWonOnBoard()	
		if self.current_player_index==3 and self.player_row_Three == 6 and self.player_col_Three == 6:
			self.ButtonWonOnBoard()
		if self.current_player_index==4 and self.player_row_Four == 6 and self.player_col_Four == 0:
			self.ButtonWonOnBoard()
	
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

	def reset_game(self):
		# Reset player positions to their initial state
		self.player_positions = [(0, 0), (0, 6), (6, 6), (6, 0)]
		self.player_row_One, self.player_col_One = 0, 0
		self.player_row_Two, self.player_col_Two = 0, 6
		self.player_row_Three, self.player_col_Three = 6, 6
		self.player_row_Four, self.player_col_Four = 6, 0
		# Reset any game flags or variables
		self.gameWon = False  # Assuming gameWon is a flag to determine if the game is won
		# Redraw the board with initial player positions
		self.getLabelWon().grid_remove()
		self.redraw_board()
		self.buttonPlay.getEndButton().grid_remove()
		self.buttonPlay.grid_remove()
		self.current_player_index=1
		self.buttonPlay= PlayButton(root,self.player_positions)
		self.labelWin.grid_remove()
		self.label.grid_remove()
		self.labelTwo.grid_remove()

root = Tk()
board = Board(root)	
def play():
	root.title("Board")
	root.winfo_toplevel().positionfrom("user")
	root.mainloop()	

