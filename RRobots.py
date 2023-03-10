import random

#setting up a board with a goal and a robot on each line
def boardSetup(w, h):
    width = w
    height = h
    randNum1 = random.randint(1,10)
    for x in range(1, height + 1):
        randNum2 = random.randint(1,10)
        for y in range(1, width + 1):
            if x == randNum1 and y == randNum2:
                print("G", end= " ")
                coords = [randNum2, randNum1]
            elif y == randNum2:
                print("R", end=" ")
            else:
                print(".", end=" ")
        print("\n")
    print(coords)

boardSetup(10,10)
