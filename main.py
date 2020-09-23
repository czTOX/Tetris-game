import pygame
import functions as fn
import objects as obj


#Constants
width = 700
height = 700
squeare = 30
run = True
background = [196, 99, 38]

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.draw.rect(window, [253, 223, 179], (0, 0, width, height))

fn.drawBoard(window, 200, 50, 600, 300, squeare)

pygame.display.update()


board = [[0 for y in range(20)] for x in range(10)]
board[3][0] = 1

structure = [ 0, 0, 0, 0,
            0, 1, 1, 0,
            0, 1, 1, 0,
            0, 0, 0, 0 ]

for i in range(4):
    for j in range(4):
        board[3+i][j] = structure[4*i+j]



for i in range(10):
    for j in range(20):
        if board[i][j] == 1:
            fn.drawSquere(window, 200+i*squeare, 50+j*squeare, squeare, [255, 255, 255])

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False