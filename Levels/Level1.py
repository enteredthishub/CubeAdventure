from Bar import Bar
from Levels.Level import Level
from Levels.Level2 import Level2


class Level1(Level):
    levelNumber = 0

    bar_list = [Bar(0, 300, 150, 50, (200, 155, 0)),
                Bar(100, 100, 50, 200, (0, 200, 0)),
                Bar(200, 0, 50, 50, (0, 200, 0)),
                Bar(150, 150, 200, 50, (40, 160, 0)),
                Bar(300, 50, 200, 50, (40, 160, 0)),
                Bar(350, 150, 300, 50, (40, 160, 100)),
                Bar(450, 0, 50, 50, (100, 160, 255)),
                Bar(200, 300, 800, 50, (20, 0, 195)),
                Bar(750, 0, 50, 300, (20, 0, 195)),
                Bar(0, 500, 200, 50, (20, 50, 15)),
                Bar(300, 350, 100, 200, (20, 80, 195)),
                Bar(600, 400, 100, 200, (20, 100, 195)),
                Bar(150, 0, 50, 50, (200, 0, 0), Bar.TYPE_DANGER),
                Bar(0, 200, 50, 50, (100, 100, 0), Bar.TYPE_SPHERE),

                ]

    def restart(self, player):
        player.player_x = 0
        player.player_y = 0
        player.player_gravity = False

    def get_next_level(self):
        level2 = Level2()
        return level2
