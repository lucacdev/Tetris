from settings import *

class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        self.tetromino = tetromino

        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill('blue')

        self.rect = self.image.get_rect()
        self.rect.topleft = pos[0] * TILE_SIZE, pos[1] * TILE_SIZE

class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = 'T'
        self.blocks = [Block(self, pos) for pos in TETROMINOES[self.shape]]

    def update(self):
        pass