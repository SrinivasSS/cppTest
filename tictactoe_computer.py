from random import *
import random
print "---------------Assignment 1: Cli based Tic Tac Toe---------------\n"
#The following code runs a Tic-Tac-Toe game
#The game is played between 2 players and as is the norm, Player-1 is X and Player-2 is O
#The objective of the game is to get a uninterrupted straight line of X's or O'x (straight row, coloumn or diagnoal)
#The player to first achieve this is the winner
#The code below can be run from the command line using "python assgnmnt1.py" 
#The players give the location of the box where they want to fill with an X or O
#eg grid:	1 | 2 | 3 
#			--|-- |--
#			4 | 5 | 6
#			--|-- |--
#			7 | 8 | 9
#Same boxes cannot be filled again by any player
#EOF error for the input has not been handled as of yet (since this is for python2 not python3), but will be sometime later.


######Drawing the board
def printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9):
	b="'"
	c="--"
	a10="  "
	a11="  "
	a12="  "
	
	print a1,b,a2,b,a3
	print c,b,c,b,c
	print a4,b,a5,b,a6
	print c,b,c,b,c
	print a7,b,a8,b,a9
	print a10,b,a11,b,a12

######Winning combinations
def winningCondition_x(a1,a2,a3,a4,a5,a6,a7,a8,a9):
	if   (a1=="x " and a2=="x " and a3=="x " ) or (a4=="x " and a5=="x " and a6=="x " )  or (a7=="x " and a8=="x " and a9=="x " ):
		return True
	elif (a1=="x " and a4=="x " and a7=="x " ) or (a2=="x " and a5=="x " and a8=="x " )  or (a3=="x " and a6=="x " and a9=="x " ):
		return True
	elif (a1=="x " and a5=="x " and a9=="x " ) or (a3=="x " and a5=="x " and a7=="x " ):
		return True
	else:
		return False
def winningCondition_y(a1,a2,a3,a4,a5,a6,a7,a8,a9):
	if   (a1=="o " and a2=="o " and a3=="o " ) or (a4=="o " and a5=="o " and a6=="o " )  or (a7=="o " and a8=="o " and a9=="o " ):
		return True
	elif (a1=="o " and a4=="o " and a7=="o " ) or (a2=="o " and a5=="o " and a8=="o " )  or (a3=="o " and a6=="o " and a9=="o " ):
		return True
	elif (a1=="o " and a5=="o " and a9=="o " ) or (a3=="o " and a5=="o " and a7=="o " ):
		return True
	else:
		return False
	
a1="  "
a2="  "
a3="  "

a4="  "
a5="  "
a6="  "

a7="  "
a8="  "
a9="  "

printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
#Start game by taking input from player-1
moves=1 #To keep game ON
count=0 #To check draw condition (or when max moves reached)
filledLocs=[] #To check against previous moves
while moves==1:
#####Player-1#######
	while moves==1:
		player1=input("Player-1:Give location of X (1,2,3....,9): ")
		if player1 in filledLocs:
			print "=>Box already filled!"
			continue
		else:
			count+=1
			#print count
			break
	else:
		print "player1Cond!=1"		
	if player1==1:
		a1="x "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	elif player1==2:
		a2="x "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	elif player1==3:
		a3="x "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	elif player1==4:
		a4="x "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	elif player1==5:
		a5="x "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	elif player1==6:
		a6="x "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	elif player1==7:
		a7="x "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	elif player1==8:
		a8="x "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	elif player1==9:
		a9="x "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	else:
		print "Give proper location between 1-9"
		count-=1
		continue
	filledLocs.append(player1)
	#####Check draw condition here as player-1 gets 1 more move than player-2
	if count==9:
		print "Game ended in draw :|"
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		break
	else: 
		pass	
#####Player-2#######
	while moves==1:
		player2=random.choice([1,3,7,9])
		if player2 in filledLocs:
			player2=random.choice([2,4,5,6,8])
			break
			if player2 in filledLocs:
				continue
		else:
			count+=1
			#print count
			break
	else:
		print "playerCond!=1"
	print "Computer played!"
	if player2==1:
		a1="o "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	elif player2==2:
		a2="o "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	elif player2==3:
		a3="o "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	elif player2==4:
		a4="o "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	elif player2==5:
		a5="o "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	elif player2==6:
		a6="o "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	elif player2==7:
		a7="o "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	elif player2==8:
		a8="o "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	elif player2==9:
		a9="o "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		pass
	else:
		print "Give proper location between 1-9"
		continue
	filledLocs.append(player2)
	
	######Check winning conditions	
	if  winningCondition_x(a1,a2,a3,a4,a5,a6,a7,a8,a9):
		print "Game Over: Player-1 Wins!!"
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		break
	elif winningCondition_y(a1,a2,a3,a4,a5,a6,a7,a8,a9):
		print "Game Over: Computer Wins :( "
		printBoard(a1,a2,a3,a4,a5,a6,a7,a8,a9)
		break
	else: 
		continue
else:
	print "Game Over"