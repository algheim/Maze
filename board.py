from square import Square
import pygame as p
from constants import *
from maze import Maze
import time
import random

class Board:
    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.board = [[Square(i, j) for i in range(self.length)] for j in range(self.height)]
        self.screen_pos = (0, 0)
        self.animate = True
        self.animation_speed = 0.05
        #self.maze = Maze(length, height)
        #self.board = self.maze.generate_maze()

    def update_event(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                quit()

            if event.type == p.MOUSEBUTTONDOWN:
                return event

    def draw(self, win, generate_mode, x, y):
        for i in range(self.height):
            for j in range(self.length):
                self.board[i][j].draw(win, self.screen_pos[0], self.screen_pos[1], generate_mode, x, y)

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

    def get_neighbors(self, x, y):
        neighbors = []
        if x > 0 and self.board[y][x - 1].visited == False: # Left
            neighbors.append((x - 1, y))
        if x < self.length - 1 and self.board[y][x + 1].visited == False: # Right
            neighbors.append((x + 1, y))
        if y > 0 and self.board[y - 1][x].visited == False: # Up
            neighbors.append((x, y - 1))
        if y < self.height - 1 and self.board[y + 1][x].visited == False: # Down
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

    def animate_generation(self, win, x, y, speed_mult):
        self.update_event()
        time.sleep(self.animation_speed * speed_mult)
        win.fill(GREY)
        self.update_screen_pos()
        self.draw(win, True, x, y)
        p.display.update()

    def recursive_backtracker(self, x, y, win):
        self.board[y][x].visited = True
        if self.animate:
            self.animate_generation(win, x, y, 1)
        neighbors = self.get_neighbors(x, y)
        self.board[y][x].visited = True
        while len(neighbors) > 0:
            index = random.randint(0, len(neighbors) - 1)
            next_cell = neighbors.pop(index)
            if self.board[next_cell[1]][next_cell[0]].visited == False:
                self.recursive_backtracker(next_cell[0], next_cell[1], win)
                self.remove_wall(x, y, next_cell[0], next_cell[1])
            if self.animate:
                self.animate_generation(win, x, y, 0.5)

    def generate_maze(self, win):
        start_x = 0
        start_y = 0
        self.recursive_backtracker(start_x, start_y, win)
        return self.board
