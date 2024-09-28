# Responsável por definir jogador e suas ações
import pygame
from animations import Animation

class Player:
    def __init__(self):
        # Vetor que indica a a direção da velocidade
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = 7

        # Atributos do movimento (andando)
        self.last_key = None  # Indica a última tecla pressionada

        # Atributos do ataque
        self.attacking = False
        self.attack_count = 0 # Tempo em que o ataque ocorre
        self.sword_rec = pygame.Rect(0, 0, 0, 0)

        # Atributos de vida e hit
        self.hp = 20
        # Quando o player tomar dano ele vai ser movido para trás
        self.damage_timeout = 0
        self.is_invincible = False
        self.is_dead = False

        # Pontuação
        self.pts = 0

        # Animação dos sprites
        spritesheet = pygame.image.load("assets/sprites/felicia/spritesheet.png").convert_alpha()
        self.animations = {
            "up": Animation(spritesheet, 8),
            "left": Animation(spritesheet, 9),
            "down": Animation(spritesheet, 10),
            "right": Animation(spritesheet, 11),
        }

        self.state = "idle"
        self.direction = "right"

        # Informações do rec do jogador
        self.width, self.height = self.animations[self.direction].get_curr_frame_shape()
        self.color = (209, 104, 227)
        # Depois mudar as dimensões para melhorar a hitbox
        self.rec = pygame.Rect(210, 300, self.width, self.height)

    # Gerencia a movimentação do jogador
    def move(self):
        # Reseta a velocidade e os boolanos de direção
        self.velocity = pygame.math.Vector2(0, 0)

        # Direção da velocidade
        dv = pygame.math.Vector2(0, 0)

        # Seleciona a direção em que o jogador vai andar
        key = pygame.key.get_pressed()

        # Atualiza o estado jogador
        if key[pygame.K_w] or key[pygame.K_a] or \
           key[pygame.K_s] or key[pygame.K_d]:
            self.state = "moving"
        else:
            self.state = "idle"

        if key[pygame.K_w]:
            dv.y -= 1
            self.last_key = 'w'
            self.direction = "up"

        if key[pygame.K_s]:
            dv.y += 1
            self.last_key = 's'
            self.direction = "down"

        if key[pygame.K_a]:
            dv.x -= 1
            self.last_key = 'a'
            self.direction = "left"

        if key[pygame.K_d]:
            dv.x += 1
            self.last_key = 'd'
            self.direction = "right"

        
        # Checa se existe velocidade em alguma direção, se não a velocidade continua 0, pois foi resetada no início do método
        if dv.length() > 0:
            # Normaliza o vetor dv para conservar o módulo da velocidade em todas as direções
            self.velocity = dv.normalize() * self.speed

        # Atualiza a posição do retângulo
        self.rec.x += self.velocity.x
        self.rec.y += self.velocity.y

    def draw_sword(self, window):
        if self.attacking:
            # Desenha a espada dependendo da posição para onde o jogador anda
            if self.last_key == 'w':
                self.sword_rec = pygame.Rect(self.rec.x + self.rec.width/3 + 2, self.rec.y - 30, 15, 32)
            elif self.last_key == 's':
                self.sword_rec = pygame.Rect(self.rec.x + self.rec.width/3 + 2, self.rec.y + self.rec.height, 15, 32)
            elif self.last_key == 'a':
                self.sword_rec = pygame.Rect(self.rec.x - self.rec.width/3 + 3, self.rec.y + self.rec.height/3, 40, 15)
            # Caso contrário, ataca para a direita
            else:
                self.sword_rec = pygame.Rect(self.rec.x + self.rec.width - 1, self.rec.y + self.rec.height/3, 40, 15)

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
            # Desenha o rec do sprite
            pygame.draw.rect(window, self.color, self.rec, 1)

            if self.state == "moving":
                self.animations[self.direction].update()
            elif self.state == "idle":
                self.animations[self.direction].set_idle()
                
            self.animations[self.direction].draw(window, self.rec.x, self.rec.y)

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

    def update(self, window: pygame.Surface, enemy):
        # Se o jogador morreu, resetar ele
        if self.is_dead:
            self.__init__()
            return
        
        self.draw(window)

        if not self.is_invincible:
            self.move()
            self.attack(window)
        else:
            ...#self.damage_move(enemy)
            

