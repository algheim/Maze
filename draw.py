from square import Square
import pygame as p
from constants import *

class Draw:
    def __init__(self, win):
        self.screen_pos = (0, 0)
        self.win = win

    def draw_board(self, board, mode, head_x, head_y):
        self.win.fill(GREY)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if mode == "generate_maze":
                    board[i][j].draw_generate_maze(self.win, self.screen_pos[0],
                    self.screen_pos[1], head_x, head_y)
                if mode == "normal":
                    board[i][j].draw_normal(self.win, self.screen_pos[0],
                    self.screen_pos[1])

        p.display.update()

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
