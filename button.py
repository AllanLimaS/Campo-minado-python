import pygame

class Button:
    def __init__(self, screen, text, x, y, width, height):

        # X é centraçizaddo na tela, massa
        # tem que arruamro nome da var widht para width

        self.screen = screen
        self.text = text
        self.x = (screen.get_width() - width) // 2
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.Font('freesansbold.ttf',18)
        self.draw()
        

    def draw(self):
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # Desenhe o botão
        if self.check_click():
            pygame.draw.rect(self.screen, 'dark gray', button_rect, 0, 5)
        else:
            pygame.draw.rect(self.screen, 'light gray', button_rect, 0, 5)

        pygame.draw.rect(self.screen, 'black', button_rect, 2, 5)

        # Calcule a posição do texto para centralizá-lo no botão
        text_surface = self.font.render(self.text, True, 'black')
        text_rect = text_surface.get_rect(center=button_rect.center)

        # Desenhe o texto no centro do botão
        self.screen.blit(text_surface, text_rect)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x,self.y),(self.width,self.height))
        if left_click and button_rect.collidepoint(mouse_pos):
            return True
        else:
            return False