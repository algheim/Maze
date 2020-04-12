import random
from constants import *
import time
import pygame as p


def update_event():
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            quit()

        if event.type == p.MOUSEBUTTONDOWN:
            return event


def set_visited(board, value):
    for row in board:
        for square in row:
            square.visited = value


def get_available_neighbors(board, x, y):
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


def animate(board, x, y, sleep_time, draw):
    update_event()
    draw.update_screen_pos()
    draw.draw_board(board, "generate_maze", x, y)
    time.sleep(sleep_time)


def test(board, x, y, length, draw):
    board[y][x].visited = True
    animate(board, x, y, 0.01, draw)
    if board[y][x].value == GOAL:
        return length, [(x, y)]

    best_path = []
    neighbors = get_available_neighbors(board, x, y)
    best_length = 1000000
    while len(neighbors) > 0:
        index = random.randint(0, len(neighbors) - 1)
        next_x, next_y = neighbors.pop(index)
        if board[next_y][next_x].visited == False:
            test_length, path = test(board, next_x, next_y, length + 0.5, draw)
            if test_length < best_length:
                best_length = test_length
                best_path = path

    animate(board, x, y, 0.1, draw)
    return best_length, [(x, y)] + best_path


def fin_path(board, x, y, draw):
    set_visited(board, False)
    length, path = test(board, x, y, 0, draw)
    return path
