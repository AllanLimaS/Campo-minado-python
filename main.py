from game import Game
from button import Button
from effects import *
import pygame 
import sys

pygame.init()

# Define o tamanho da janela 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Define a quantidade de telas esperadas por segundo 
fps = 60
timer = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Campo minado - Allan Lima")

# Preenche a tela de preto
screen.fill((0,0,0))
# Chama a animação de introdução 
intro(screen)
fadeOut(screen,1000)
# Printa o titulo do menu 
menuTitle(screen)

# inicia o looping inicial 
while True:
    timer.tick(fps)

    # Cria os botões do menu inicial

    buttonPlay = Button(screen,text="Jogar",
                        x=10,y=280, 
                        width= 100, height= 50, 
                        center=True)
    
    buttonQuit = Button(screen,text="Sair",
                        x=10,y=350, 
                        width= 100, height= 50, 
                        center=True)

    # Condição para o clique esquerdo do mouse
    if pygame.mouse.get_pressed()[0]:
        
        # Caso o botão de "jogar" tenha sido pressionado, inicia a
        # animação de transição de tela e cria um Game 
        if buttonPlay.check_click():
            
            fadeOut(screen,2000)

            game = Game(screen,
                        difficulty='Fácil',
                        health=3)
            game.run()
            
            screen.fill((0,0,0))
            menuTitle(screen)

        # Condição para o botão de "Sair"
        if buttonQuit.check_click():
            fadeOut(screen,2000)
            pygame.quit()
            sys.exit()

    # Caso o jogador feche a janela ou pressione "esc"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualiza a tela a cada iteração 
    pygame.display.update()

    