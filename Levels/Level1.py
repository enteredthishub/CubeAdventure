import random

from Bar import Bar
from Levels.Level import Level
from Levels.Level2 import Level2


class Level1(Level):
    levelNumber = 0
    bar_list = [Bar(0, 300, 150, 50, (200, 155, 0)),
                Bar(100, 100, 50, 200, (0, 200, 0)),
                Bar(200, 0, 50, 50, (0, 200, 0)),
                #Bar(150, 150, 200, 50, (40, 160, 0)),
                Bar(300, 50, 200, 50, (40, 160, 0)),
                Bar(350, 150, 300, 50, (40, 160, 100)),
                Bar(450, 0, 50, 50, (100, 160, 255)),
                Bar(200, 300, 800, 50, (20, 0, 195)),
                Bar(750, 0, 50, 300, (20, 0, 195)),
                #Bar(0, 500, 200, 50, (20, 50, 15)),
                Bar(300, 350, 100, 200, (20, 80, 195)),
                Bar(600, 400, 100, 200, (20, 100, 195)),
                Bar(150, 0, 50, 50, (200, 0, 0), Bar.TYPE_DANGER),
                Bar(0, 200, 50, 50, (100, 100, 0), Bar.TYPE_SPHERE),
                Bar(550, 50, 200, 50, (20, 100, 195)),
                Bar(600, 100, 50, 50, (200, 0, 0), Bar.TYPE_DANGER),
                Bar(100, 400, 50, 200, (20, 50, 15)),
                Bar(0, 500, 50, 50, (20, 123, 150)),
                Bar(210, 350, 50, 50, (200, 0, 0), Bar.TYPE_DANGER),
                Bar(50, 400, 50, 50, (5, 50, 150)),
                ]

    def restart(self, player):
        spawns_list = self.get_spawns_list()
        spawn_index = random.randint(0, len(spawns_list) - 1)
        spawn = spawns_list[spawn_index]  # [700, 0]
        player.player_x = spawn[0]
        player.player_y = spawn[1]
        player.player_gravity = False

    def get_next_level(self):
        level2 = Level2()
        return level2

    def get_spawns_list(self):
        self.spawns_list = [[0, 0], [700, 0], [0, 550]]
        return self.spawns_list

