import pygame


def drawBoard(window, x, y, height, width, squeare):
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

    pygame.display.update()


def drawSquere(window, x, y, squeare, color):
    pygame.draw.rect(window, color, (x+1, y+1, squeare-1, squeare-1))
    pygame.display.update()
