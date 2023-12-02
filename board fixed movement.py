from tkinter import Tk, Canvas, Frame, Label ,Button
from PIL import Image, ImageTk
import sys
import pygame
import random
from MiniGame_One import MiniGame_One 
from MiniGame_Two import MiniGame_Two 
from input_text import InputText
from flappy_bird import flappyBird

#newstuff
#POS=0
boardsize=24
qsize=6
board_code =["&","x","_","x","_","x"]*4

pygame.init()
root = Tk()
root.title("Board")

# Constants for window size and grid setup
ROWS,COLS = 7,7 #delimite how many squares you want to have
WIDTH, HEIGHT = 100,100
#size = (WIDTH,HEIGHT)
SQUARE_SIZE = 100  # the size of the square is width divided by number of rows 

SQUARE_SIZE_X = WIDTH // COLS 
SQUARE_SIZE_Y = WIDTH // COLS 

# Image path and positions for player pieces

image_path_Two = "images\playerTwo.png"
original_image_Two = Image.open(image_path_Two)
resized_image2 = original_image_Two.resize((SQUARE_SIZE-50, SQUARE_SIZE-50))           
#image_Two = ImageTk.PhotoImage(resized_image2)

image_path_Three = "images\playerThree.png"
original_image_Three = Image.open(image_path_Three)
resized_image_Three = original_image_Three.resize((SQUARE_SIZE-50, SQUARE_SIZE-50))           
#image_Three = ImageTk.PhotoImage(resized_image_Three)

image_path_Four = "images\playerFour.png"
original_image_Four = Image.open(image_path_Four)
resized_image_Four = original_image_Four.resize((SQUARE_SIZE-50, SQUARE_SIZE-50))           
#image_Four = ImageTk.PhotoImage(resized_image_Four)

#player_positions = [(0, 0), (0, 6), (6, 6), (6, 0)] # list containing multiple tuples each tuple represent the position of     the player on the board

# Define color constants
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

class Player:
    image_path_temp =""
    def __init__(self,tempplayernumber):               
        if tempplayernumber==1:
            self.pos =0
            image_path_temp = "images\playerOne.png"
            self.grid=(0,0)
        if tempplayernumber==2:
            self.pos =6
            image_path_temp = "images\playerTwo.png"
            self.grid=(6,0)
        if tempplayernumber==3:
            self.pos =12
            image_path_temp = "images\playerThree.png"
            self.grid=(6,6)
        if tempplayernumber==4:
            self.pos =18
            image_path_temp = "images\playerFour.png"
            self.grid=(0,6)

        self.movesToWin=boardsize
        self.playnum=tempplayernumber
        original_image_temp = Image.open(image_path_temp)
        resized_image_temp = original_image_temp.resize((SQUARE_SIZE-50, SQUARE_SIZE-50))           
        self.image =ImageTk.PhotoImage(resized_image_temp)
            
    #function position 
    
    def setgrid(self):
        #roll=1   
        global boardsize, qsize # Add player_positions to the list of global variables
        #self.pos=(self.pos+roll)%boardsize
        print(self.pos)
        fliped=(self.pos>=(qsize*2))
        temp=self.pos%(qsize*2)
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
            self.grid = (fi,si)  #player_four position update
        else:
            self.grid = (si,fi)
        print(self.grid)

    def move(self,x):
        self.pos= (self.pos+x)%boardsize
        self.movesToWin-=x
    
    def position(self):
        self.x =self.grid[0]   # x position 
        self.y =self.grid[1]    #y position
        

    def draw(self,rect,player):  #load the image on the board on the giving position by the function position
        if player==1:
            rect.create_image(50, 50, anchor="nw", image=self.image)
        if player==2:
            rect.create_image(0, 50, anchor="nw", image=self.image)
        if player==3:
            rect.create_image(0, 0, anchor="nw", image=self.image)
        if player==4:
            rect.create_image(50, 0, anchor="nw", image=self.image)    


class EndTurnButton(Button):
    def __init__(self,root,player_positions,my_button_move):
        super().__init__(root,text="End Turn ",command=self.on_button_click,width=10,height=3)
        self.player_positions=player_positions
        self.my_button_move=my_button_move

    def on_button_click(self):
        self.grid_remove()
        self.my_button_move.grid(row=ROWS // 2, column=COLS // 2)
        
class PlayButton(Button):
    def __init__(self, root,player_positions):
        # Call the constructor of the base class (Button)
        super().__init__(root, text="Play ", command=self.on_button_click,width=10,height=3)
        self.gameWon = False
        self.button_move = MyButtonMove(root,player_positions,False,text="Move")
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
            print("current player "+str(board.get_current_player_index()))

    def getendTurn(self):
        return self.endTurn

class MyButtonMove(Button):
    def __init__(self, root,player_positions,endTurn,text="Play "):
        # Call the constructor of the base class (Button)
        super().__init__(root, text=text, command=self.on_button_click,width=10,height=3)
        #self.player_positions = player_positions
        self.endTurn = endTurn
        #self.button_move = MyButtonMove(root,player_positions,False,text="Move")
        self.button_End = EndTurnButton(root,player_positions,self)

    def getEndButton(self):
        return self.button_End 

    def on_button_click(self):
        roll=random.randrange(1,6)
        #roll=1
        #print(roll)
        Ptemp=board.get_current_player()
        print(str(Ptemp.playnum)+" moves from "+str(Ptemp.pos)+" to "+str(Ptemp.pos+roll))
        Ptemp.move(roll)
        if board_code[Ptemp.pos]=="x":
            Ptemp = red_land(Ptemp)
        Ptemp.setgrid()
        board.move_player(Ptemp.grid[1],Ptemp.grid[0],board.get_current_player_index()-1)
        board.set_current_player(Ptemp)
        if board_code[Ptemp.pos]=="&":
            Ptemp = blue_land()
        board.update_players()
        

class Board:
    def __init__(self):
        self.PLAYERS=[Player(1),Player(2),Player(3),Player(4)]
        self.board = [] # Initialize an empty list to represent the game board.
        self.player_positions = [(0, 0), (6,0), (6, 6), (0,6)]    
        self.red_left = self.white_left = 12 
        self.squares = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.create_board(0,0)
        self.draw_squares()
        self.notMove = False
        #self.player_row_One, self.player_col_One = 0, 0
        #self.player_row_Two, self.player_col_Two = 0, 6
        #self.player_row_Three, self.player_col_Three = 6, 6
        #self.player_row_Four, self.player_col_Four = 6, 0
        root.bind("<Key>", self.on_key_press)
        self.gameWon = False
        self.buttonPlay=PlayButton(root,self.player_positions)
        self.current_player_index = 1
        self.num_of_players=4
        self.label = Label(root, text="Turn Player 1", bg="#D3D3D3",padx=10, pady=10)
        self.labelTwo = Label(root, text="Blue", bg="#D3D3D3",padx=10, pady=10)
        self.labelWin = Label(root, text="You Have Won ", bg="#D3D3D3",padx=10, pady=10)
        self.labelPlayer(self.current_player_index)

    def get_current_player_index(self):
        return self.current_player_index
    
    def get_current_player(self):
        return self.PLAYERS[self.current_player_index-1]
    
    def set_current_player(self,temp):
        self.PLAYERS[self.current_player_index-1]=temp
        if  self.PLAYERS[self.current_player_index-1].movesToWin<=0:
            pygame.quit()
            sys.exit()
            print("player "+str(self.current_player_index)+" won")

    def swap_current_player(self):
        # Toggle the current player's index (0 to 1, 1 to 0)
        self.current_player_index = 2 if self.current_player_index == 1 else 1

    def swap_current_four_players(self):
        if self.current_player_index == 4:
            self.current_player_index = 4 if self.current_player_index == 1 else 1
        elif self.current_player_index == 3:
            self.current_player_index = 3 if self.current_player_index == 4 else 4
        elif self.current_player_index == 2:
            self.current_player_index = 2 if self.current_player_index == 3 else 3
        elif self.current_player_index == 1:
            self.current_player_index = 1 if self.current_player_index == 2 else 2
        else :
            print ("Not a player")

    def update_players(self):
        self.current_player_index += 1
        if self.current_player_index>self.num_of_players:
            self.current_player_index = 1
        self.labelPlayer(self.current_player_index)


    def getPlayButton(self):
        return self.buttonPlay

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
        self.redraw_board()
    
    def create_board(self,row,col):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if (row, col) in [(0, 0), (0, 6), (6, 6), (6, 0)]:
                    #print(str(row)+" "+str(col))
                    self.board[row].append(self.PLAYERS[0])
                    self.board[row].append(self.PLAYERS[1])
                    self.board[row].append(self.PLAYERS[2])
                    self.board[row].append(self.PLAYERS[3])
                else:
                    self.board[row].append(0)
        
    def move_player(self,new_row,new_col,player):
        self.player_positions=[]
        for x in self.PLAYERS:
            self.player_positions.append(x.grid)
        print(self.player_positions)
        self.redraw_board()    
    # ... (other methods) ...

    def redraw_board(self):
        # Redraw the board with updated player position
        print("redraw")
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
                canvas_widget=self.squares[self.player_positions[0][1]][self.player_positions[0][0]]#control movement player one
                canvas_widget.create_image(50, 50, anchor="nw", image=self.PLAYERS[0].image)
                
                #player 2
                rect = self.squares[0][6]
                canvas_widget=self.squares[self.player_positions[1][1]][self.player_positions[1][0]]    #control movement player 2
                canvas_widget.create_image(0, 50, anchor="nw", image=self.PLAYERS[1].image)
                
                #player 3
                rect = self.squares[row][col]
                rect = self.squares[6][6]
                canvas_widget=self.squares[self.player_positions[2][1]][self.player_positions[2][0]]    #control movement player 3
                canvas_widget.create_image(0, 0, anchor="nw", image=self.PLAYERS[2].image)
    
                #player 4
                rect = self.squares[row][col]
                rect = self.squares[6][0]
                canvas_widget=self.squares[self.player_positions[3][1]][self.player_positions[3][0]]    #control movement player 4
                canvas_widget.create_image(50, 0, anchor="nw", image=self.PLAYERS[3].image)
    
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

def blue_land():
    rand=random.randrange(1,4)
    itt= InputText()
    itt.runInputBox()
    aceptable=["1","2","3","4"]
    Ptemp=board.PLAYERS[rand-1]
    if itt.getInput() in aceptable:
        Ptemp=board.PLAYERS[int(itt.getInput())]


    Ptemp.move(-2)
    #print(Ptemp.grid)
    Ptemp.setgrid()
    if itt.getInput() in aceptable:
        board.move_player(Ptemp.grid[1],Ptemp.grid[0],int(itt.getInput()))
        board.PLAYERS[int(itt.getInput())]=Ptemp
    else:
        board.move_player(Ptemp.grid[1],Ptemp.grid[0],rand-1)
        board.PLAYERS[rand-1]=Ptemp
        
def red_land(player):
    return player
    rand=random.randrange(1,4)
    print(rand)
    if rand==1:
        game = MiniGame_One()
    elif rand==2:
        game = MiniGame_Two()
    elif rand==3:
        game = flappyBird()
    else:
        print("HGBI*YGBI*YB")
        #return player
    
        
    game.Play_Mini()
    if game.getWon():
        return player
    player.move(-random.randrange(1,4))
    return player

    
info = pygame.display.Info()

# Get screen width and height
screen_width = info.current_w
screen_height = info.current_h

# Calculate the center of the screen
center_x = screen_width // 2
center_y = screen_height // 2

board = Board()


def play():
        pygame.init()
        root.mainloop()

play()