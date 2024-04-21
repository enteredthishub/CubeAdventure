import pygame

from CubeAdventure import CubeAdventure
from Menus.MenuItems.Button import Button
from Menus.Menu import Menu
from Menus.MenuConnectToServer import MenuConnectToServer
from Server import Server

pygame.init()


class MenuMultiplayer(Menu):

    def __init__(self):
        self.menu_item_list = [Button('Create server', 445, 300, 310, self.start_game_as_server),
                          Button('Connect to server', 445, 400, 310, self.open_connect_to_server_menu),
                          Button('Back', 445, 500, 310, self.close_menu)]


    def start_game_as_server(self):
        cubeAdventure = CubeAdventure()
        server = Server()
        cubeAdventure.start_game()

    def open_connect_to_server_menu(self):
        ConnectToServer = MenuConnectToServer()
        ConnectToServer.draw_menu()



    def get_menu_items_list(self):
        return self.menu_item_list
