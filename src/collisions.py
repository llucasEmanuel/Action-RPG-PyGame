# Responsável por tratar as colisões entre objetos
import pygame
    
def handle_player_attack_collision(player, enemy):
    if not enemy.is_dead and player.attacking and player.sword_rec.colliderect(enemy.rec):
        print("Jogador acertou inimigo")
        if not enemy.is_invincible:
            print("Inimigo vulnerável")
            enemy.take_damage(damage=5)
            if enemy.is_dead:
                print("Inimigo morreu")
                player.pts += 10

def handle_player_enemy_collision(player, enemy):
    if not player.is_dead and not enemy.is_dead and player.rec.colliderect(enemy.rec):
        print("Inimigo acertou o jogador")
        if not player.is_invincible:
            print("Jogador vulnerável")
            player.take_damage(damage=5)
            if player.is_dead:
                print("Jogador morreu")
