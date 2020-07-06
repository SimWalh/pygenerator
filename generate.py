from graphics import GraphWin, Point, Rectangle, update, GraphicsError
import random
import time

import cProfile

pixelsize = 10
listsizeH, listsizeW = 100, 100
aliveRequirement = 4
colors = ["white", "gray75", "gray10", "black"]


def main():
    '''states:
        0: alive forever
        1: alive
        2: dead
        3: dead forever
        '''

    cellsWindow = GraphWin("Cells",
                           pixelsize * listsizeW - 1,
                           pixelsize * listsizeH - 1,
                           autoflush=False)

    while (1):
        matrix = [[random.randint(1, 2) for i in range(listsizeW)]
                  for i in range(listsizeH)]

        matrix = generaterooms(matrix)
        for i in range(5):
            matrix = doCellularAutomation(matrix)
        drawcanvas(matrix, cellsWindow)
        update()

        try:
            cellsWindow.getMouse()  # Pause to view result
        except GraphicsError:
            pass                    # ignore if window already closed
            break

    cellsWindow.close()  # Close window when done

def generaterooms(mat)
    # this is a test for git, now generation of mazes is done
    return mat

def drawcanvas(mat, win):
    # iterate over all elements of the matrix
    for row in range(len(mat)):
        for element in range(len(mat[row])):
            # Calculate upper left and lower right points of pixels
            pointUL = Point(element * pixelsize, row * pixelsize)
            pointLR = Point((element + 1) * pixelsize, (row + 1) * pixelsize)
            # draw a pixel there
            item = Rectangle(pointUL, pointLR)
            # in the color corresponding to the elements alive state
            state = mat[row][element]
            item.setFill(colors[state])
            # draw it
            item.draw(win)
    # update()  # update screen when all elements are drawn (performance)


def doCellularAutomation(inputMatrix):

    outputMatrix = inputMatrix
    for row in range(listsizeH):
        for element in range(listsizeW):
            state_old = inputMatrix[row][element]
            # calculate alive status
            if state_old == 0 or state_old == 3:
                outputMatrix[row][element] = state_old
            else:
                # number of living neighbours
                num_n_alive = 0
                for y in range(row - 1, row + 2):
                    if y < 0 or y > (listsizeH - 1):
                        continue
                    ''' #or ((y == row) and (x == element))): 
                        when the focused cell is also counted, 
                        this acts like leaving the cell as is 
                        when the alivereqirement is exactly met'''
                    for x in range(element - 1, element + 2):
                        if (x < 0 or x > (listsizeW - 1)):
                            continue

                        state_n = inputMatrix[y][x]
                        if state_n == 0 or state_n == 1:  # alive forever or alive
                            num_n_alive += 1
                '''leave as is when req. is exactly met is implemented, because cell itself is counted towards alive neighbours'''
                if num_n_alive > aliveRequirement:
                    outputMatrix[row][element] = 1  # alive
                else:
                    outputMatrix[row][element] = 2  # dead
    return outputMatrix


main()
