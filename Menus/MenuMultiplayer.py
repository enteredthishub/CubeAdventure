import pygame
import socket

from Button import Button
from CubeAdventure import CubeAdventure
from Game import Game
from Menus.Menu import Menu

pygame.init()


class MenuMultiplayer(Menu):
    def get_button_list(self):
        buttons_list = [Button('Create server', 265, 200, 270, None),
                        Button('Connect to server', 265, 300, 270, None),
                        Button('Back', 265, 400, 270, None)]
        return buttons_list

