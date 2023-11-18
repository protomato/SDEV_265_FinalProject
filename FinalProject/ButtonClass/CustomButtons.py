from tkinter import Button
from Board import board
from MiniGame_One import MiniGame_One 
from MiniGame_Two import MiniGame_Two 
import random

ROWS,COLS = 7,7

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
		pos = 0
		boardsize=24
		qsize=6
		roll=random.randrange(1,6)
		#roll=1   
		#global pos, boardsize, qsize # Add player_positions to the list of global variables
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
				self.player_positions[0] = [(si,fi)]  #player_One position update
				board.move_player(si,fi,1)
			elif board.get_current_player_index()==2:
				self.player_positions[1] = [(si,fi)]  #player_two position update
				board.move_player(si,fi,2)
			elif board.get_current_player_index()==3:
				self.player_positions[2] = [(si,fi)]  #player_three position update
				board.move_player(si,fi,3)
			else:
				self.player_positions[3] = [(si,fi)]  #player_four position update
				board.move_player(si,fi,4)
		else:
			if board.get_current_player_index()==1:
				self.player_positions[0] = [(fi,si)]  #player_One position update
				board.move_player(fi,si,1)
			elif board.get_current_player_index()==2:
				self.player_positions[1] = [(fi,si)]  #player_two position update
				board.move_player(fi,si,2)
			elif board.get_current_player_index()==3:
				self.player_positions[2] = [(fi,si)]  #player_three position update
				board.move_player(fi,si,3)
			else:
				self.player_positions[3] = [(fi,si)]  #player_four position update
				board.move_player(fi,si,4)
				#print(self.player_positions)