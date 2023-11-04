import pygame
import socket

from Button import Button
from CubeAdventure import CubeAdventure
from Game import Game
from Menus.Menu import Menu
from Menus.MenuMultiplayer import MenuMultiplayer

pygame.init()


class MainMenu(Menu):
    def quit_game(self):
        pygame.quit()

    def create_server(self):
        # create server
        # listen for connection
        # receive data
        # print data
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("192.168.50.2", 45001))
        s.listen()
        conn, addr = s.accept()
        print("New client from " + addr[0])
        data = conn.recv(1024)
        print("New data from client " + str(data))

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

    def get_button_list(self):
        buttons_list = [Button('Single player', 265, 200, 270, self.start_single_game),
                        Button('Multiplayer', 265, 300, 270, self.open_multiplayer_menu),
                        Button('Quit', 265, 400, 270, self.quit_game)]
        return buttons_list

mainMenu = MainMenu()
mainMenu.draw_menu()
