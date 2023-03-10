import random


#defining a rectangular board (https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array)
def createBoard(x,y):
    board = [["." for i in range(2*x+1)] for j in range(2*y+1)] 
    for i in range (0, len(board)):
        for j in range (0, len(board[0])):
            if j == 0 and i!=0:
                board[i][j] = "|"
            elif j == len(board[0])-1 and i!=0:
                board[i][j] = "|"
            elif i == 0 and j!=0 and j!=len(board[0])-1:
                board[i][j] = "_"
            elif i == len(board)-1 and j!=0:
                board[i][j] = "_"
            #Create blank spaces every other spot on the board (for the walls to be inserted into)
            elif j%2 == 0:
                board[i][j] = " "
            elif i%2 == 0:
                board[i][j] = " "
    return board

#inserting given amount of robots into the board
def insertRobots(board, n):
    robots = 0
    while robots<n:
        for i in range (0,len(board)):
            for j in range (0,len(board[0])):
                if board[i][j] == "." and random.randint(1,len(board)*len(board)/n) == 1:
                    board[i][j] = "R"
                    robots = robots+1
                if robots == n:
                    return board

def insertVerticalWalls(board):
    walls = 0
    n = (len(board)-1)/2
    #go through the odd rows and look for an open space. Randomly insert a vertical wall into this space. 
    #Check each row to see if it has a wall. If a row already has a wall, do not place another wall on that row. Continue until all rows have one wall.
    while walls<n:
        for i in range (1,len(board)):
            for j in range (1,len(board[0])):
                if board[i][j] == " " and random.randint(1,len(board)) ==1 and i%2==1:
                    board[i][j] = "|"
                    walls = walls+1
                #stops the while loop after there are n walls
                if walls == n:
                    return board
                    #print("i: "+ str(i) + ", j: " + str(j))         
  
#Start with row 0. Pick a random number from 0 to n-1 that will designate the index of the row. Insert vertical line at this spot. Repeat for all rows.
#This is where I can start next time. This is a different method than the way above (for inserting walls)
def insertHorizontalWalls(board):
    walls = 0
    n = (len(board)-1)/2




       
#defining the printing of the board
def printBoard(board):
    for i in range (0,len(board)):
        for j in range (0,len(board[0])):
            print(board[i][j]),
        print("")

#actual calling of the function
blank_board = createBoard(6,6)
robot_board = insertRobots(blank_board, 3)
wall_board = insertVerticalWalls(robot_board)
printBoard(wall_board)
