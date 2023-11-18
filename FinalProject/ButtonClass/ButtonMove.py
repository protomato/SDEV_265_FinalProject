import random
from tkinter import Button
from EndTurnButton import EndTurnButton
from Board import board

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