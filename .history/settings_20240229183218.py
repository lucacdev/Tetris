import pygame as pg

FPS = 60
FIELD_COLOUR = (48, 39, 32)

TILE_SIZE = 35
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

TETROMINOES = {
    'T' : [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O' : [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J' : [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L' : [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I' : [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S' : [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z' : [(0, 0), (1, 0), (0, -1), (-1, -1)]
}