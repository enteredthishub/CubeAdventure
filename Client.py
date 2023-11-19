import socket
from threading import Thread

from CubeAdventure import CubeAdventure
from Game import Game


class Client:
    def create_client(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("93.182.6.25", 45001))
        data = s.recv(1024)
        print("Current level: " + str(data))
        Game.curr_level = CubeAdventure.levels[int.from_bytes(data, "big")]
        #s.sendall(b"hello")

    def __init__(self):
        thread = Thread(target=self.create_client, args=[])
        thread.start()
