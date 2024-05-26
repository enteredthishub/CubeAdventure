import random

from Bar import Bar
from Levels.Level import Level


class Level4(Level):
    levelNumber = 3

    bar_list = [Bar(0, 200, 100, 50, (200, 162, 157)),
                Bar(100, 150, 50, 600, (150, 162, 107)),
                Bar(300, 300, 50, 450, (98, 162, 107)),
                Bar(1100, 200, 100, 50, (150, 162, 107)),
                Bar(1050, 150, 50, 600, (150, 162, 107)),
                Bar(850, 300, 50, 450, (98, 162, 107)),
                Bar(400, 350, 400, 50, (150, 162, 107)),
                #Bar(100, 800, 1000, 50, (255, 201, 201)),
                Bar(200, 200, 50, 50, (150, 162, 107)),
                Bar(950, 200, 50, 50, (98, 162, 107)),
                Bar(450, 450, 50, 50, (150, 162, 255)),
                Bar(450, 650, 50, 50, (150, 162, 107)),
                Bar(700, 450, 50, 50, (98, 162, 107)),
                Bar(700, 650, 50, 50, (150, 162, 107)),
                Bar(575, 550, 50, 50, (150, 162, 255)),
                #Bar(575, 750, 50, 50, (150, 162, 107)),
                Bar(575, 100, 50, 50, (150, 162, 107)),
                Bar(300, 0, 50, 50, (150, 162, 107)),
                Bar(850, 0, 50, 50, (150, 162, 107)),
                Bar(0, 850, 50, 50, (255, 0, 0), Bar.TYPE_DANGER),
                Bar(1150, 850, 50, 50, (255, 0, 0), Bar.TYPE_DANGER),
                Bar(100, 750, 25, 50, (0, 0, 0), Bar.TYPE_SPAWN_1),
                Bar(1075, 750, 25, 50, (255, 0, 0), Bar.TYPE_SPAWN_0),
                Bar(525, 500, 150, 150, (150, 162, 255, 145), Bar.TYPE_ZONE)
                ]

    def restart(self, player):
        super().restart(player)
        spawns_list = self.get_spawns_list()
        spawn_index = random.randint(0, len(spawns_list) - 1)
        spawn = spawns_list[spawn_index]  # [700, 0]
        player.player_x = spawn[0]
        player.player_y = spawn[1]
        player.player_gravity = False
        player.set_spawn_index(spawn_index)

    def get_spawns_list(self):
        self.spawns_list = [[0, 0], [1150, 0],]
        return self.spawns_list

    # def get_next_level(self):
    #     level3 = Level3()
    #     return level3
    # TODO: do a capture point, that player is supposed to hold for some period of time to win.
    # #WarThunderIsBeautiful #Snails
