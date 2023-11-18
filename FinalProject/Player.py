class Player:
	def __init__(self,row,col,image,board):			   
		self.image = image
		self.row = row
		self.col = col
		self.board=board

		#function position 
	def position(self):
		self.x =self.col   # x position 
		self.y =self.row   #y position
		

	def draw(self,rect,player):  #load the image on the board on the giving position by the function position
		if player==1:
			rect.create_image(50, 50, anchor="nw", image=self.image)
		if player==2:
			rect.create_image(0, 50, anchor="nw", image=self.board.getPlayerColorTwo())
		if player==3:
			pass
			rect.create_image(0, 0, anchor="nw", image=self.board.getPlayerColorThree())
		if player==4:
			rect.create_image(50, 0, anchor="nw", image=self.board.getPlayerColorFour())			
