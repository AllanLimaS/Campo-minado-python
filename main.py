from block import Block

import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
blockSize = 50
bombLimit = 30
campoSize = SCREEN_WIDTH // blockSize , SCREEN_HEIGHT // blockSize

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

run = True

vidas= 3
pontuacao = 0
mapafeito = False

campo = []
# Primeiro, crie uma lista vazia para cada coluna
for x in range(campoSize[0]):
    coluna = []
    campo.append(coluna)

    # Em seguida, adicione elementos (por exemplo, instâncias da classe Block) a cada coluna
    for y in range(campoSize[1]):
        coluna.append(None)  # Ou qualquer outro valor inicial desejado


def handleClick(mousePos,mouseButton):
    x, y = mousePos
    # Calcule o índice do bloco com base na posição do mouse e nas dimensões dos blocos
    index = x // blockSize, y // blockSize
    # Verifique se o índice está dentro dos limites do campo
    if 0 <= index[0] < campoSize[0] and 0 <= index[1] < campoSize[1]:
        if mouseButton == "left":
            clickBlock(index)
        elif mouseButton == "right":
            flagBlock(index)
    else:
        return None

def clickBlock(index):
    global vidas, pontuacao

    block = campo[index[0]][index[1]]
    clickReturn = block.click()
    
    if (clickReturn == "bomb"):
        vidas -= 1
    elif (clickReturn == "safe"):
        pontuacao += 1
        checkVizinhos(block)

    screen.blit(block.image, (block.x* blockSize, block.y* blockSize))

    print("Vidas:", vidas)
    print("Pontuação:", pontuacao)

def flagBlock(index):
    print("CU")
    block = campo[index[0]][index[1]]
    block.setFlag()
    screen.blit(block.image, (block.x* blockSize, block.y* blockSize))


def placeBombs():
    for bomb in range(bombLimit):
        x = random.randint(0, campoSize[0] - 1)  # Gera um valor aleatório de x dentro dos limites do campo
        y = random.randint(0, campoSize[1] - 1)  # Gera um valor aleatório de y dentro dos limites do campo
        block = campo[x][y]
        block.setBomb()
        print(x,y)


def drawMap():
    for x in range(campoSize[0]):
        campo.append([])
        for y in range(campoSize[1]):
            
            # Cria o elemento block
            block = Block(x,y,blockSize)
            # printa na tela 
            screen.blit(block.image, (x* blockSize, y* blockSize))
            # Adicionao o block a lista
            campo[x][y] = block
    placeBombs()

def checkVizinhos(block):
    bombsCount = 0

    for x in range(block.x - 1, block.x + 2):
        for y in range(block.y - 1, block.y + 2):
            if 0 <= x < campoSize[0] and 0 <= y < campoSize[1]:
                vizinho = campo[x][y]
                if vizinho.bomb:
                    bombsCount += 1
        
    block.setImage(bombsCount)




while run:

    if(mapafeito == False):
       drawMap()
       mapafeito = True

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if event.button == 1:
                handleClick(mousePos,"left")
            elif event.button == 3:
                handleClick(mousePos,"right")

        if event.type == pygame.QUIT:

            run = False

    pygame.display.update()
pygame.quit()