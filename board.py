from square import Square
import pygame as p
from constants import *
import time
import random


class Board:
    def __init__(self, win, length, height, draw, settings):
        self.win = win
        self.length = length
        self.height = height
        self.board = [[Square(i, j) for i in range(self.length)] for j in range(self.height)]
        self.screen_pos = (0, 0)
        self.animation_speed = 0.01
        self.draw = draw
        self.settings = settings
        self.start = (0, 0)
        self.goal = (length - 1, height - 1)

    def update_event(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                quit()

            if event.type == p.MOUSEBUTTONDOWN:
                return event

    def set_visited(self, value):
        for row in self.board:
            for square in row:
                square.visited = value

    def set_value(self, value):
        for row in self.board:
            for square in row:
                square.value = value

    def reset_walls(self):
        for row in self.board:
            for square in row:
                square.wall_up = True
                square.wall_down = True
                square.wall_left = True
                square.wall_right = True

    def fill_path(self, path):
        if path is None:
            return

        for pos in path:
            if self.board[pos[1]][pos[0]].value == EMPTY:
                self.board[pos[1]][pos[0]].value = PATH
                if self.settings.animate:
                    self.update_event()
                    self.draw.update_screen_pos()
                    self.draw.draw_board(self.board, "normal", -1, -1)
                    p.display.update()
                    time.sleep(self.settings.animation_speed)

    def get_neighbors(self, x, y):
        neighbors = []
        if x > 0: # Left
            neighbors.append((x - 1, y))
        if x < self.length - 1: # Right
            neighbors.append((x + 1, y))
        if y > 0: # Up
            neighbors.append((x, y - 1))
        if y < self.height - 1: # Down
            neighbors.append((x, y + 1))

        return neighbors

    def remove_wall(self, x, y, next_x, next_y):
        if x + 1 == next_x: # RIGHT
            self.board[y][x].wall_right = False
            self.board[y][next_x].wall_left = False
        if next_x + 1 == x: # Left
            self.board[y][x].wall_left = False
            self.board[y][next_x].wall_right = False
        if y + 1 == next_y: # Down
            self.board[y][x].wall_down = False
            self.board[next_y][x].wall_up = False
        if next_y + 1 == y: # Up
            self.board[y][x].wall_up = False
            self.board[next_y][x].wall_down = False

    def animate_generation(self, x, y, speed_mult=1):
        self.update_event()
        time.sleep(self.settings.animation_speed * speed_mult)
        self.draw.update_screen_pos()
        self.draw.draw_board(self.board, "generate_maze", x, y)
        p.display.update()

    def recursive_backtracker(self, x, y):
        self.board[y][x].visited = True
        if self.settings.animate:
            self.animate_generation(x, y)
        neighbors = self.get_neighbors(x, y)
        self.board[y][x].visited = True
        while len(neighbors) > 0:
            index = random.randint(0, len(neighbors) - 1)
            next_cell = neighbors.pop(index)
            if self.board[next_cell[1]][next_cell[0]].visited == False:
                self.remove_wall(x, y, next_cell[0], next_cell[1])
                self.recursive_backtracker(next_cell[0], next_cell[1])
            if self.settings.animate:
                self.animate_generation(x, y, 0.1)

    def update_start_goal(self):
        self.board[self.start[1]][self.start[0]].value = START
        self.board[self.goal[1]][self.goal[0]].value = GOAL

    def generate_maze(self):
        self.set_visited(False)
        self.set_value(EMPTY)
        self.reset_walls()
        self.update_start_goal()
        start_x = 0
        start_y = 0
        self.recursive_backtracker(start_x, start_y)
        #return self.board
