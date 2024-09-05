# responsável por definir o jogador e suas ações
import pygame

class Player:
    def __init__(self) -> None:
        # Informações do rec do jogador
        self.width = 50
        self.height = 60
        self.color = (209, 104, 227)
        self.rec = pygame.Rect(400, 400, self.width, self.height)

        # Atributos do movimento horizontal (andando)
        self.going_right = False # Flag que checa se está andando para direita
        self.going_left = False # O mesmo de cima só que para a esquerda (ajuda a suavizar o movimento horizontal)
        self.vx = 8 # Velocidade

        # Atributos do movimento vertical (pulando)
        self.jumping = False
        self.g = 1.2
        self.vy = -14

    def walk_right(self):
        if not self.going_left: # Dá prioridade ao primeiro movimento
            self.rec.x += self.vx
            self.going_right = True
    def walk_left(self):
        if not self.going_right:
            self.rec.x -= self.vx
            self.going_left = True

    def start_jump(self):
        if not self.jumping:
            self.jumping = True
            self.vy = -14

    def draw(self, window:pygame.Surface):
        pygame.draw.rect(window, self.color, self.rec)
    
    def update_jump(self, window:pygame.Surface):
        if self.jumping:
            self.rec.y += self.vy
            self.vy += self.g
            # Checa se atingiu o chão (chão = 400 no meu jogo)
            if self.rec.y >= 400:
                self.rec.y = 400
                self.jumping = False
                self.vy = 0