import pygame

GRAVITY = 0.7
MAX_FALL_SPEED = 10

class Physics:
    def __init__(self, player, gravity = GRAVITY, max_fall_speed = MAX_FALL_SPEED):
        self.player = player
        self.gravity = gravity
        self.max_fall_speed = max_fall_speed

    def apply_gravity(self):
        # Se o jogador estiver no ar (independente se está pulando ou não)
        if not self.player.on_floor:
            self.player.rec.y += self.player.vy
            self.player.vy += self.gravity
            if self.player.vy > self.max_fall_speed:
                self.player.vy = self.max_fall_speed
