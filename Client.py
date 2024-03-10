import socket
import time
from threading import Thread

from Bullet import Bullet
from CubeAdventure import CubeAdventure
from Game import Game
from Player import Player


class Client:
    def create_client(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("93.182.6.25", 45001))
        data = s.recv(2)
        print("Current level: " + str(data))
        Game.curr_level = CubeAdventure.levels[int.from_bytes(data, "big")]
        self.send_player_coords_thread(s)
        self.send_and_receive_player_coords(s)
        #s.sendall(b"hello")

    initialized = False
    internet_players = []
    def send_and_receive_player_coords(self, s):
        while True:
            data = s.recv(2)
            number_of_players = int.from_bytes(data, "big")
            if not self.initialized:
                for n in range(0, number_of_players):
                    player = Player(0, 0, 50, 50, (0, 0, 0), Player.CONTROL_TYPE_INTERNET, None, None, None)
                    Game.players = Game.players + [player]
                    self.internet_players = self.internet_players + [player]
                self.initialized = True

            for ip in self.internet_players:
                data = s.recv(2)
                player_x = int.from_bytes(data, "big")
                ip.player_x = player_x
                data = s.recv(2)
                player_y = int.from_bytes(data, "big")
                ip.player_y = player_y
                data = s.recv(2)
                flag = int.from_bytes(data, "big")
                if flag == 1:
                    bullet = Bullet(bullet_originator=ip, bullet_x=self.get_int(s), bullet_y=self.get_int(s), bullet_target_x=self.get_int(s),
                                    bullet_target_y=self.get_int(s), bullet_speed=self.get_int(s), bullet_color=(self.get_int(s), self.get_int(s), self.get_int(s)), bullet_radius=self.get_int(s))
                    Game.curr_level.bullet_list.append(bullet)
                    ip.bullet_list.append(bullet)

    def get_int(self, s):
        data = s.recv(2)
        return int.from_bytes(data, "big")

    def send_player_coords(self, s):
        p = Game.players[0]
        while True:
            s.sendall(int(p.player_x).to_bytes(2, 'big'))
            s.sendall(int(p.player_y).to_bytes(2, 'big'))
            bullet = self.get_last_bullet(p)
            if bullet != None and bullet.bullet_x > 0 and bullet.bullet_y > 0:  # FIXME
                # print("x: " + str(bullet.bullet_x) + " y: " + str(bullet.bullet_y))
                s.sendall(int(1).to_bytes(2, 'big'))
                s.sendall(int(bullet.bullet_x).to_bytes(2, 'big'))
                s.sendall(int(bullet.bullet_y).to_bytes(2, 'big'))
                s.sendall(int(bullet.bullet_target_x).to_bytes(2, 'big'))
                s.sendall(int(bullet.bullet_target_y).to_bytes(2, 'big'))
                s.sendall(int(bullet.bullet_speed).to_bytes(2, 'big'))
                s.sendall(int(bullet.bullet_color[0]).to_bytes(2, 'big'))
                s.sendall(int(bullet.bullet_color[1]).to_bytes(2, 'big'))
                s.sendall(int(bullet.bullet_color[2]).to_bytes(2, 'big'))
                s.sendall(int(bullet.bullet_radius).to_bytes(2, 'big'))
            else:
                s.sendall(int(0).to_bytes(2, 'big'))
            time.sleep(0.01)

    prev_bullet = None
    def get_last_bullet(self, p):
        if len(p.bullet_list) > 0 and p.bullet_list[-1] != self.prev_bullet:
            self.prev_bullet = p.bullet_list[-1]
            return p.bullet_list[-1]
        else:
            return None

    def __init__(self):
        thread = Thread(target=self.create_client, args=[])
        thread.start()

    def send_player_coords_thread(self, s):
        thread = Thread(target=self.send_player_coords, args=[s])
        thread.start()


# Game.players: [player1, player2]

# Game.players: [player1, player2, internet_player1, internet_player2]
