from block import Block
from game import Game
import pygame

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Campo minado - Allan Lima")
while True:

    game = Game(screen)
    game.run()
    