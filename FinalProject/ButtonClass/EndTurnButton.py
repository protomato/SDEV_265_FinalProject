#from ButtonMove import *
from Board import board, ROWS, COLS
from tkinter import Button


class EndTurnButton(Button):
	def __init__(self,root,player_positions,my_button_move):
		super().__init__(root,text="End Turn ",command=self.on_button_click,width=10,height=3)
		self.player_positions=player_positions
		self.my_button_move=my_button_move

	def on_button_click(self):
		self.grid_remove()
		self.my_button_move.grid(row=ROWS // 2, column=COLS // 2)
		board.labelPlayer(board.get_current_player_index())