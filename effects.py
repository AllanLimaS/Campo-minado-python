import pygame


# Função para fazer a animacao de fade-out
def fadeOut(screen, fade_duration):
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill((0, 0, 0)) 
    for alpha in range(0, 255):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(fade_duration // 255)

    

# Função para fazer a animacao de derrota
def fadeOutDefeat(screen, fade_duration,difficulty):
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill((255, 0, 0))  
    for alpha in range(0, 255):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(fade_duration // 255)
    
    font = pygame.font.Font(None, 36)
    text = "Você perdeu no - " + difficulty
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(200, 250))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    
    running = True
    tempo_de_pausa = 3000

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Apenas pausa sem renderizar novamente
        pygame.time.delay(tempo_de_pausa)
        screen.fill((0, 0, 0))  
        return

# Função para fazer a animacao de vitoria
def fadeOutWin(screen, fade_duration,difficulty):
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill((255, 255, 255))  
    for alpha in range(0, 255):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(fade_duration // 255)
    
    font = pygame.font.Font(None, 36)
    text = "Você venceu no - " + difficulty
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(200, 250))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    
    running = True
    tempo_de_pausa = 3000

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Apenas pausa sem renderizar novamente
        pygame.time.delay(tempo_de_pausa)
        screen.fill((0, 0, 0))  
        return 


def intro(screen):
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 24)
    text = "Projeto desenvolvido para matéria de\nIntrodução a programação em python\npor: Allan Lima"
    text_lines = text.split('\n')

    text_surfaces = []
    for line in text_lines:
        text_surface = font.render(line, True, (255, 255, 255))
        text_surfaces.append(text_surface)

    # Desenha o texto uma vez antes do atraso
    screen.fill((0, 0, 0))
    y_offset = 250
    for text_surface in text_surfaces:
        text_rect = text_surface.get_rect(center=(200, y_offset))
        screen.blit(text_surface, text_rect)
        y_offset += 24
    pygame.display.flip()

    running = True
    tempo_de_pausa = 3000

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Apenas pausa sem renderizar novamente
        pygame.time.delay(tempo_de_pausa)
        return
    
def menuTitle(screen):
    font = pygame.font.Font(None, 36)
    text = "CAMPO MINADO"
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(200, 250))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()


def updateDisplay(screen,difficulty,health):
    pygame.draw.rect(screen,(255,255,255),(0,0,screen.get_width(),100))

    font = pygame.font.Font(None, 36)
    text = difficulty
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(200, 40))
    screen.blit(text_surface, text_rect)

    # posição do texto
    text = "Saúde"
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.left = 10
    text_rect.top = 10

    # posição da barra de saúde
    barra_x = 10
    barra_y = 40 
    barra_largura = health * 25
    barra_altura = 25

    screen.blit(text_surface, text_rect)

    # Contorno da barra de saúde
    pygame.draw.rect(screen, (0, 0, 0), (barra_x - 2, barra_y - 2, barra_largura + 4, barra_altura + 4))

    # Barra de saúde
    pygame.draw.rect(screen, (255, 0, 0), (barra_x, barra_y, barra_largura, barra_altura))

