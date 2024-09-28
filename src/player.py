# Responsável por definir jogador e suas ações
import pygame

class Player:
    def __init__(self):
        # Informações do rec do jogador
        self.width = 50
        self.height = 60
        self.color = (209, 104, 227)
        # O jogador é gerado no ar e cai até atingir uma plataforma
        self.rec = pygame.Rect(210, 300, self.width, self.height)

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

        # Carrega os sprites do jogador e os armazena em um dicionário
        self.sprites_dict = {
            "up": {
                "idle": pygame.image.load("assets/sprites/felicia/felicia_up_idle.png"),
            },
            "down": {
                "idle": pygame.image.load("assets/sprites/felicia/felicia_down_idle.png"),
            },
            "left": {
                "idle": pygame.image.load("assets/sprites/felicia/felicia_left_idle.png"),
            },
            "right": {
                "idle": pygame.image.load("assets/sprites/felicia/felicia_right_idle.png"),
            },
        }

        self.state = "idle"
        self.direction = "right"
        self.curr_sprite = self.sprites_dict["right"]["idle"]

    # Gerencia a movimentação do jogador
    def move(self):
        # Reseta a velocidade e os boolanos de direção
        self.velocity = pygame.math.Vector2(0, 0)

        # Direção da velocidade
        dv = pygame.math.Vector2(0, 0)

        # Seleciona a direção em que o jogador vai andar
        key = pygame.key.get_pressed()

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
                self.sword_rec = pygame.Rect(self.rec.x - self.rec.width + 17, self.rec.y + self.rec.height/3, 40, 15)
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
            self.curr_sprite = self.sprites_dict[self.direction][self.state]
            pygame.draw.rect(window, self.color, self.rec, 1)
            self.rec.width = self.curr_sprite.get_width()
            self.rec.height = self.curr_sprite.get_height()
            window.blit(self.curr_sprite, (self.rec.x, self.rec.y))

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
            

