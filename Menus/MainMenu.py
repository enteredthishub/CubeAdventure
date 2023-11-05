import pygame
import socket

from CubeAdventure import CubeAdventure
from Menus.Menu import Menu
from Menus.MenuItems.Button import Button
from Menus.MenuMultiplayer import MenuMultiplayer

pygame.init()


class MainMenu(Menu):
    def quit_game(self):
        pygame.quit()


    def create_client(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("93.182.6.25", 45001))
        s.sendall(b"hello")
        # connect to server
        # send data

    def start_single_game(self):
        cubeAdventure = CubeAdventure()
        cubeAdventure.start_game()

    def open_multiplayer_menu(self):
        menumultiplayer = MenuMultiplayer()
        menumultiplayer.draw_menu()

    def get_menu_items_list(self):
        menu_items_list = [Button('Single player', 265, 200, 270, self.start_single_game),
                        Button('Multiplayer', 265, 300, 270, self.open_multiplayer_menu),
                        Button('Quit', 265, 400, 270, self.quit_game)]
        return menu_items_list

mainMenu = MainMenu()
mainMenu.draw_menu()
