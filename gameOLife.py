import math
import random
import numpy as np
import time

def makeAnArray(rows,cols):
    randArray= np.random.randint(0,2, size=(rows,cols)) #creates a random matrix between 0 (inclusive) and 2 (exclusive)
    randArray = np.pad(randArray, pad_width=1, mode='constant', constant_values="0") #creates a border
    return randArray


def GoL(array):
    rows = len(array)
    cols = len(array[0])
    newArray = np.zeros((rows,cols))
    for i in range (1,rows - 1): # 1 to rows-1 because you are ignoring the padded border this way
        for j in range (1,cols - 1):
            count = 0 #how many cells there are around the target cell
            if array[i-1][j-1] == 1:
                count += 1
            if array[i-1][j] == 1:
                count += 1
            if array[i-1][j+1] == 1:
                count += 1
            if array[i][j-1] == 1:
                count += 1
            if array[i][j+1] == 1:
                count += 1
            if array[i+1][j-1] == 1:
                count += 1
            if array[i+1][j] == 1:
                count += 1
            if array[i+1][j+1] == 1:
                count += 1

            if array[i][j] == 1 and count == 2:      #conditions for the rules. I can't figure out how to make it in a separate function while keeping the i,j, etc
                newArray[i][j] = 1
            elif count == 3:
                newArray[i][j] = 1
            else:
                newArray[i][j] = 0

            count = 0
    print(newArray)
    return newArray




array = makeAnArray(5,5)
newerArray = GoL(array)

i = 0
while(i< 10):
    GoL(newerArray)
    time.sleep(1)
    i += 1
