# Arquivo principal em que o jogo será executado
import pygame
from sys import exit
from player import Player

# Incialização da lib
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
            # [d] = anda para a direita
            if event.key == pygame.K_d:
                player.walk_right()
            # [a] = anda para a esquerda
            if event.key == pygame.K_a:
                player.walk_left()
    

    # Checa se os botões de andar estão sendo segurados
    if pygame.key.get_pressed()[pygame.K_a]:
        player.walk_left()
    else:
        player.going_left = False
        
    if pygame.key.get_pressed()[pygame.K_d]:
        player.walk_right()
    else:
        player.going_right = False


    # Limpa o fundo da tela
    window.fill((86, 106, 153))

    # Usar apenas como teste, depois mover para o levels.py
    pygame.draw.line(window, (0, 0, 0), (0, 400+player.rec.height), (800, 400+player.rec.height))

    # Atualiza pulo do jogador
    player.update_jump(window)

    # Desenha o jogador na janela
    player.draw(window)

    # Atualiza a janela        
    pygame.display.update()
