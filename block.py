import pygame

class Block:
    def __init__(self, x, y, blockSize):
        
        # Coordenadas do bloco
        self.x = x
        self.y = y
        
        self.blockSize = blockSize # propriedade para o tamanho do bloco na tela 
        self.bomb = False # flag para saber se tem bomba
        self.clicked = False # flag para saber se foi clicado
        self.flag = False # flag para saber se foi colocada uma flag
        
        # Após o primeiro click do jogador, uma area de 3x3 em torno do click 
        # vira uma safezone, onde nao é possivel ter bomba, para facilitar o 
        # inicio do game
        self.safe = False 
        
        
        self.image = pygame.image.load("Assets/normal.png")
        self.image = pygame.transform.scale(self.image,(self.blockSize,self.blockSize))

    def setSafe(self):
        self.safe = True

    def setBomb(self):
        self.bomb = True

    def click(self):
        if self.clicked == False:
            self.clicked = True
            if self.bomb == True:
                self.image = pygame.image.load("Assets/bomb.png")
                self.image = pygame.transform.scale(self.image,(self.blockSize,self.blockSize))
                return "bomb"
            else:
                self.image = pygame.image.load("Assets/clicked.png")
                self.image = pygame.transform.scale(self.image,(self.blockSize,self.blockSize))
                return "safe"

    def setImage(self,bombsCount):
        match bombsCount:
            case 1:
                self.image = pygame.image.load("Assets/1.png")
            case 2:
                self.image = pygame.image.load("Assets/2.png")
            case 3:
                self.image = pygame.image.load("Assets/3.png")

        self.image = pygame.transform.scale(self.image,(self.blockSize,self.blockSize))
        
    def setFlag(self):
        if self.clicked == False:
            self.flag = not self.flag
            if self.flag: 
                self.image = pygame.image.load("Assets/flag.png")
            else:
                self.image = pygame.image.load("Assets/normal.png")
            self.image = pygame.transform.scale(self.image,(self.blockSize,self.blockSize))


    # Verificação para vitória 
    def getStatus(self):
        
        # Caso não houver bomba, e o bloco estiver clicado
        if (self.bomb == False and self.clicked == True):
            return "ok"
        
        # Caso houver bomba e o bloco estiver com flag
        elif (self.bomb == True and self.flag == True):
            return "ok"
        
        # Caso houver bomba e usuario tiver perdido vida
        elif (self.bomb == True and self.clicked == True ):
            return "ok"
        
        else:  
            return "notOk"
            
            
