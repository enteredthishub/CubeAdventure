import pygame

from Menus.MenuItems.MenuItem import MenuItem
from Menus.MenuItems.TextField import TextField


class GameInterface:
    red_score_textfield = None
    blue_score_textfield = None
    red_score = 200
    blue_score = 200

    def __init__(self):
        self.red_score_textfield = TextField(str(self.red_score), 500, 50, (255, 0 ,0))
        self.blue_score_textfield = TextField(str(self.blue_score), 650, 50, (0, 0, 255))

    def draw(self, screen):
        self.red_score_textfield.draw(screen)
        self.blue_score_textfield.draw(screen)



