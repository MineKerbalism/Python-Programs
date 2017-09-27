import turtle
import time

def set_things():
	global player
	player = 1
	global squareNumber
	squareNumber = 0
	global coordinates
	coordinates = [{'x': -140, 'y': 60},{'x': -40, 'y': 60},{'x': 60, 'y': 60}, {'x': -140, 'y': -40}, {'x': -40, 'y': -40}, {'x': 60, 'y': -40}, {'x': -140, 'y': -140}, {'x': -40, 'y': -140}, {'x': 60, 'y': -140}]
	global wins
	wins = False
	global isPlaying
	isPlaying = True
	global size
	size = 9
	global playingField
	playingField = [0] * size


set_things()
t = turtle.Turtle()
t.shape("turtle")
t.width(5)
t.penup()
t.goto(-50, -150)
t.pendown()
t.color("red")
t.speed(0)

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
	if isPlaying == False and x_coordinate in range(40, 260) and y_coordinate in range(-285, -200):
		reset()
	else:
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
	if isPlaying == True:
		playingField[squareNumber - 1] = player 
		if player == 1:
			player = 2
			draw_x(squareNumber-1)
			check_if_wins(playingField,1)
		else:
			player = 1
			draw_o(squareNumber-1)
			check_if_wins(playingField,2)

def reset():
	t.reset()
	t.shape("turtle")
	t.width(5)
	t.penup()
	t.goto(-50, -150)
	t.pendown()
	t.color("red")
	draw_field()
	set_things()
	


	
def draw_field():
	vertLines = 0
	horizontaLines = 0
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
	
	if (board[0] == board[1] == board[2] == player or 
		board[2] == board[5] == board[8] == player or 
		board[2] == board[4] == board[6] == player or
		board[3] == board[4] == board[5] == player or 
		board[1] == board[4] == board[7] == player or 
		board[0] == board[4] == board[8] == player or
		board[6] == board[7] == board[8] == player or 
		board[0] == board[3] == board[6] == player):
		
		wins = True


	if playingField.count(0) == 0 and wins == False:	
		isPlaying = False
		t.color("blue")
		t.penup()
		t.goto(120, 0)
		t.pendown()
		t.write(("Draw!"), False, "right", ("Arial", 80, "normal"))
		t.penup()
		t.goto(150, -260)
		t.pendown()
		t.write(("Play Again!"), False, "center", ("Arial", 36, "normal"))
		t.penup()
		t.goto(40, -200)
		t.setheading(270)
		t.pendown()
		sides = 0
		while sides <= 2:
			t.forward(85)
			t.left(90)
			t.forward(220)
			t.left(90)
			sides = sides + 1
			
	if wins == True:
		isPlaying = False
		t.color("blue")
		t.penup()
		t.goto(150, 0)
		t.pendown()
		if player == 1:
			t.write(("'X' wins!"), False, "right", ("Arial", 80, "normal"))
		else:
			t.write(("'O' wins!"), False, "right", ("Arial", 80, "normal"))
		
		t.penup()
		t.goto(150, -260)
		t.pendown()
		t.write(("Play Again!"), False, "center", ("Arial", 36, "normal"))
		t.penup()
		t.goto(40, -200)
		t.setheading(270)
		t.pendown()
		sides = 0
		while sides <= 2:
			t.forward(85)
			t.left(90)
			t.forward(220)
			t.left(90)
			sides = sides + 1

draw_field()
turtle.onscreenclick(location)
turtle.mainloop()

