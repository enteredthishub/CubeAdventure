from Bar import Bar
from Levels.Level import Level


class Level3(Level):
    bar_list = [Bar(0, 300, 150, 50, (200, 155, 200)),
                Bar(0, 550, 750, 50, (200, 0, 0), Bar.TYPE_DANGER),
                Bar(250, 300, 50, 50, (0, 0, 255), Bar.TYPE_BLUE_SPHERE),
                Bar(100, 0, 800, 50, (200, 0, 0), Bar.TYPE_DANGER),
                Bar(350, 100, 50, 50, (0, 0, 255), Bar.TYPE_BLUE_SPHERE),
                Bar(450, 300, 50, 50, (0, 0, 255), Bar.TYPE_BLUE_SPHERE),
                Bar(550, 300, 200, 50, (255, 100, 255)),
                ]

    def restart(self, player):
        player.player_x = 0
        player.player_y = 0
        player.player_gravity = False

    # def get_next_level(self):
    #     level3 = Level3()
    #     return level3