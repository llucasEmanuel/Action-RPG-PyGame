# Responsável por tratar as colisões entre objetos
import pygame
from player import Player
from enemy import StaticEnemy

def handle_player_attack_collision(player: Player, enemy: StaticEnemy):
    if player.attacking and player.sword_rec.colliderect(enemy.rec):
        print("Jogador acertou inimigo")
        if not enemy.is_invincible:
            print("Inimigo vulnerável")
            enemy.take_damage(damage=5)
            if enemy.is_dead:
                print("Inimigo morreu")
                player.pts += 10