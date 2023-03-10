import random


#defining a rectangular board (https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array)
def createBoard(x,y):
    board = [["x" for i in range(x)] for j in range(y)] 
    return board

#inserting given amount of robots into the board
def insertRobots(board, n):
    robots = 0
    while robots<n:
        for i in range (0,len(board)):
            for j in range (0,len(board[0])):
                if random.randint(1,len(board)*len(board)/n) == 1 and board[i][j]=="x":
                    board[i][j] = "!"
                    robots = robots+1
                if robots == n:
                    return board
       
#defining the printing of the board
def printBoard(board):
    for i in range (0,len(board)):
        for j in range (0,len(board[0])):
            print(board[i][j]),
        print("")

#actual calling of the function
blank_board = createBoard(6,6)
robot_board = insertRobots(blank_board, 3)
printBoard(robot_board)


