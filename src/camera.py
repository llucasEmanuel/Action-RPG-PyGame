import pygame

class Camera:
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height
        # Câmera vai ter a resolução desse retângulo
        self.camera = pygame.Rect(0, 0, width, height)
    
    def update(self, target):
        # Calcula a posição da câmera em relação ao jogador
        x = int(self.window.get_width()/2) - target.rec.centerx
        y = int(self.window.get_height()/2) - target.rec.bottom

        # Limitar a posição da câmera para não sair do mapa
        x = min(0, x) # Esquerda
        y = min(0, y) # Cima
        x = max(-(self.width - self.window.get_width()), x) # Direita
        y = max(-(self.height - self.window.get_height()), y) # Baixo
        
        self.camera = pygame.Rect(x, y, self.width, self.height)

    def apply(self, entity):
        # Aplica o offset a uma entity
        return entity.rec.move(self.camera.topleft)