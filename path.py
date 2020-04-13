import random
from constants import *
import time
import pygame as p


class Path:
    def __init__(self, board, settings, draw):
        self.board = board
        self.settings = settings
        self.draw = draw

    def get_start(self):
        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[0])):
                if self.board.board[i][j].value == START:
                    return (j, i)

    def get_available_neighbors(self, x, y):
        board = self.board.board
        neighbors = []
        if x > 0: # Left
            if not (board[y][x].wall_left or board[y][x - 1].wall_right):
                neighbors.append((x - 1, y))
        if x < len(board[0]) - 1: # Right
            if not (board[y][x].wall_right or board[y][x + 1].wall_left):
                neighbors.append((x + 1, y))
        if y > 0: # Up
            if not (board[y][x].wall_up or board[y - 1][x].wall_down):
                neighbors.append((x, y - 1))
        if y < len(board) - 1: # Down
            if not (board[y][x].wall_down or board[y + 1][x].wall_up):
                neighbors.append((x, y + 1))

        return neighbors

    def test(self, x, y, length):
        board = self.board.board
        board[y][x].visited = True
        if self.settings.animate:
            self.board.animate_generation(x, y)

        if board[y][x].value == GOAL:
            return length, [(x, y)]

        best_path = []
        neighbors = self.get_available_neighbors(x, y)
        best_length = 1000000
        while len(neighbors) > 0:
            index = random.randint(0, len(neighbors) - 1)
            next_x, next_y = neighbors.pop(index)
            if board[next_y][next_x].visited == False:
                test_length, path = self.test(next_x, next_y, length + 1)
                if test_length < best_length:
                    best_length = test_length
                    best_path = path
        if self.settings.animate:
            self.board.animate_generation(x, y, 0.5)

        return best_length, [(x, y)] + best_path

    def find_path(self):
        start = self.get_start()
        if start is None:
            return

        self.board.set_visited(False)
        length, path = self.test(start[0], start[1], 0)
        return path
