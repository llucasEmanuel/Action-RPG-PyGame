# Módulo principal
import pygame
from sys import exit
from player import Player
from enemy import StaticEnemy
from ui import HUD, TitleScreen
from physics import Physics
from levels import Tilemap
import collisions

# Inicialização da lib
pygame.init()

# Constantes que armazenam informações da janela
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Action RPG Game"

# Criação da janela
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# Clock para controlar o FPS
clk = pygame.time.Clock()
FPS = 35

# Inicializa o mixer
pygame.mixer.init()

# Variáveis auxiliares
goto_tittle = True

# Inicialização dos objetos principais
player = Player()
enemy = StaticEnemy()
hud = HUD()
tittle_screen = TitleScreen()
physics = Physics(player)
tilemap = Tilemap()

# Carrega o tilemap
tilemap.load("assets/tilemaps/tilemap.txt")

# Loop principal que roda o jogo
while True:
    # Seta o FPS do jogo
    clk.tick(FPS)
    
    # Checa os eventos ocorridos
    for event in pygame.event.get():
        # Se o evento for um clique no X da janela, fecha o jogo
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Checa se houve clique no mouse
        if event.type == pygame.MOUSEBUTTONDOWN and goto_tittle:
            # Detecta o clique do mouse no botão de play da tela de início
            if tittle_screen.rec_btn.collidepoint(pygame.mouse.get_pos()):
                tittle_screen.stop_song()
                goto_tittle = False
            
        # Checa se apertou alguma tecla
        if event.type == pygame.KEYDOWN:
            # # [SPACE] = pula
            # if event.key == pygame.K_SPACE:k
            #     player.set_jump()
            # # [D] = anda para a direita
            # if event.key == pygame.K_d:
            #     player.going_right = True
            #     player.last_key = 'd'  # Atualiza a última tecla pressionada
            # # [A] = anda para a esquerda
            # if event.key == pygame.K_a:
            #     player.going_left = True
            #     player.last_key = 'a'  # Atualiza a última tecla pressionada
            # [K] = ataca (usa uma espada de início)
            if event.key == pygame.K_k and not player.attacking and not player.is_dead:
                player.attacking = True
                player.attack_count = 10

        # # Detecta as teclas que foram soltas
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_d:
        #         player.going_right = False
        #         # Verifica se a tecla A ainda está pressionada para ajustar a direção
        #         if pygame.key.get_pressed()[pygame.K_a]:
        #             player.last_key = 'a'
        #     if event.key == pygame.K_a:
        #         player.going_left = False
        #         # Verifica se a tecla D ainda está pressionada para ajustar a direção
        #         if pygame.key.get_pressed()[pygame.K_d]:
        #             player.last_key = 'd'

    # Se a flag de ir para a tela de título for ativada
    if goto_tittle:
        # Gera a tela de título
        tittle_screen.draw(window)
        tittle_screen.play_song()
        if tittle_screen.rec_btn.collidepoint(pygame.mouse.get_pos()):
            tittle_screen.color_btn = (0, 30, 20)
        else:
            tittle_screen.color_btn = (0, 50, 43)
        # Não executa as outras operações, poisa são desnecessárias nesse estado
        continue

    # Desenha o tilemap e retorna uma lista de plataformas em que há colisão
    platforms = tilemap.draw(window)

    # Desenha inimigo
    enemy.update(window)

    # AINDA É PRECISO RESETAR O STATUS DO INIMIGO QUANDO O PLAYER MORRE (adicionar flag de game over?)
    # Se o jogador morrer, volta para a tela de titulo
    if player.is_dead:
        goto_tittle = True
    # Atualiza o estado do jogador (movimento, pulo, etc.)
    player.update(window, enemy)

    # Checa se houve colisão entre jogador e inimigo
    collisions.handle_player_enemy_collision(player, enemy)

    # Checa se houve colisão da espada do jogador com o inimigo
    collisions.handle_player_attack_collision(player, enemy)

    # Desenha a HUD
    hud.draw(window, player)

    # Atualiza a janela
    pygame.display.update()
