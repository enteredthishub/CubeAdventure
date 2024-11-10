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
        self.send_data_thread(s)
        self.send_and_receive_data(s)
        #s.sendall(b"hello")

    initialized = False
    internet_players = []
    def send_and_receive_data(self, s):
        while True:
            data = s.recv(2)
            number_of_players = int.from_bytes(data, "big")
            if not self.initialized:
                p = Game.players[0]
                p.player_color = (200, 50, 50)
                for n in range(0, number_of_players):
                    player = Player(0, 0, 50, 50, (0, 0, 0), Player.CONTROL_TYPE_INTERNET, None, None, None)
                    Game.players = Game.players + [player]
                    self.internet_players = self.internet_players + [player]
                self.initialized = True

            for ip in self.internet_players:
                ip.player_x = self.get_int(s)
                ip.player_y = self.get_int(s)
                ip.player_color = (self.get_int(s), self.get_int(s), self.get_int(s))
                bullets_amount = self.get_int(s)
                if bullets_amount > 0:
                    for i in range(0, bullets_amount):
                        bullet = Bullet(bullet_originator=ip,
                                        bullet_weapon=ip.weapon_list[self.get_int(s)],
                                        bullet_x=self.get_int(s),
                                        bullet_y=self.get_int(s),
                                        bullet_target_x=self.get_int(s),
                                        bullet_target_y=self.get_int(s),
                                        bullet_speed=self.get_int(s),
                                        bullet_color=(self.get_int(s), self.get_int(s), self.get_int(s)),
                                        bullet_radius=self.get_int(s),
                                        bullet_damage=self.get_int(s))
                        Game.curr_level.bullet_list.append(bullet)
                        ip.bullet_list.append(bullet)

            for z in Game.curr_level.zone_list:
                z.zone_color = (self.get_int(s), self.get_int(s), self.get_int(s), self.get_int(s))
                for p in Game.players:
                    if z.zone_color[0] == p.player_color[0] and z.zone_color[1] == p.player_color[1] and z.zone_color[2] == p.player_color[2]:
                        z.capture_player = p

    def get_int(self, s):
        data = s.recv(2)
        return int.from_bytes(data, "big")

    def send_data(self, s):
        p = Game.players[0]
        while True:
            # Players data
            if p.player_x < 0: p.player_x = 0
            if p.player_y < 0: p.player_y = 0
            s.sendall(int(p.player_x).to_bytes(2, 'big'))
            s.sendall(int(p.player_y).to_bytes(2, 'big'))
            s.sendall(int(p.player_color[0]).to_bytes(2, 'big'))
            s.sendall(int(p.player_color[1]).to_bytes(2, 'big'))
            s.sendall(int(p.player_color[2]).to_bytes(2, 'big'))
            bullets = self.get_unsent_bullets(p)
            if bullets != None:
                # print("x: " + str(bullet.bullet_x) + " y: " + str(bullet.bullet_y))
                s.sendall(int(len(bullets)).to_bytes(2, 'big'))
                for bullet in bullets:
                    if bullet.bullet_x < 0 or bullet.bullet_y < 0:
                        continue
                    s.sendall(int(p.weapon_list.index(bullet.bullet_weapon)).to_bytes(2, 'big'))
                    s.sendall(int(bullet.bullet_x).to_bytes(2, 'big'))
                    s.sendall(int(bullet.bullet_y).to_bytes(2, 'big'))
                    s.sendall(int(bullet.bullet_target_x).to_bytes(2, 'big'))
                    s.sendall(int(bullet.bullet_target_y).to_bytes(2, 'big'))
                    s.sendall(int(bullet.bullet_speed).to_bytes(2, 'big'))
                    s.sendall(int(bullet.bullet_color[0]).to_bytes(2, 'big'))
                    s.sendall(int(bullet.bullet_color[1]).to_bytes(2, 'big'))
                    s.sendall(int(bullet.bullet_color[2]).to_bytes(2, 'big'))
                    s.sendall(int(bullet.bullet_radius).to_bytes(2, 'big'))
                    s.sendall(int(bullet.bullet_damage).to_bytes(2, 'big'))
            else:
                s.sendall(int(0).to_bytes(2, 'big'))

            # Zones data
            for z in Game.curr_level.zone_list:
                s.sendall(int(z.zone_color[0]).to_bytes(2, 'big'))
                s.sendall(int(z.zone_color[1]).to_bytes(2, 'big'))
                s.sendall(int(z.zone_color[2]).to_bytes(2, 'big'))
                s.sendall(int(z.zone_color[3]).to_bytes(2, 'big'))
            time.sleep(0.01)

    prev_bullet = None
    def get_last_bullet(self, p):
        if len(p.bullet_list) > 0 and p.bullet_list[-1] != self.prev_bullet:
            self.prev_bullet = p.bullet_list[-1]
            return p.bullet_list[-1]
        else:
            return None

    def get_unsent_bullets(self, p):
        if len(p.bullet_list) > 0 and p.bullet_list[-1] != self.prev_bullet:
            i = -1
            bullet_list_to_send = []
            if self.prev_bullet is None:
                self.prev_bullet = p.bullet_list[-1]
                return p.bullet_list
            while True:
                if p.bullet_list[i] == self.prev_bullet:
                    break
                else:
                    bullet_list_to_send.append(p.bullet_list[i])
                i -= 1
            self.prev_bullet = p.bullet_list[-1]
            return bullet_list_to_send
        else:
            return None



    def __init__(self):
        thread = Thread(target=self.create_client, args=[])
        thread.start()

    def send_data_thread(self, s):
        thread = Thread(target=self.send_data, args=[s])
        thread.start()


# Game.players: [player1, player2]

# Game.players: [player1, player2, internet_player1, internet_player2]
