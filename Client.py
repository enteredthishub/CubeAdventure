import socket
from threading import Thread



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
        self.receive_player_coords(s)
        #s.sendall(b"hello")

    initialized = False
    internet_players = []
    def receive_player_coords(self, s):
        while True:
            data = s.recv(2)
            number_of_players = int.from_bytes(data, "big")
            print("Number of players: " + str(number_of_players))
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
                print("player_x: " + str(player_x))
                data = s.recv(2)
                player_y = int.from_bytes(data, "big")
                ip.player_y = player_y
                print("player_y: " + str(player_y))

    def __init__(self):
        thread = Thread(target=self.create_client, args=[])
        thread.start()


# Game.players: [player1, player2]

# Game.players: [player1, player2, internet_player1, internet_player2]
