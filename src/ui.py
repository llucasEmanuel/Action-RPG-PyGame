# responsável por gerar a UI (HUD, menu, ...)
import pygame

class TitleScreen:
    ...

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