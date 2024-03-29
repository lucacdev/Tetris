from settings import *
import random

class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        self.tetromino = tetromino
        self.pos = vec(pos) + INIT_POS_OFFSET

        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill('blue')

        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos * TILE_SIZE

class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.blocks = [Block(self, pos) for pos in TETROMINOES[self.shape]]

    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction]
        for block in self.blocks:
            block.pos += move_direction

    def update(self):
        self.move(direction='down')