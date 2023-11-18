from Game import Game


class Level:
    levelNumber = None
    bar_list = []

    def restartAll(self):
        for p in Game.players:
            self.restart(p)

    def restart(self, player):
        pass

    def get_next_level(self):
        pass
