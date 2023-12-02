import socket
import time
from threading import Thread

from Game import Game
from Player import Player


class Server:
    client_player = None
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
        self.client_player = Player(0, 0, 50, 50, (0, 0, 0), Player.CONTROL_TYPE_INTERNET, None, None, None)
        Game.players = Game.players + [self.client_player]
        conn.sendall(Game.curr_level.levelNumber.to_bytes(2, 'big'))
        self.send_player_coords(conn)
        #data = conn.recv(1024)
        #print("New data from client " + str(data))

    def send_player_coords(self, conn):
        while True:
            conn.sendall(len(Game.players).to_bytes(2, 'big'))
            for p in Game.players:
                conn.sendall(int(p.player_x).to_bytes(2, 'big'))
                conn.sendall(int(p.player_y).to_bytes(2, 'big'))
            self.receive_player_coords(conn)
            #time.sleep(0.001)

    def receive_player_coords(self, s):
        data = s.recv(2)
        player_x = int.from_bytes(data, "big")
        self.client_player.player_x = player_x
        data = s.recv(2)
        player_y = int.from_bytes(data, "big")
        self.client_player.player_y = player_y

    def __init__(self):
        thread = Thread(target=self.create_server, args=[])
        thread.start()
