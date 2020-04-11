import pygame as p
from board import Board
from constants import *

p.init()
clock = p.time.Clock()
win = p.display.set_mode((WIDTH, HEIGHT))
board = Board(15, 15)
board.generate_maze(win)


def update_event():
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            quit()

        if event.type == p.MOUSEBUTTONDOWN:
            return event


def main():
    while True:
        board.update_screen_pos()

        win.fill(GREY)
        board.update_event()
        board.draw(win, False, 0, 0)
        p.display.update()

        clock.tick(60)


main()
