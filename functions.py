import pygame


def drawBoard(window, x, y, height, width, squeare, board):
    #Constants
    background = [105,105,105]
    black = [0, 0, 0]

    #Background
    pygame.draw.rect(window, background, (x, y, width, height))
    pygame.draw.rect(window, black, (x-1, y-1, width+1, height+1), 3)
    

    #Grid
    for i in range(10):
        pygame.draw.line(window, [0, 0, 0], (x+i*squeare, y), (x+i*squeare, y+height), 1)
    
    for j in range(20):
        pygame.draw.line(window, [0, 0, 0], (x, y+j*squeare), (x+width, y+j*squeare), 1)

    #Draw all 1 in a 2D array
    for i in range(10):
        for j in range(20):
            if board[i][j] == 1:
                drawSquere(window, 200+i*squeare, 50+j*squeare, squeare, [255, 255, 255])


    pygame.display.update()


def drawSquere(window, x, y, squeare, color):
    pygame.draw.rect(window, color, (x+1, y+1, squeare-1, squeare-1))
    pygame.display.update()

#TODO need to rework for a whole board
def replaceWithZero(board):
    for i in range(4):
        for j in range(4):
            board[3+i][j] = 0

#TODO replace at any place on the board
def replaceWithShape(board, shape, stageOfTheShape, startPoint = 0):
    for i in range(4):
        for j in range(4):
            board[3+i][j] = shape.structure[stageOfTheShape][4*i+j]
