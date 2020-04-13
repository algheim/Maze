import pygame as p
from board import Board
from settings import Settings
from path import Path
from draw import Draw
from constants import *

p.init()
clock = p.time.Clock()
win = p.display.set_mode((WIDTH, HEIGHT))
draw = Draw(win)
settings = Settings(win)
board = Board(win, 25, 25, draw, settings)
path = Path(board, settings, draw)


def change_settings(settings, board, button_pressed):
    if button_pressed is None:
        return

    if button_pressed == settings.maze_button:
        board.generate_maze()
    if button_pressed == settings.path_button:
        new_path = path.find_path()
        board.fill_path(new_path)
    if button_pressed == settings.animate_button:
        settings.change_animate()


def main():
    while True:
        event = board.update_event()
        draw.update_screen_pos()
        button_pressed = settings.get_button_pressed(event)
        change_settings(settings, board, button_pressed)
        draw.draw_board(board.board, "normal", -1, -1)
        draw.draw_settings(settings)
        p.display.update()
        clock.tick(60)


main()
