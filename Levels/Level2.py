from Bar import Bar
from Levels.Level import Level
from Levels.Level3 import Level3


class Level2(Level):
    bar_list = [Bar(0, 300, 150, 50, (200, 155, 200)),
                Bar(100, 100, 50, 200, (0, 200, 100)),
                Bar(250, 500, 500, 50, (0, 200, 100), Bar.TYPE_SPHERE),
                Bar(0, 550, 750, 50, (200, 0, 0), Bar.TYPE_DANGER),
                Bar(150, 0, 800, 50, (200, 0, 0), Bar.TYPE_DANGER),
                Bar(300, 400, 800, 50, (20, 55, 70)),
                Bar(210, 100, 50, 50, (200, 0, 0), Bar.TYPE_DANGER),
                Bar(150, 200, 50, 50, (55, 80, 65)),
                Bar(260, 150, 50, 50, (200, 0, 0), Bar.TYPE_DANGER),
                Bar(200, 250, 50, 50, (55, 80, 65)),
                ]

    def restart(self, player):
        player.player_x = 0
        player.player_y = 0
        player.player_gravity = False

    def get_next_level(self):
        level3 = Level3()
        return level3