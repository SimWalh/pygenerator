from graphics import GraphWin, Point, Rectangle, update, GraphicsError
import random
import time

import cProfile
import re

states = {"alive forever":0, "alive":1, "dead":2, "dead forever":3}
color_list = {0:"white", 1:"gray75", 2:"gray10", 3:"black", -1:"red"}

#test for testcommit

def generaterooms(dest_mat, n_rooms_horiz, n_rooms_vertic, chance_percent):
    """
    Generates a Matrix of e.g. 4x4 Points for 16 Rooms consisting of (Float!) coordinates, 
    that represent locations in the main map tile matrix
    
    Parameters:
        dest_mat: Matrix on wich the rooms should be placed
        n_rooms_horiz: Number of rooms in hosizontal direction
        n_rooms_vertic: Number of rooms in vertical direction
        chance_percent: Percentage chance that a room is placed

    Returns:
        A modified dest_mat with the rooms placed in it
    """
    
    gridRows = len(dest_mat) #number of rows in the destination matrix
    gridCols = len(dest_mat[0]) #number of columns in the destination matrix
    n_rows = n_rooms_vertic  # no of rows of rooms
    n_rooms_per_row = n_rooms_horiz  # no of rooms per row
    
    roomHeight = gridCols / n_rows #height of a point placement area / "room"
    roomWidth = gridRows / n_rooms_per_row  #width of a point placement area / "room"
    arealimit = 0.6 # percentage of room height / width that is valid for point placement (centered)

    pointAreaH = roomHeight * arealimit #actual area height in wich points can be placed
    pointAreaW = roomWidth * arealimit #actual area width in wich points can be placed
    
    roommap = [[Point(i, j) for i in range(n_rooms_per_row)] for j in range(n_rows)] #list of room coordinates, initialized

    for rowNr in range(len(roommap)):  # for a row in the matrix
        for roomNr in range(len(roommap[rowNr])):  # for a room in a row
            roomcenter = Point((roomNr - 0.5) * roomWidth, (rowNr - 0.5) * roomHeight) #calculate the center position of the room
            randomPoint = Point(random.randint(int(-pointAreaW/2), int(pointAreaW/2)), random.randint(int(-pointAreaH/2), int(pointAreaH/2))) #generate random point, area centered around 0
            px = round(roomcenter.getX() + randomPoint.getX())
            py = round(roomcenter.getY() + randomPoint.getY())
            roommap[rowNr][roomNr] = Point(px, py) #move area center over room center
    return placerooms(dest_mat, roommap, states["alive forever"], chance_percent) #place the generated rooms on the destination matrix and return that

def drawcanvas(mat, zoom, win):
    """
    Draw the provided matrix of map tiles into the provided window.
    
    Parameters: 
        mat: Matrix of tiles to be drawn, eg a level map
        zoom: amount of magnification (eg 10, 1 tile is 10x10px)
        window: Graphics.py GraphWin on wich to draw

    Returns: nothing
    """
    # iterate over all elements of the matrix
    for row in range(len(mat)):
        for element in range(len(mat[row])):
            # Calculate upper left and lower right points of pixels
            pointUL = Point(element * zoom, row * zoom)
            pointLR = Point((element + 1) * zoom, (row + 1) * zoom)
            # place a rectangle there
            item = Rectangle(pointUL, pointLR)
            # in the color corresponding to the elements alive state
            state = mat[row][element]
            item.setFill(color_list[state])
            # draw it
            item.draw(win)
    update()  # update screen when all elements are drawn (performance)
    print("updated")
    win.flush()
    print("flushed")

def doCellularAutomation(inputMatrix, n):
    """
    Run n iterations of a cellular automaton on the provided matrix

    Parameters:
        inputMatrix: Matrix on wich to run the cellular automation
        n: Number of cycles to run

    Returns: The resulting matrix
    """
    outputMatrix = inputMatrix #initialize output matrix with same size and values as input
    matrixHeight = len(inputMatrix)
    matrixWidth = len(inputMatrix[0])
    aliveReq = 4
    for i in range(n):
        for row in range(matrixHeight):
            for element in range(matrixWidth):
                state_old = inputMatrix[row][element]
                # calculate alive status
                if state_old == 0 or state_old == 3:
                    outputMatrix[row][element] = state_old
                else:
                    # number of living neighbours
                    num_n_alive = 0
                    for y in range(row - 1, row + 2):
                        if y < 0 or y > (matrixHeight - 1):
                            continue
                        for x in range(element - 1, element + 2):
                            if (x < 0 or x > (matrixWidth - 1)):
                                continue

                            state_n = inputMatrix[y][x]
                            if state_n == 0 or state_n == 1:  # alive forever or alive
                                num_n_alive += 1
                    if num_n_alive > aliveReq:
                        outputMatrix[row][element] = states["alive"] 
                    else:
                        outputMatrix[row][element] = states["dead"] 
        inputMatrix = outputMatrix #prepare to start over with the resulting matrix as the new input    
        print("Simulated", i, "times...") #log and remove "i is not used blablabla" error...
    return outputMatrix

def placerooms(input_mat, input_roomPositions, dest_val, chance_percent):
    """
    Place rooms on the map

    Parameters:
        input_mat: Matrix on wich to place the rooms
        input_roomPositions: Matrix of rooms with position coordinates
        dest_val: value to place on the maps where the rooms are
        chance_percent: Percentage chance that a room is actually placed

    Returns: The resulting matrix
    """
    for roomrow in range(len(input_roomPositions)):
        for room in range(len(input_roomPositions[roomrow])): #iterate over all items in the roomPositions Matrix

            #get x and y positions for each room
            x = int(round(input_roomPositions[roomrow][room].getX()))
            y = int(round(input_roomPositions[roomrow][room].getY()))

            #Placement chance evaluation
            if (chance_percent > random.randint(1,100)):
                dest_val = dest_val
            else:
                #if no room should be placed still place it as "alive" so it can be deleted if theres nothing around it
                dest_val = states["alive"] 

            #set 3x3 area
            input_mat[y-1][x-1] = dest_val 
            input_mat[y-1][x] = dest_val 
            input_mat[y-1][x+1] = dest_val
            input_mat[y][x-1] = dest_val
            input_mat[y][x] = dest_val 
            input_mat[y][x+1] = dest_val
            input_mat[y+1][x-1] = dest_val
            input_mat[y+1][x] = dest_val
            input_mat[y+1][x+1] = dest_val
    return input_mat #return the modified matrix
    
def main():
    pixelsize = 10
    listsizeH, listsizeW = 100, 100
    # open a window to size
    cellsWindow = GraphWin("Cells", pixelsize * listsizeW - 1, pixelsize * listsizeH - 1, autoflush=False)
    # main loop

    matrix = [[random.randint(1, 2) for i in range(listsizeW)] for i in range(listsizeH)]
    #matrix = [[states["dead"] for i in range(listsizeW)] for i in range(listsizeH)]
    matrix = generaterooms(matrix, 4,4, 50)

    while (1):
        matrix = doCellularAutomation(matrix,10)
        drawcanvas(matrix, pixelsize,cellsWindow)
        try:
            cellsWindow.getMouse()  # Pause to view result
        except GraphicsError:
            pass  # ignore if window already closed
            break
    cellsWindow.close()  # Close window when done



# pr = cProfile.Profile()
# pr.enable()
main()
# pr.disable()
# pr.print_stats(sort='cumtime')