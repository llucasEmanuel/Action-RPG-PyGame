# Responsável por definir os inimigos e suas ações
import pygame

class Enemy:
    def __init__(self, hp:int):
        self.hp = hp
        self.is_dead = False
        self.rec = pygame.Rect(600, 400, 50, 60)
        # Contador que deixa o inimigo invulnerável por um tempo após receber dano
        self.damage_timeout = 0
        # Indica se o inimigo está em estado de invencibilidade
        self.is_invincible = False
    
    def take_damage(self, damage):
        if not self.is_invincible:
            # 1 segundo de invencibilidade
            self.hp -= damage
            if self.hp <= 0:
                self.hp = 0
                self.is_dead = True
                self.is_invincible = False
                self.damage_timeout = 0
                self.rec = pygame.Rect(0, 0, 0, 0)
            else:
                # 50 segundos de invencibilidade
                self.damage_timeout = 50
                self.is_invincible = True

    
    def draw(self, window):
        if not self.is_dead:
            if not self.is_invincible:
                pygame.draw.rect(window, (101, 145, 85), self.rec)
            else:
                pygame.draw.rect(window, (64, 87, 55), self.rec)


    def update(self, window):
        if self.is_invincible and not self.is_dead:
            self.damage_timeout -= 1
            if self.damage_timeout <= 0:
                self.is_invincible = False
        self.draw(window)


class StaticEnemy(Enemy):
    def __init__(self, hp:int=10):
        super().__init__(hp)
