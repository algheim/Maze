import pygame as p
from board import Board
from constants import *

p.init()
clock = p.time.Clock()

win = p.display.set_mode((WIDTH, HEIGHT))
board = Board(10, 10)


def update_event():
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            quit()

        if event.type == p.MOUSEBUTTONDOWN:
            return event


def main():
    board.set_temp_values()

    while True:
        event = update_event()
        board.update_screen_pos()
        
        win.fill(GREY)
        board.draw(win)
        p.display.update()

        clock.tick(60)


main()
