import pygame


# Função para fazer o fade-out
def fade_out(screen, fade_duration):
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill((0, 0, 0))  # Preencha com preto
    for alpha in range(0, 255):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(fade_duration // 255)


def introducao(screen):
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
    
def menu_titulo(screen):
    font = pygame.font.Font(None, 36)
    text = "CAMPO MINADO"
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(200, 250))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

