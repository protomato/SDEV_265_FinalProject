from ButtonMove import ButtonMove
from tkinter import Button
from Board import  ROWS, COLS

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