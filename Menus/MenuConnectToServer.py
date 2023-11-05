import socket

import pygame

from Menus.MenuItems.Button import Button
from Menus.Menu import Menu
from Menus.MenuItems.TextField import TextField

pygame.init()


class MenuConnectToServer(Menu):

    def create_client(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("93.182.6.25", 45001))
        s.sendall(b"hello")

    def get_menu_items_list(self):
        menu_items_list = [TextField('Enter IP address of the server', 180, 100),
                           Button('Connect', 265, 300, 270, self.create_client),
                           Button('Back', 265, 400, 270, self.close_menu)]
        return menu_items_list
