import turtle
import time
import numpy as np
import random

player = 1
vertLines = 0
horizontaLines = 0
squareNumber = 0
coordinates = [{'x': -140, 'y': 60},{'x': -40, 'y': 60},{'x': 60, 'y': 60}, {'x': -140, 'y': -40}, {'x': -40, 'y': -40}, {'x': 60, 'y': -40}, {'x': -140, 'y': -140}, {'x': -40, 'y': -140}, {'x': 60, 'y': -140}]
wins = False
isPlaying = True
comp_player = random.randint(0, 1)

def whocomputer():
	t.penup()
	t.goto(0, -250)
	t.pendown()
	t.color("red")
	if comp_player == 0:
		t.write(("The computer is player 'X'"), False, "center", ("Arial", 30, "normal"))
	if comp_player == 1:
		t.write(("The computer is player 'O'"), False, "center", ("Arial", 30, "normal"))		

size = 9
playingField = [0] * size

t = turtle.Turtle()
t.shape("turtle")
t.width(5)
t.penup()
t.goto(-50, -150)
t.pendown()
t.color("red")

s = turtle.Screen()

def draw_x(squareNumber):
	x_start_coord = coordinates[squareNumber]['x']
	y_start_coord = coordinates[squareNumber]['y']
	t.setheading(90)
	t.penup()
	t.goto(x_start_coord, y_start_coord)
	t.pendown()
	t.color("black")
	t.right(45)
	t.forward(105)
	t.setheading(90)
	t.penup()
	t.goto(x_start_coord + 80, y_start_coord)
	t.pendown()
	t.left(45)
	t.forward(105)

def draw_o(squareNumber):
	x_start_coord = coordinates[squareNumber]['x']
	y_start_coord = coordinates[squareNumber]['y']
	t.setheading(0)
	t.penup()
	t.goto(x_start_coord + 40, y_start_coord)
	t.pd()
	t.circle(40)

def location(x_coordinate, y_coordinate):
	if y_coordinate in range(50, 150):
		if x_coordinate in range(-150, -50):
			squareNumber = 1
			print("You clicked in the 1st square")
			play(squareNumber)
		if x_coordinate in range(-50, 50):
			squareNumber = 2
			print("You clicked in the 2nd square")
			play(squareNumber)
		if x_coordinate in range(50, 150):
			squareNumber = 3
			print("You clicked in the 3rd square")
			play(squareNumber)
	
	if y_coordinate in range(-50, 50):
		if x_coordinate in range(-150, -50):
			squareNumber = 4
			print("You clicked in the 4th square")
			play(squareNumber)
		if x_coordinate in range(-50, 50):
			squareNumber = 5
			print("You clicked in the 5th square")
			play(squareNumber)
		if x_coordinate in range(50, 150):
			squareNumber = 6
			print("You clicked in the 6th square")
			play(squareNumber)
	
	if y_coordinate in range(-150, -50):
		if x_coordinate in range(-150, -50):
			squareNumber = 7
			print("You clicked in the 7th square")
			play(squareNumber)
		if x_coordinate in range(-50, 50):
			squareNumber = 8
			print("You clicked in the 8th square")
			play(squareNumber)
		if x_coordinate in range(50, 150):
			squareNumber = 9
			print("You clicked in the 9th square")
			play(squareNumber)

def play(squareNumber):
	global player
	global isPlaying
	if isPlaying:
		playingField[squareNumber - 1] = player 
		if player == 1:
			player = 2
			if comp_player == 0:
				computer()
			if comp_player == 1:
				draw_x(squareNumber-1)
				check_if_wins(playingField,1)
		if player == 2:
			player = 1
			if comp_player == 0:
				draw_o(squareNumber-1)
				check_if_wins(playingField,2)
			if comp_player == 1:
				computer()

def computer():

def neighbors(cell):
	cell_y = cell / 3
	cell_x = cell % 3
	neighbors = []
	if (x-1) >= 0:
		if (y-1) >= 0:
			neighbors.append((y-1) * 3 + (x-1))
		if (y+1) >= 2:
			neighbors.append((y+1) * 3 + (x-1))
		neighbors.append(y * 3 + (x-1))


def next_move(board, opposingPlayer, computerPlayer):
	if board[0] == computerPlayer:
		if 
def draw_field():
	global xCoordinate
	xCoordinate = -50
	global yCoordinate
	yCoordinate = -150
	t.left(90)
	for vertLines in range(1, 3):
		t.penup()
		t.goto(xCoordinate, yCoordinate)
		t.pendown()
		xCoordinate = xCoordinate + 100
		t.forward(300)
		vertLines = vertLines + 1
	xCoordinate = 150
	yCoordinate = 50
	t.left(90)
	for horizontaLines in range(1, 3):
		t.penup()
		t.goto(xCoordinate, yCoordinate)
		t.pendown()
		yCoordinate = yCoordinate - 100
		t.forward(300)
		horizontaLines = horizontaLines + 1

	t.penup()
	t.goto(-200, -200)
	t.pendown()

def check_if_wins(board, player):
	global isPlaying
	global wins
	wins = False
	if board[2] == player:
		if board[0] == board[1] == board[2] == player:
			wins = True
		if board[2] == board[5] == board[8] == player:
			wins = True
		if board[2] == board[4] == board[6] == player:
			wins = True			
	if board[4] == player:
		if board[3] == board[4] == board[5] == player:
			wins = True
		if board[1] == board[4] == board[7] == player:
			wins = True
		if board[0] == board[4] == board[8] == player:
			wins = True
		if board[2] == board[4] == board[6] == player:
			wins = True
	if board[6] == player:
		if board[0] == board[3] == board[6] == player:
			wins = True
		if board[6] == board[7] == board[8] == player:
			wins = True
		if board[2] == board[4] == board[6] == player:
			wins = True

	if playingField.count(0) == 0:
		if wins == False:
			t.color("blue")
			t.penup()
			t.goto(120, 0)
			t.pendown()
			t.write(("Draw!"), False, "right", ("Arial", 80, "normal"))


	if wins:
		isPlaying = False
		t.color("blue")
		t.penup()
		t.goto(150, 0)
		t.pendown()
		if player == 1:
			t.write(("'X' wins!"), False, "right", ("Arial", 80, "normal"))
		else:
			t.write(("'O' wins!"), False, "right", ("Arial", 80, "normal"))	

# def checkRows(board):
#     for row in board:
#         if len(set(row)) == 1:
#             return row[0]
#     return 0

# def checkDiagonals(board):
#     if len(set([board[i][i] for i in range(len(board))])) == 1:
#         return board[0][0]
#     if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
#         return board[0][len(board)-1]
#     return 0

# def checkWin(board):
#     #transposition to check rows, then columns
#     for newBoard in [board, np.transpose(board)]:
#         result = checkRows(newBoard)
#         if result:
#             return result
#     return checkDiagonals(board)

draw_field()
whocomputer()
turtle.onscreenclick(location)
turtle.mainloop()

