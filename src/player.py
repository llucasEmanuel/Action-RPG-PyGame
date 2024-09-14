# Responsável por definir jogador e suas ações
import pygame
from physics import Physics

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
        self.on_floor = True
        self.vy = -10  # Velocidade inicial do pulo
        self.jumping = False

        # Atributos do ataque
        self.attacking = False
        self.attack_count = 0 # tempo em que o ataque ocorre
        self.sword_rec = pygame.Rect(0, 0, 0, 0)

        # Atributos de vida e hit
        self.hp = 20
        # Quando o player tomar dano ele vai ser movido para trás
        self.damage_timeout = 0
        self.is_invincible = False
        self.is_dead = False

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

    def set_jump(self):
        if not self.jumping:
            self.jumping = True
            self.on_floor = False
            self.vy = -10

    def handle_floor_contact(self):
        if not self.on_floor or self.jumping:
            # Checa se atingiu o chão (400 é a posição do chão)
            if self.rec.y >= 400:
                self.rec.y = 400
                self.jumping = False
                self.on_floor = True
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
            self.sword_rec = None

    def attack(self, window):
        # Lógica do ataque
        if self.attacking:
            self.draw_sword(window)
            self.attack_count -= 1
            if self.attack_count <= 0:
                self.attacking = False

    def draw(self, window: pygame.Surface):
        if not self.is_dead:
            pygame.draw.rect(window, self.color, self.rec)

    def take_damage(self, damage):
        if not self.is_invincible:
            self.hp -= damage
            self.damage_timeout = 30
            if self.hp <= 0:
                self.hp = 0
                self.is_dead = True
                self.is_invincible = False
                self.damage_timeout = 0
                self.rec = pygame.Rect(0, 0, 0, 0)
            else:
                # 50 segundos de invencibilidade
                self.is_invincible = True

    def damage_move(self, enemy):
        # Se colidiu com a metade direita do inimigo, então vai para a direita
        if self.rec.x > enemy.rec.x:
            self.rec.x += 3
        # Caso contrário vai para a esquerda
        else:
            self.rec.x -= 3

        self.damage_timeout -= 1
        if self.damage_timeout <= 0:
            self.is_invincible = False

    def update(self, window: pygame.Surface, enemy):
        # Se o jogador morreu, resetar ele
        if self.is_dead:
            self.__init__()
            return

        # Aplica a gravidade no jogador e checa se ele atingiu o chão
        self.handle_floor_contact()
        
        if not self.is_invincible:
            self.move()
            # self.jump()
            self.attack(window)
        else:
            self.damage_move(enemy)

        self.draw(window)
