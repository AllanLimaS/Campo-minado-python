from block import Block
from effects import *

import sys
import pygame
import random

class Game:
    def __init__(self, screen, dificuldade):
        self.screen = screen

        self.dificuldade = dificuldade
        if dificuldade == 'Fácil':
            self.blockSize = 50
            self.bombLimit = 10
        elif dificuldade == 'Médio':
            self.blockSize = 50
            self.bombLimit = 16
        else:
            self.blockSize = 50
            self.bombLimit = 25

        self.uiSize = 100
        self.campoSize = screen.get_width() // self.blockSize , (screen.get_height() - self.uiSize) // self.blockSize 

        self.vidas = 3
        self.mapafeito = False
        self.bombasColocadas = False
        self.fps = 60
        self.timer = pygame.time.Clock()
        
        self.campo = self.createCampo()

    def createCampo(self):
        campo = []

        # Crie a estrutura do campo da mesma maneira que você fez anteriormente
        for x in range(self.campoSize[0]):
            coluna = []
            for y in range(self.campoSize[1]):
                coluna.append(None)
            campo.append(coluna)

        return campo     
                
            
    def drawMap(self):
        for x in range(self.campoSize[0]):
            self.campo.append([])
            for y in range(self.campoSize[1]):
                # Cria o elemento block
                block = Block(x,y,self.blockSize)
                # printa na tela 
                
                self.screen.blit(block.image, (x* self.blockSize, (y* self.blockSize + self.uiSize)))
                # Adicionao o block a lista
                self.campo[x][y] = block    
            
    def handleClick(self,mousePos,mouseButton):
    
        x, y = mousePos

        # interface do jogo apenas 
        if( y <= self.uiSize):
            return None
        y = y - self.uiSize

        # Calcule o índice do bloco com base na posição do mouse e nas dimensões dos blocos
        index = x // self.blockSize, y // self.blockSize

        # Verifique se o índice está dentro dos limites do campo
        if 0 <= index[0] < self.campoSize[0] and 0 <= index[1] < self.campoSize[1]:
            if mouseButton == "left":
                self.clickBlock(index)
            elif mouseButton == "right":
                self.flagBlock(index)
        else:
            return None
    
    
    def clickBlock(self,index):

        if (self.bombasColocadas == False):
            self.setSafezone(index)
            self.placeBombs()  
            self.bombasColocadas = True
            

        block = self.campo[index[0]][index[1]]
        clickReturn = block.click()
        
        if (clickReturn == "bomb"):
            self.vidas -= 1
        elif (clickReturn == "safe"):
            # botar isso aqui em baixo em uma variavel 
            if self.checkVizinhos(block) == "safeBlock":
                # caso o bloco selecionado nao possuir bombas em volta,
                # inicia a reação em cadeia para abrir os blocos em volta
                for x in range(block.x - 1, block.x + 2):
                    for y in range(block.y - 1, block.y + 2):
                        if 0 <= x < self.campoSize[0] and 0 <= y < self.campoSize[1]:
                            index = x , y
                            self.clickBlock(index)

        self.screen.blit(block.image, (block.x* self.blockSize, (block.y* self.blockSize)+self.uiSize))
    
    def flagBlock(self,index):
        block = self.campo[index[0]][index[1]]
        block.setFlag()
        self.screen.blit(block.image, (block.x* self.blockSize, (block.y* self.blockSize)+self.uiSize))
        
    def setSafezone(self,index):
        for x in range(index[0] - 1, index[0] + 2):
            for y in range(index[1] - 1, index[1] + 2):
                if 0 <= x < self.campoSize[0] and 0 <= y < self.campoSize[1]:
                    block = self.campo[x][y]
                    block.setSafe()
    
    def placeBombs(self):
    
        for bomb in range(self.bombLimit):
            
            ok = False
            while(ok == False):
                
                # Gera um valor aleatório de x e y dentro dos limites do campo
                x = random.randint(0, self.campoSize[0] - 1)  
                y = random.randint(0, self.campoSize[1] - 1) 
                
                block = self.campo[x][y]
                
                # Só é possivel colocar uma bomba aonde não for safezone
                # e também onde não tem bomba
                if (block.safe == False and block.bomb == False):
                    block.setBomb()
                    ok = True
    
    def checkVizinhos(self,block):
        bombsCount = 0

        for x in range(block.x - 1, block.x + 2):
            for y in range(block.y - 1, block.y + 2):
                if 0 <= x < self.campoSize[0] and 0 <= y < self.campoSize[1]:
                    vizinho = self.campo[x][y]
                    if vizinho.bomb:
                        bombsCount += 1        
        block.setImage(bombsCount)
        if bombsCount == 0:
            return "safeBlock"
        else:  
            return "nomalBlock"
    
    def checkWin(self):
        win = True 
        for x in range(self.campoSize[0]):
            for y in range(self.campoSize[1]):
                block = self.campo[x][y]
                blockStatus =  block.getStatus()
                if blockStatus == "notOk":
                    win = False
                    
        if win == True:
            return True
    
    def run(self):
        running = True
        while running:

            self.timer.tick(self.fps)

            update_display(self.screen,self.dificuldade,self.vidas)

            if(self.vidas<=0):
                fade_out_derrota(self.screen,1000,self.dificuldade)
                running = False


            if(self.mapafeito == False):
                self.drawMap()
                self.mapafeito = True

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    if event.button == 1:
                        self.handleClick(mousePos,"left")

                    elif event.button == 3:
                        self.handleClick(mousePos,"right")

                    if self.checkWin():
                        fade_out_vitoria(self.screen,1000,self.dificuldade)
                        if self.dificuldade == 'Fácil':
                            game = Game(self.screen,'Médio')
                            game.run()
                        elif self.dificuldade == 'Médio':
                            game = Game(self.screen,'Difícil')
                            game.run()
                        running = False
                        

                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

            pygame.display.update()
