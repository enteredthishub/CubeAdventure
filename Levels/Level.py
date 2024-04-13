from Game import Game
from Player import Player


class Level:
    levelNumber = None
    bar_list = []
    bullet_list = []
    spawns_list = []

    def restartAll(self):
        for p in Game.players:
            self.restart(p)

    def restart(self, player):
        player.health_now = Player.HEALTH_POINTS

    def get_next_level(self):
        pass

    def get_spawns_list(self):
        self.spawns_list = [[0, 0]]
        return self.spawns_list
