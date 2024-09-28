import pygame

# Cada tile é quadrado e possui 32 px de lado
TILE_SIZE = 32

# Classe do tilemap que, posteriormente, cada fase irá possuir
class Tilemap:
    def __init__(self):
        # Armazena os tiles em um dicionário em que a chave é o nome do arquivo sem o .png
        self.tile_dict = {}
        self.tile_dict["stone1"] = pygame.image.load("assets/tiles/stone1.png")

        # Matriz correspondente ao arquivo de texto do tilemap
        self.matrix = []

    # Carrega o tilemap e o armazena na matriz a partir da leitura do txt
    def load(self, file):
        with open(file, 'r') as f:
            self.matrix = [list(line.strip()) for line in f.readlines()]

    # Desenha o tilemap na tela
    def draw(self, window):
        tiles = []
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                tile = self.matrix[row][col]

                # Determina a posição de cada tile
                x = col * TILE_SIZE
                y = row * TILE_SIZE
                
                # Checa qual o tile correspondente e determina se haverá colisão ou não com ele
                if tile == '0':
                    window.blit(self.tile_dict["stone1"], (x, y))
        # Tiles que devem ser considerados para colisão
        return tiles
