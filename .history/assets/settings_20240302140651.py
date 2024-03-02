import pygame as pg

vec = pg.math.Vector2

FPS = 60
FIELD_COLOUR = (146, 190, 51)
BG_COLOUR = (37, 72, 50)

# SPRITE_DIR_PATH = 'assets/sprites'

ANIM_TIME_INTERVAL = 150 # ms
FAST_ANIM_TIME_INTERVAL = 15 # ms

TILE_SIZE = 35
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

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
    'O' : (205, 205, 0),
    'I' : (0, 205, 205),
    'S' : (0, 205, 0),
    'Z' : (205, 0, 0),
    'L' : (205, 102, 0),
    'J' : (0, 0, 205),
    'T' : (154, 0, 205)
}