from game import Game
from button import Button
from effects import *
import pygame 
import sys


pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
fps = 60
timer = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Campo minado - Allan Lima")

screen.fill((0,0,0))
introducao(screen)
fade_out(screen,1000)

menu_titulo(screen)
while True:
    timer.tick(fps)

    botao_jogar = Button(screen,text="Jogar",x=10,y=280, width= 100, height= 50)
    botao_sair = Button(screen,text="Sair",x=10,y=350, width= 100, height= 50)

    if pygame.mouse.get_pressed()[0]:
        print(pygame.mouse.get_pos())
        if botao_jogar.check_click():

            fade_out(screen,2000)
            game = Game(screen)
            game.run()

        if botao_sair.check_click():
            fade_out(screen,2000)
            pygame.quit()
            sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    