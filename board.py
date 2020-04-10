from square import Square
import pygame as p
from constants import *

class Board:
    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.board = [[Square() for i in range(self.length)] for j in range(self.height)]
        self.screen_pos = (0, 0)

    def draw(self, win):
        for i in range(self.height):
            for j in range(self.length):
                self.draw_square(win, j, i)

    def draw_square(self, win, x, y):
        x_offset = int(win.get_size()[0] * X_OFFSET)
        tile_length = int((win.get_size()[0] - x_offset) / ZOOM)
        draw_x = (x_offset + x * tile_length) - self.screen_pos[0]
        draw_y = (y * tile_length) - self.screen_pos[1]
        if self.board[y][x].value == EMPTY:
            p.draw.rect(win, WHITE, (draw_x, draw_y, tile_length, tile_length))
        elif self.board[y][x].value == WALL:
            p.draw.rect(win, BLACK, (draw_x, draw_y, tile_length, tile_length))

    def update_screen_pos(self):
        screen_x = self.screen_pos[0]
        screen_y = self.screen_pos[1]
        keys_pressed = p.key.get_pressed()
        if keys_pressed[p.K_d] or keys_pressed[p.K_RIGHT]:
            screen_x += SCREEN_SPEED
        if keys_pressed[p.K_s] or keys_pressed[p.K_DOWN]:
            screen_y += SCREEN_SPEED
        if keys_pressed[p.K_a] or keys_pressed[p.K_LEFT]:
            screen_x -= SCREEN_SPEED
        if keys_pressed[p.K_w] or keys_pressed[p.K_UP]:
            screen_y -= SCREEN_SPEED


        self.screen_pos = (screen_x, screen_y)

    def set_temp_values(self):
        self.board[0][0].value = WALL
        self.board[self.length - 1][self.height - 1].value = WALL
        self.board[7][7].value = WALL
