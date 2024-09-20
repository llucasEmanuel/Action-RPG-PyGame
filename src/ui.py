# responsável por gerar a UI (HUD, menu, ...)
import pygame

class TitleScreen:
    def __init__(self):
        self.menu_img = pygame.image.load("assets/tittle_screen.jpeg")
        # Ajuste da imagem ao tamanho da janela
        self.menu_img = pygame.transform.scale(self.menu_img, (900, 600))
        self.menu_rec = self.menu_img.get_rect()

        self.tittle_img = pygame.image.load("assets/tittle.png")
        self.tittle_img = pygame.transform.scale(self.tittle_img, (360, 360))

        self.rec_btn = pygame.Rect(375, 420, 165, 100)
        self.color_btn = (0, 50, 43)
        self.font_btn = pygame.font.SysFont("arial", 45)
        self.surface_text_btn = self.font_btn.render("PLAY", False, (255, 255, 255))
        

    def draw(self, window):
        window.fill((0, 0, 0))
        window.blit(self.menu_img, self.menu_rec)
        window.blit(self.tittle_img, (270, -70))
        pygame.draw.rect(window, self.color_btn, self.rec_btn)
        window.blit(self.surface_text_btn, (400, 450))

        pygame.display.update()

class HUD:
    def __init__(self):
        self.font_pts = pygame.font.SysFont("verdana", 35)
    
    def render_pts(self, player):
        text = f'SCORE: {player.pts}'
        text_surface = self.font_pts.render(text, True, (0, 0, 0))
        return text_surface

    def setup_hp_bar(self, player):
        ...

    def draw(self, window, player):
        text_surface = self.render_pts(player)
        window.blit(text_surface, (window.get_width() - 275, 0))