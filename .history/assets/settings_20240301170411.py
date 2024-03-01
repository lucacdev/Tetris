import pygame as pg

vec = pg.math.Vector2

FPS = 60
FIELD_COLOUR = (48, 39, 32)

# SPRITE_DIR_PATH = 'assets/sprites'

ANIM_TIME_INTERVAL = 150 # ms
FAST_ANIM_TIME_INTERVAL = 15 # ms

TILE_SIZE = 35
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)
MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)}

TETROMINOES = {
    'O' : [(0, 0), (0, -1), (1, 0), (1, -1)],
    'I' : [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S' : [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z' : [(0, 0), (1, 0), (0, -1), (-1, -1)],
    'L' : [(0, 0), (1, 0), (0, -1), (0, -2)],
    'J' : [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'T' : [(0, 0), (-1, 0), (1, 0), (0, -1)]
}

TETROMINOES_COLOURS = {
    'O' : (255, 255, 0),
    'I' : (0, 255, 255),
    'S' : (0, 255, 0),
    'Z' : (255, 0, 255),
    'L' : (255, 165, 0),
    'J' : (0, 0, 255),
    'T' : (255, 0, 0)
}