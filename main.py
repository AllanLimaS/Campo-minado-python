from block import Block

import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
blockSize = 85
bombLimit = 10
campoSize = SCREEN_WIDTH // blockSize , SCREEN_HEIGHT // blockSize

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

run = True

vidas= 3
pontuacao = 0
mapafeito = False
bombasColocadas = False

campo = []
# Primeiro, crie uma lista vazia para cada coluna
for x in range(campoSize[0]):
    coluna = []
    campo.append(coluna)

    # Em seguida, adicione elementos (por exemplo, instâncias da classe Block) a cada coluna
    for y in range(campoSize[1]):
        coluna.append(None)  # Ou qualquer outro valor inicial desejado


def handleClick(mousePos,mouseButton):
    
    global vidas, pontuacao
    
    print("Vidas:", vidas)
    print("Pontuação:", pontuacao)
    
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

def setSafezone(index):
    for x in range(index[0] - 1, index[0] + 2):
        for y in range(index[1] - 1, index[1] + 2):
            if 0 <= x < campoSize[0] and 0 <= y < campoSize[1]:
                block = campo[x][y]
                block.setSafe()


def clickBlock(index):
    global vidas, pontuacao, bombasColocadas

    if bombasColocadas == False:
        setSafezone(index)
        placeBombs()  
        bombasColocadas = True
          

    block = campo[index[0]][index[1]]
    clickReturn = block.click()
    
    if (clickReturn == "bomb"):
        vidas -= 1
    elif (clickReturn == "safe"):
        pontuacao += 1
        # botar isso aqui em baixo em uma variavel 
        if checkVizinhos(block) == "safeBlock":
            # caso o bloco selecionado nao possuir bombas em volta,
            # inicia a reação em cadeia para abrir os blocos em volta
            for x in range(block.x - 1, block.x + 2):
                for y in range(block.y - 1, block.y + 2):
                    if 0 <= x < campoSize[0] and 0 <= y < campoSize[1]:
                        index = x , y
                        clickBlock(index)

    screen.blit(block.image, (block.x* blockSize, block.y* blockSize))



def flagBlock(index):
    block = campo[index[0]][index[1]]
    block.setFlag()
    screen.blit(block.image, (block.x* blockSize, block.y* blockSize))


def placeBombs():
    
    for bomb in range(bombLimit):
        
        ok = False
        while(ok == False):
            
            # Gera um valor aleatório de x e y dentro dos limites do campo
            x = random.randint(0, campoSize[0] - 1)  
            y = random.randint(0, campoSize[1] - 1) 
            
            block = campo[x][y]
            
            # Só é possivel colocar uma bomba aonde não for safezone
            # e também onde não tem bomba
            if (block.safe == False and block.bomb == False):
                block.setBomb()
                ok = True
    

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
    

def checkVizinhos(block):
    bombsCount = 0

    for x in range(block.x - 1, block.x + 2):
        for y in range(block.y - 1, block.y + 2):
            if 0 <= x < campoSize[0] and 0 <= y < campoSize[1]:
                vizinho = campo[x][y]
                if vizinho.bomb:
                    bombsCount += 1        
    block.setImage(bombsCount)
    if bombsCount == 0:
        return "safeBlock"
    else:  
        return "nomalBlock"

def checkWin():
    win = True 
    for x in range(campoSize[0]):
        for y in range(campoSize[1]):
            block = campo[x][y]
            blockStatus =  block.getStatus()
            if blockStatus == "notOk":
                win = False
                
    if win == True:
        print ("ganhou otario!")

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
            checkWin()

        if event.type == pygame.QUIT:

            run = False

    pygame.display.update()
pygame.quit()