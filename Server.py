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
        self.receive_data_thread(conn)
        self.send_data(conn)
        #data = conn.recv(1024)
        #print("New data from client " + str(data))

    def send_data(self, conn):
        while True:
            #Players data
            conn.sendall((len(Game.players)-1).to_bytes(2, 'big'))
            for p in Game.players:
                if p.control_type != Player.CONTROL_TYPE_INTERNET:
                    if p.player_x < 0: p.player_x = 0
                    if p.player_y < 0: p.player_y = 0
                    conn.sendall(int(p.player_x).to_bytes(2, 'big'))
                    conn.sendall(int(p.player_y).to_bytes(2, 'big'))
                    conn.sendall(int(p.player_color[0]).to_bytes(2, 'big'))
                    conn.sendall(int(p.player_color[1]).to_bytes(2, 'big'))
                    conn.sendall(int(p.player_color[2]).to_bytes(2, 'big'))
                    bullets = self.get_unsent_bullets(p)
                    if bullets != None: # FIXME
                        #print("x: " + str(bullet.bullet_x) + " y: " + str(bullet.bullet_y))
                        conn.sendall(int(len(bullets)).to_bytes(2, 'big'))
                        for bullet in bullets:
                            if bullet.bullet_x < 0 or bullet.bullet_y < 0:
                                continue
                            conn.sendall(int(bullet.bullet_x).to_bytes(2, 'big'))
                            conn.sendall(int(bullet.bullet_y).to_bytes(2, 'big'))
                            conn.sendall(int(bullet.bullet_target_x).to_bytes(2, 'big'))
                            conn.sendall(int(bullet.bullet_target_y).to_bytes(2, 'big'))
                            conn.sendall(int(bullet.bullet_speed).to_bytes(2, 'big'))
                            conn.sendall(int(bullet.bullet_color[0]).to_bytes(2, 'big'))
                            conn.sendall(int(bullet.bullet_color[1]).to_bytes(2, 'big'))
                            conn.sendall(int(bullet.bullet_color[2]).to_bytes(2, 'big'))
                            conn.sendall(int(bullet.bullet_radius).to_bytes(2, 'big'))
                            conn.sendall(int(bullet.bullet_damage).to_bytes(2, 'big'))
                    else:
                        conn.sendall(int(0).to_bytes(2, 'big'))

            #Zones data
            for z in Game.curr_level.zone_list:
                conn.sendall(int(z.zone_color[0]).to_bytes(2, 'big'))
                conn.sendall(int(z.zone_color[1]).to_bytes(2, 'big'))
                conn.sendall(int(z.zone_color[2]).to_bytes(2, 'big'))
                conn.sendall(int(z.zone_color[3]).to_bytes(2, 'big'))
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


    def receive_data(self, s):
        while True:
            self.client_player.player_x = self.get_int(s)
            self.client_player.player_y = self.get_int(s)
            self.client_player.player_color = (self.get_int(s), self.get_int(s), self.get_int(s))
            bullets_amount = self.get_int(s)
            if bullets_amount > 0:
                for i in range(0, bullets_amount):
                    bullet = Bullet(bullet_originator=self.client_player,
                                    bullet_x=self.get_int(s),
                                    bullet_y=self.get_int(s),
                                    bullet_target_x=self.get_int(s),
                                    bullet_target_y=self.get_int(s),
                                    bullet_speed=self.get_int(s),
                                    bullet_color=(self.get_int(s), self.get_int(s), self.get_int(s)),
                                    bullet_radius=self.get_int(s),
                                    bullet_damage=self.get_int(s))
                    Game.curr_level.bullet_list.append(bullet)
                    self.client_player.bullet_list.append(bullet)
            for z in Game.curr_level.zone_list:
                z.zone_color = (self.get_int(s), self.get_int(s), self.get_int(s), self.get_int(s))

            #print(str(time.time()) + ": " + str(player_x) + ", " + str(player_y))

    def __init__(self):
        thread = Thread(target=self.create_server, args=[])
        thread.start()

    def receive_data_thread(self, s):
        thread = Thread(target=self.receive_data, args=[s])
        thread.start()

    def get_int(self, s):
        data = s.recv(2)
        return int.from_bytes(data, "big")