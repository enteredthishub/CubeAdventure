import socket
import time
from threading import Thread

from Bullet import Bullet
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
        self.receive_player_coords_thread(conn)
        self.send_player_coords(conn)
        #data = conn.recv(1024)
        #print("New data from client " + str(data))

    def send_player_coords(self, conn):
        while True:
            conn.sendall((len(Game.players)-1).to_bytes(2, 'big'))
            for p in Game.players:
                if p.control_type != Player.CONTROL_TYPE_INTERNET:
                    conn.sendall(int(p.player_x).to_bytes(2, 'big'))
                    conn.sendall(int(p.player_y).to_bytes(2, 'big'))
                    bullet = self.get_last_bullet(p)
                    if bullet != None and bullet.bullet_x > 0 and bullet.bullet_y > 0 \
                            and bullet.bullet_target_x > 0 and bullet.bullet_target_y > 0: # FIXME
                        #print("x: " + str(bullet.bullet_x) + " y: " + str(bullet.bullet_y))
                        conn.sendall(int(1).to_bytes(2, 'big'))
                        conn.sendall(int(bullet.bullet_x).to_bytes(2, 'big'))
                        conn.sendall(int(bullet.bullet_y).to_bytes(2, 'big'))
                        conn.sendall(int(bullet.bullet_target_x).to_bytes(2, 'big'))
                        conn.sendall(int(bullet.bullet_target_y).to_bytes(2, 'big'))
                        conn.sendall(int(bullet.bullet_speed).to_bytes(2, 'big'))
                        conn.sendall(int(bullet.bullet_color[0]).to_bytes(2, 'big'))
                        conn.sendall(int(bullet.bullet_color[1]).to_bytes(2, 'big'))
                        conn.sendall(int(bullet.bullet_color[2]).to_bytes(2, 'big'))
                        conn.sendall(int(bullet.bullet_radius).to_bytes(2, 'big'))
                    else:
                        conn.sendall(int(0).to_bytes(2, 'big'))
            time.sleep(0.01)

    prev_bullet = None
    def get_last_bullet(self, p):
        if len(p.bullet_list) > 0 and p.bullet_list[-1] != self.prev_bullet:
            self.prev_bullet = p.bullet_list[-1]
            return p.bullet_list[-1]
        else:
            return None


    def receive_player_coords(self, s):
        while True:
            data = s.recv(2)
            player_x = int.from_bytes(data, "big")
            self.client_player.player_x = player_x
            data = s.recv(2)
            player_y = int.from_bytes(data, "big")
            self.client_player.player_y = player_y
            data = s.recv(2)
            flag = int.from_bytes(data, "big")
            if flag == 1:
                bullet = Bullet(bullet_originator=self.client_player, bullet_x=self.get_int(s), bullet_y=self.get_int(s), bullet_target_x=self.get_int(s),
                                bullet_target_y=self.get_int(s), bullet_speed=self.get_int(s), bullet_color=(self.get_int(s), self.get_int(s), self.get_int(s)), bullet_radius=self.get_int(s))
                Game.curr_level.bullet_list.append(bullet)
                self.client_player.bullet_list.append(bullet)

            #print(str(time.time()) + ": " + str(player_x) + ", " + str(player_y))

    def __init__(self):
        thread = Thread(target=self.create_server, args=[])
        thread.start()

    def receive_player_coords_thread(self, s):
        thread = Thread(target=self.receive_player_coords, args=[s])
        thread.start()

    def get_int(self, s):
        data = s.recv(2)
        return int.from_bytes(data, "big")