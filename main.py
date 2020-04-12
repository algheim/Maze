import pygame as p
from board import Board
from constants import *
import pathfind
import draw

p.init()
clock = p.time.Clock()
win = p.display.set_mode((WIDTH, HEIGHT))
draw = draw.Draw(win)
board = Board(15, 15, draw)

board.generate_maze(win)
board.board[14][14].value = GOAL
path = pathfind.fin_path(board.board, 0, 0, draw)
board.fill_path(path, 0.1)

def update_event():
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            quit()

        if event.type == p.MOUSEBUTTONDOWN:
            return event


def main():
    while True:
        board.update_event()
        draw.update_screen_pos()
        draw.draw_board(board.board, "normal", -1, -1)
        clock.tick(60)


main()
