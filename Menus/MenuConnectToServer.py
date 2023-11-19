import socket
from threading import Thread

import pygame

from Client import Client
from CubeAdventure import CubeAdventure
from Game import Game
from Menus.MenuItems.Button import Button
from Menus.Menu import Menu
from Menus.MenuItems.InputBox import InputBox
from Menus.MenuItems.TextField import TextField

pygame.init()


class MenuConnectToServer(Menu):
    def __init__(self):
        self.menu_items_list = [TextField('Enter IP address of the server', 180, 100),
                           InputBox(265, 200, 270, 45, "93.182.6.25"),
                           Button('Connect', 265, 300, 270, self.start_game_as_client),
                           Button('Back', 265, 400, 270, self.close_menu)]

    def start_game_as_client(self):
        cubeAdventure = CubeAdventure()
        client = Client()
        cubeAdventure.start_game()

    def get_menu_items_list(self):
        return self.menu_items_list
