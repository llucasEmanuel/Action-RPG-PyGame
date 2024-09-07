# Responsável por definir jogador e suas ações
import pygame

class Player:
    def __init__(self):
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

        # Atributos do ataque
        self.attacking = False
        self.attack_count = 0 # tempo em que o ataque ocorre
        self.sword_rec = pygame.Rect(0, 0, 0, 0)

        # Pontuação
        self.pts = 0

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
        
    def jump(self):
        # Lógica do pulo
        if self.jumping:
            self.rec.y += self.vy
            self.vy += self.g
            # Checa se atingiu o chão (400 é a posição do chão)
            if self.rec.y >= 400:
                self.rec.y = 400
                self.jumping = False
                self.vy = 0

    def draw_sword(self, window):
        if self.attacking:
            # Se o jogador estiver indo para a esquerda, ataca a esquerda
            if self.last_key == 'a':
                self.sword_rec = pygame.Rect(self.rec.x - self.rec.width + 10, self.rec.y + self.rec.height/3, 40, 15)
            # Caso contrário, independente da última tecla, ataca para a direita
            else:
                self.sword_rec = pygame.Rect(self.rec.x + self.rec.width, self.rec.y + self.rec.height/3, 40, 15)

            pygame.draw.rect(window, (191, 191, 191), self.sword_rec)
        else:
            self.sword_rec = pygame.Rect(0, 0, 0, 0)

    def attack(self, window):
        # Lógica do ataque
        if self.attacking:
            self.draw_sword(window)
            self.attack_count -= 1
            if self.attack_count <= 0:
                self.attacking = False

    def draw(self, window: pygame.Surface):
        pygame.draw.rect(window, self.color, self.rec)

    def update(self, window: pygame.Surface):
        self.move()

        self.jump()

        self.attack(window)

        self.draw(window)
