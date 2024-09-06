# player.py
import pygame

class Player:
    def __init__(self) -> None:
        # Informações do rec do jogador
        self.width = 50
        self.height = 60
        self.color = (209, 104, 227)
        self.rec = pygame.Rect(400, 400, self.width, self.height)

        # Atributos do movimento horizontal (andando)
        self.going_right = False
        self.going_left = False
        self.last_key = None  # Indica a última tecla pressionada
        self.vx = 8  # Velocidade horizontal

        # Atributos do movimento vertical (pulando)
        self.jumping = False
        self.g = 1.2  # Gravidade
        self.vy = -14  # Velocidade inicial do pulo

    def move(self):
        # Movimentação baseada na última tecla pressionada
        if self.going_right and self.last_key == 'd':
            self.walk_right()
        elif self.going_left and self.last_key == 'a':
            self.walk_left()

    def walk_right(self):
        self.rec.x += self.vx

    def walk_left(self):
        self.rec.x -= self.vx

    def start_jump(self):
        if not self.jumping:
            self.jumping = True
            self.vy = -14

    def draw(self, window: pygame.Surface):
        pygame.draw.rect(window, self.color, self.rec)

    def update(self, window: pygame.Surface):
        self.move()

        # Lógica do pulo
        if self.jumping:
            self.rec.y += self.vy
            self.vy += self.g
            # Checa se atingiu o chão (400 é a posição do chão)
            if self.rec.y >= 400:
                self.rec.y = 400
                self.jumping = False
                self.vy = 0

        self.draw(window)
