import numpy as np
import pygame
import math
import sys

R = 3
C = 3
sqsize = 200
radcir = 60
offset = 55
Owidth= 15
Xwidth = 25
scnwidth = C * sqsize
scnheigth = R * sqsize
linecolor = (0,0,0)
bgcolor = (255,255,0)
Ocolor= (255,105,180)
Xcolor = (255,0,0)
player = 0
gameover = False
inmenu = True

def printingboard():
    fb = np.flip(Board, 0)
    print(fb)
    print("")
 
def drawboard():
    drawlines()
    drawfigures()
 
def drawlines():
    pygame.draw.line(scn, linecolor, (0, 200), (600, 200), 10)
    pygame.draw.line(scn, linecolor, (0, 400), (600, 400), 10)
    pygame.draw.line(scn, linecolor, (200, 0), (200, 600), 10)
    pygame.draw.line(scn, linecolor, (400, 0), (400, 600), 10)
 
def drawfigures():
    for col in range(C):
        for row in range(R):
            if Board[row][col] == 1:
                pygame.draw.circle(scn, Ocolor, (int(col * sqsize + sqsize / 2), int(row * sqsize + sqsize / 2)), radcir, Owidth)
            elif Board[row][col] == 2:
                pygame.draw.line(scn, Xcolor, (col * sqsize + offset, row * sqsize + offset), (col * sqsize + sqsize - offset, row *sqsize + sqsize - offset), Xwidth)
                pygame.draw.line(scn, Xcolor, (col * sqsize + offset, row * sqsize + sqsize - offset), (col * sqsize + sqsize - offset, row * sqsize + offset), Xwidth)
 
def fullboard():
    for col in range(C):
        for row in range(R):
            if Board[row][col] == 0:
                return False
 
    return True

def availablesquare(row, col):
    return Board[row][col] == 0
 
def marksquare(row, col, player):
    Board[row][col] = player
    
def win(player):
    verwin = vwin(player)
    horwin = hwin(player)
    diagwin = dwin(player)
 
    if verwin or horwin or diagwin:
        return True
    else:
        return False
 
def vwin(player):
    for col in range(C):
        if Board[0][col] == player and Board[1][col] == player and Board[2][col] == player:
            vline(col, player)
            return True
 
    return False
 
def hwin(player):
    for row in range(R):
        if Board[row][0] == player and Board[row][1] == player and Board[row][2] == player:
            hline(row, player)
            return True
 
    return False
 
def dwin(player):
    if Board[0][0] == player and Board[1][1] == player and Board[2][2] == player:
        dline(player)
        return True
    elif Board[2][0] == player and Board[1][1] == player and Board[0][2] == player:
        dline(player, False)
        return True
    else:
        return False
 
def vline(col, player):
    posX = col * sqsize + sqsize / 2
 
    if player == 1:
        pygame.draw.line(scn, Ocolor, (posX, 10), (posX, scnheigth - 10), Owidth)
    else:
        pygame.draw.line(scn,Xcolor, (posX, 10), (posX, scnheigth - 10), Owidth)
 
def hline(row, player):
    posY = row * sqsize + sqsize/ 2
 
    if player == 1:
        pygame.draw.line(scn, Ocolor, (10, posY), (scnwidth - 10, posY), Owidth)
    else:
        pygame.draw.line(scn, Xcolor, (10, posY), (scnwidth - 10, posY), Owidth)
 
def dline(player, down_diag=True):
    if down_diag:
        if player == 1:
            pygame.draw.line(scn, Ocolor, (25, 25), (scnwidth - 25, scnheigth - 25), Xwidth)
        else:
            pygame.draw.line(scn, Ocolor, (25, 25), (scnwidth - 25, scnheigth - 25), Xwidth)
    else:
        if player == 1:
            pygame.draw.line(scn, Ocolor, (25, scnheigth - 25), (scnwidth - 25, 25), Xwidth)
        else:
            pygame.draw.line(scn, Xcolor, (25, scnheigth - 25), (scnwidth - 25, 25), Xwidth)
            
Board = np.zeros((R,C))
pygame.init()
pygame.display.set_caption("TIC TAC TOE GAME by PRANJAL SRIVASTAVA")
scn = pygame.display.set_mode((scnwidth, scnheigth))
scn.fill(bgcolor)
drawlines()
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
            positiony = event.pos[1]
            row = int(math.floor(positiony / sqsize))
            positionx = event.pos[0]
            col = int(math.floor(positionx / sqsize))
 
            if player % 2 == 0:
                if availablesquare(row, col):
                    marksquare(row, col, 1)
 
                    if win(1):
                        gameover = True
                    player += 1
 
            else:
                if availablesquare(row, col):
                    marksquare(row, col, 2)
 
                    if win(2):
                        gameover = True
                    player += 1
 
            if fullboard():
                gameover = True
    drawfigures()
    pygame.display.update()