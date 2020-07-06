from graphics import *
import random


def printme(str):
    print(str)


def calcme(int1, int2):
    return int1 * int2


def main():
    matrix = [[random.randint(1, 4) for i in range(2)] for i in range(2)]
    point1 = Point(14, 36)
    printme(matrix)
    printme(calcme(matrix, matrix))


main()
