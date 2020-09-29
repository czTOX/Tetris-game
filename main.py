import pygame
import functions as fn
import objects as obj
import random


#Constants
width = 700
height = 700
squeare = 30
run = True
background = [196, 99, 38]
board = [[0 for y in range(20)] for x in range(10)]

shapeO = obj.Oshape()
shapeI = obj.Ishape()
shapeS = obj.Sshape()
shapeZ = obj.Zshape()
shapeL = obj.Lshape()
shapeJ = obj.Jshape()
shapeT = obj.Tshape()

shapeArray = [shapeO, shapeI, shapeS, shapeZ, shapeL, shapeJ, shapeT]


#Basic layout
pygame.init()
window = pygame.display.set_mode((width, height))
pygame.draw.rect(window, [253, 223, 179], (0, 0, width, height))
fn.drawBoard(window, 200, 50, 600, 300, squeare, board)
pygame.display.update()

shape = random.choice(shapeArray)
stageOfTheShape = 0


#Replace chunk of 2D board with a shape block
for i in range(4):
    for j in range(4):
        board[3+i][j] = shape.structure[stageOfTheShape][4*i+j]

fn.drawBoard(window, 200, 50, 600, 300, squeare, board)


#Main loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                lenght = len(shape.structure)-1
                if stageOfTheShape < lenght:
                    stageOfTheShape+=1
                elif stageOfTheShape == lenght:
                    stageOfTheShape = 0
                fn.replaceWithZero(board)
                fn.replaceWithShape(board, shape, stageOfTheShape)

                fn.drawBoard(window, 200, 50, 600, 300, squeare, board)

