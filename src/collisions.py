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
    if player.is_invincible and not player.is_dead:
        # Se colidiu com a metade direita do inimigo, então vai para a direita
        if player.rec.x > enemy.rec.x:
            player.rec.x += 3
        # Caso contrário vai para a esquerda
        else:
            player.rec.x -= 3

        player.damage_timeout -= 1
        if player.damage_timeout <= 0:
            player.is_invincible = False

    if not player.is_dead and not enemy.is_dead and player.rec.colliderect(enemy.rec):
        print("Inimigo acertou o jogador")
        if not player.is_invincible:
            print("Jogador vulnerável")
            player.take_damage(damage=5)
            if player.is_dead:
                print("Jogador morreu")
