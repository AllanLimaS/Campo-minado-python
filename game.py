from block import Block
from button import Button
from effects import *

import sys
import pygame
import random

class Game:
    def __init__(self, screen, difficulty, health):
        self.screen = screen

        # Com base na dificuldade do jogo, é definido
        # o tamanho dos blocos e a quantidade de bombas
        self.difficulty = difficulty
        if difficulty == 'Fácil':
            self.blockSize = 50
            self.bombLimit = 10
        elif difficulty == 'Médio':
            self.blockSize = 50
            self.bombLimit = 16
        else:
            self.blockSize = 50
            self.bombLimit = 25

        # Define o tamanho vertical da UI do jogo
        self.uiSize = 100

        # Define o espaço que vai possuir os blocos 
        self.boardSize = (screen.get_width() // self.blockSize ,
                         (screen.get_height() - self.uiSize) // self.blockSize) 

        # define a vida inicial do jogador 
        self.health = health

        # Parametros para criar o campo
        self.boardCreated = False
        self.bombsPlaced = False
        self.fps = 60
        self.timer = pygame.time.Clock()
        
        # definição da matriz do campo
        self.board = self.createBoard()

    # Criação da matriz do campo
    def createBoard(self):
        board = []

        # Crie a estrutura do board da mesma maneira que você fez anteriormente
        for x in range(self.boardSize[0]):
            column = []
            for y in range(self.boardSize[1]):
                column.append(None)
            board.append(column)

        return board     
                
    
    def drawBoard(self):
        for x in range(self.boardSize[0]):
            self.board.append([])
            for y in range(self.boardSize[1]):
                # Cria o elemento block
                block = Block(x,y,self.blockSize)
                # printa na tela 
                self.screen.blit(block.image, (x* self.blockSize, (y* self.blockSize + self.uiSize)))
                # Adicionao o block a matriz
                self.board[x][y] = block    
            

    def handleClick(self,mousePos,mouseButton):
    
        x, y = mousePos

        # interface do jogo apenas 
        if( y <= self.uiSize):
            return None
        y = y - self.uiSize

        # Calcule o índice do bloco com base na posição do mouse e nas dimensões dos blocos
        index = x // self.blockSize, y // self.blockSize

        # Verifique se o índice está dentro dos limites do board
        if 0 <= index[0] < self.boardSize[0] and 0 <= index[1] < self.boardSize[1]:
            if mouseButton == "left":
                self.clickBlock(index)
            elif mouseButton == "right":
                self.flagBlock(index)
        else:
            return None
    
    
    def clickBlock(self,index):

        # caso as bombas ainda não tenham sido posicionadas ainda
        # é definida a area de "spawn" do jogador e colocada  
        # as bombas
        if (self.bombsPlaced == False):
            self.setSafezone(index)
            self.placeBombs()  
            self.bombsPlaced = True
            
        # verifica o bloco no index clicado
        block = self.board[index[0]][index[1]]
        clickStatus = block.click()
        
        if (clickStatus == "bomb"):
            self.health -= 1
        elif (clickStatus == "safe"):
            if self.checkVizinhos(block) == "safeBlock":
                # caso o bloco selecionado nao possuir bombas em volta,
                # inicia a reação em cadeia para abrir os blocos em volta
                for x in range(block.x - 1, block.x + 2):
                    for y in range(block.y - 1, block.y + 2):
                        if 0 <= x < self.boardSize[0] and 0 <= y < self.boardSize[1]:
                            index = x , y
                            self.clickBlock(index)

        # Atualiza na tela a imagem do bloco clicado
        self.screen.blit(block.image, (block.x* self.blockSize, (block.y* self.blockSize)+self.uiSize))
    
    def flagBlock(self,index):
        block = self.board[index[0]][index[1]]
        block.setFlag()
        self.screen.blit(block.image, (block.x* self.blockSize, (block.y* self.blockSize)+self.uiSize))

    # define a zona de proteção do jogador ( "spawn" )    
    def setSafezone(self,index):
        for x in range(index[0] - 1, index[0] + 2):
            for y in range(index[1] - 1, index[1] + 2):
                if 0 <= x < self.boardSize[0] and 0 <= y < self.boardSize[1]:
                    block = self.board[x][y]
                    block.setSafe()
    
    # Posiciona as bombas na matriz 
    def placeBombs(self):
    
        for bomb in range(self.bombLimit):
            
            ok = False
            while(ok == False):
                
                # Gera um valor aleatório de x e y dentro dos limites do board
                x = random.randint(0, self.boardSize[0] - 1)  
                y = random.randint(0, self.boardSize[1] - 1) 
                
                block = self.board[x][y]
                
                # Só é possivel colocar uma bomba aonde não for safezone
                # e também onde não tem bomba
                if (block.safe == False and block.bomb == False):
                    block.setBomb()
                    ok = True
    
    # Funcao para verificar se os blocos proximos ao bloco  
    # central possuem ou nao bombas.
    def checkVizinhos(self,block):
        bombsCount = 0

        for x in range(block.x - 1, block.x + 2):
            for y in range(block.y - 1, block.y + 2):
                if 0 <= x < self.boardSize[0] and 0 <= y < self.boardSize[1]:
                    vizinho = self.board[x][y]
                    if vizinho.bomb:
                        bombsCount += 1        
        block.setImage(bombsCount)
        if bombsCount == 0:
            return "safeBlock"
        else:  
            return "nomalBlock"
    
    # Verifica condição de vitoria, com base nos blocos
    # que foram clicados e adicionados flag 
    def checkWin(self):
        win = True 
        for x in range(self.boardSize[0]):
            for y in range(self.boardSize[1]):
                block = self.board[x][y]
                blockStatus =  block.getStatus()
                if blockStatus == "notOk":
                    win = False
                    
        if win == True:
            return True
    

    def run(self):

        running = True
        while running:

            self.timer.tick(self.fps)

            # Atualiza Saude do jogador e dificuldade do jogo na tela
            updateDisplay(self.screen,self.difficulty,self.health)

            buttonQuit = Button(self.screen, text="Sair",
                                x=self.screen.get_width()-85, y=35,
                                width= 70, height= 35, 
                                center=False)

            # Condição de derrota
            if(self.health<=0):
                fadeOutDefeat(self.screen,1000,self.difficulty)
                running = False

            # Criação inicial do campo
            if(self.boardCreated == False):
                self.drawBoard()
                self.boardCreated = True

            # Verificação de acao do jogador
            for event in pygame.event.get():
                
                # Condicao para pressionar algum botao do mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    
                    # Botao esquerdo pressionado
                    if event.button == 1:
                        self.handleClick(mousePos,"left")
                        
                        # botao de "sair" pressionado
                        if buttonQuit.check_click():
                            fadeOut(self.screen,2000)
                            running = False

                    # Botao direito pressionado
                    elif event.button == 3:
                        self.handleClick(mousePos,"right")

                    # chama verificacao de vitoria apos todo click 
                    if self.checkWin():
                        # caso vitória, cria um novo jogo com dificuldade
                        # maior, mantendo a vida atual do jogador
                        fadeOutWin(self.screen,1000,self.difficulty)
                        if self.difficulty == 'Fácil':
                            game = Game(self.screen,
                                        difficulty='Médio',
                                        health= self.health)
                            game.run()
                        elif self.difficulty == 'Médio':
                            game = Game(self.screen, 
                                        difficulty='Difícil',
                                        health=self.health)
                            game.run()
                        # Caso o jogador tenha terminado a fase "Difícil"
                        # ele ira retornar para o menu 
                        running = False
                        

                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

            pygame.display.update()
