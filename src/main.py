# main.py
import pygame
from sys import exit
from player import Player

# Inicialização da lib
pygame.init()

# Constantes que armazenam informações da janela
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Action RPG Game"

# Criação da janela
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# Clock para controlar o FPS
clk = pygame.time.Clock()
FPS = 60

# Inicialização do jogador
player = Player()

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
        
        # Checa se apertou alguma tecla
        if event.type == pygame.KEYDOWN:
            # [SPACE] = pula
            if event.key == pygame.K_SPACE:
                player.start_jump()
            # [D] = anda para a direita
            if event.key == pygame.K_d:
                player.going_right = True
                player.last_key = 'd'  # Atualiza a última tecla pressionada
            # [A] = anda para a esquerda
            if event.key == pygame.K_a:
                player.going_left = True
                player.last_key = 'a'  # Atualiza a última tecla pressionada

        # Detecta as teclas que foram soltas
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.going_right = False
                # Verifica se a tecla A ainda está pressionada para ajustar a direção
                if pygame.key.get_pressed()[pygame.K_a]:
                    player.last_key = 'a'
            if event.key == pygame.K_a:
                player.going_left = False
                # Verifica se a tecla D ainda está pressionada para ajustar a direção
                if pygame.key.get_pressed()[pygame.K_d]:
                    player.last_key = 'd'

    # Limpa o fundo da tela
    window.fill((86, 106, 153))

    # Desenha a linha do chão (use isto temporariamente)
    pygame.draw.line(window, (0, 0, 0), (0, 400 + player.rec.height), (800, 400 + player.rec.height))

    # Atualiza o estado do jogador (movimento, pulo, etc.)
    player.update(window)

    # Atualiza a janela
    pygame.display.update()
