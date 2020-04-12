from constants import *
import pygame as p


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = EMPTY
        self.visited = False
        self.wall_left = True
        self.wall_right = True
        self.wall_down = True
        self.wall_up = True

    def draw_normal(self, win, screen_x, screen_y):
        tile_length = int((win.get_size()[0]) / ZOOM)
        draw_x = (self.x * tile_length) - screen_x
        draw_y = (self.y * tile_length) - screen_y

        if self.value == EMPTY:
            p.draw.rect(win, WHITE, (draw_x, draw_y, tile_length, tile_length))
        elif self.value == START:
            p.draw.rect(win, GREEN, (draw_x, draw_y, tile_length, tile_length))
        elif self.value == PATH:
            p.draw.rect(win, PURPLE, (draw_x, draw_y, tile_length, tile_length))
        elif self.value == GOAL:
            p.draw.rect(win, RED, (draw_x, draw_y, tile_length, tile_length))

        self.draw_walls(win, screen_x, screen_y)

    def draw_generate_maze(self, win, screen_x, screen_y, head_x, head_y):
        tile_length = int((win.get_size()[0]) / ZOOM)
        draw_x = (self.x * tile_length) - screen_x
        draw_y = (self.y * tile_length) - screen_y

        if self.visited:
            if (self.x == head_x and self.y == head_y):
                p.draw.rect(win, GREEN, (draw_x, draw_y, tile_length, tile_length))
            else:
                p.draw.rect(win, YELLOW, (draw_x, draw_y, tile_length, tile_length))
        else:
            p.draw.rect(win, WHITE, (draw_x, draw_y, tile_length, tile_length))

        self.draw_walls(win, screen_x, screen_y)

    def draw_walls(self, win, screen_x, screen_y):
        tile_length = int((win.get_size()[0]) / ZOOM)
        draw_x = (self.x * tile_length) - screen_x
        draw_y = (self.y * tile_length) - screen_y

        if self.wall_up:
            p.draw.line(win, BLACK, (draw_x, draw_y), (draw_x + tile_length, draw_y), 4)
        if self.wall_down:
            p.draw.line(win, BLACK, (draw_x, draw_y + tile_length), (draw_x + tile_length, draw_y + tile_length), 4)
        if self.wall_right:
            p.draw.line(win, BLACK, (draw_x + tile_length, draw_y), (draw_x + tile_length, draw_y + tile_length), 4)
        if self.wall_left:
            p.draw.line(win, BLACK, (draw_x, draw_y), (draw_x, draw_y + tile_length), 4)
