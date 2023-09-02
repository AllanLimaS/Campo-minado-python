import pygame

class Block:
    def __init__(self, x, y, blockSize):
        self.x = x
        self.y = y
        self.blockSize = blockSize
        self.bomb = False
        self.clicked = False
        self.flag = False
        self.image = pygame.image.load("Assets/normal.png")
        self.image = pygame.transform.scale(self.image,(self.blockSize,self.blockSize))


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

        
            
            
