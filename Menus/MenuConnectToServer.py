import socket
from threading import Thread

import pygame

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
                           Button('Connect', 265, 300, 270, self.create_client_thread),
                           Button('Back', 265, 400, 270, self.close_menu)]

    def create_client(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("93.182.6.25", 45001))
        data = s.recv(1024)
        print("Current level: " + str(data))
        Game.curr_level = data
        #s.sendall(b"hello")

    def create_client_thread(self):
        thread = Thread(target=self.create_client, args=[])
        thread.start()

    def get_menu_items_list(self):
        return self.menu_items_list
