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

    def draw(self, win, screen_x, screen_y, generate_mode, x, y):
        tile_length = int((win.get_size()[0]) / ZOOM)
        draw_x = (self.x * tile_length) - screen_x
        draw_y = (self.y * tile_length) - screen_y
        if generate_mode:
            if self.visited:
                if (self.x == x and self.y == y):
                    p.draw.rect(win, GREEN, (draw_x, draw_y, tile_length, tile_length))
                else:
                    p.draw.rect(win, YELLOW, (draw_x, draw_y, tile_length, tile_length))
            else:
                p.draw.rect(win, WHITE, (draw_x, draw_y, tile_length, tile_length))
        else:
            # Main part
            if self.value == EMPTY:
                p.draw.rect(win, WHITE, (draw_x, draw_y, tile_length, tile_length))

        # Walls
        if self.wall_up:
            p.draw.line(win, BLACK, (draw_x, draw_y), (draw_x + tile_length, draw_y), 2)
        if self.wall_down:
            p.draw.line(win, BLACK, (draw_x, draw_y + tile_length), (draw_x + tile_length, draw_y + tile_length), 2)
        if self.wall_right:
            p.draw.line(win, BLACK, (draw_x + tile_length, draw_y), (draw_x + tile_length, draw_y + tile_length), 2)
        if self.wall_left:
            p.draw.line(win, BLACK, (draw_x, draw_y), (draw_x, draw_y + tile_length), 2)
