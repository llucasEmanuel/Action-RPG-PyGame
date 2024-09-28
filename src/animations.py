import pygame

SPRITE_WIDTH = 128
SPRITE_HEIGHT = 128

FRAMES_PER_ROW = 7

class Animation:
    # row vai começa a partir de 0
    def __init__(self, spritesheet, row):
        # Lista dos frames da animação
        self.frames = []
        # Extrai uma linha do spritesheet e coloca cada frame numa lista
        for i in range(FRAMES_PER_ROW):
            x = i * SPRITE_WIDTH
            y = row * SPRITE_HEIGHT
            frame = spritesheet.subsurface((x, y, SPRITE_WIDTH, SPRITE_HEIGHT))
            self.frames.append(frame)
        self.curr_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_duration = 100 # Duração de cada frame em ms
    
    def update(self):
        now = pygame.time.get_ticks()

        # Checa se passou o tempo da animação do sprite
        if now - self.last_update > self.frame_duration:
            self.curr_frame = (self.curr_frame + 1) % FRAMES_PER_ROW
            self.last_update = now

    # Quando o jogador não estiver se mexendo, o sprite idle será atribuído
    def set_idle(self):
        self.curr_frame = 0
    
    def draw(self, window, x, y):
        window.blit(self.frames[self.curr_frame], (x, y))

    def get_curr_frame_shape(self):
        w = self.frames[self.curr_frame].get_width()
        h = self.frames[self.curr_frame].get_height()
        return (w, h)
