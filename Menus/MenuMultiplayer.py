import socket
from threading import Thread

import pygame

from CubeAdventure import CubeAdventure
from Game import Game
from Menus.MenuItems.Button import Button
from Menus.Menu import Menu
from Menus.MenuConnectToServer import MenuConnectToServer

pygame.init()


class MenuMultiplayer(Menu):

    def __init__(self):
        self.menu_item_list = [Button('Create server', 245, 200, 310, self.start_game_as_server),
                          Button('Connect to server', 245, 300, 310, self.open_connect_to_server_menu),
                          Button('Back', 245, 400, 310, self.close_menu)]

    def create_server(self):
        # create server
        # listen for connection
        # receive data
        # print data
        print("Starting Server")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("192.168.50.2", 45001))
        s.listen()
        conn, addr = s.accept()
        print("New client from " + addr[0])
        conn.sendall(Game.curr_level.levelNumber.to_bytes(2, 'big'))
        #data = conn.recv(1024)
        #print("New data from client " + str(data))

    def create_server_thread(self):
        thread = Thread(target=self.create_server, args=[])
        thread.start()

    def start_game_as_server(self):
        cubeAdventure = CubeAdventure()
        self.create_server_thread()
        cubeAdventure.start_game()

    def open_connect_to_server_menu(self):
        ConnectToServer = MenuConnectToServer()
        ConnectToServer.draw_menu()



    def get_menu_items_list(self):
        return self.menu_item_list
