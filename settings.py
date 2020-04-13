from buttons import Button
import pygame as p
from constants import *


class Settings:
    def __init__(self, win):
        self.win = win
        self.draw_settings = True
        self.animate = True
        self.animation_speed = 0.005
        self.maze_button = None
        self.path_button = None
        self.animate_button = None
        self.buttons = None
        self.button_pressed = None
        self.surface = p.Surface((win.get_size()[0], int(win.get_size()[1] * 0.2)))
        self.surface.set_alpha(230)
        self.surface.fill(BLACK)
        self.init_buttons()

    def init_buttons(self):
        button_length = self.surface.get_size()[0] * 0.21
        button_height = self.surface.get_size()[1] * 0.35
        x_space = self.surface.get_size()[0] * 0.03
        y_space = self.surface.get_size()[1] * 0.05
        text_mult = 0.17

        self.maze_button = Button((button_length * 0 + x_space * 1), y_space,
        button_length, button_height, text="Generate maze")
        self.path_button = Button((button_length * 1 + x_space * 2), y_space,
        button_length, button_height, text="Find path")
        self.animate_button = Button((button_length * 0 + x_space), button_height + y_space * 2,
        button_length, button_height, text="Animate")
        self.buttons = [self.maze_button, self.path_button, self.animate_button]

        for button in self.buttons:
            button.main_color = WHITE
            button.highlight_color = LIGHT_GREY
            button.set_text(text_size=button_length * text_mult)

        self.animate_button.main_color = GREEN
        self.animate_button.highlight_color = DARK_GREEN

    def get_button_pressed(self, event):
        if event is None:
            return

        self.button_pressed = None
        for button in self.buttons:
            if button.check_if_pressed(event.pos[0], event.pos[1]):
                self.button_pressed = button
                return button

    def change_animate(self):
        if self.animate:
            self.animate = False
            self.animate_button.main_color = RED
            self.animate_button.highlight_color = DARK_RED
        else:
            self.animate = True
            self.animate_button.main_color = GREEN
            self.animate_button.highlight_color = DARK_GREEN

    def get_surface(self):
        for button in self.buttons:
            button.update_highlight()
            button.draw(self.surface)

        return self.surface
