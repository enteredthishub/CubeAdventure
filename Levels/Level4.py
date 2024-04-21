from Bar import Bar
from Levels.Level import Level


class Level4(Level):
    levelNumber = 3

    bar_list = [Bar(0, 200, 100, 50, (178, 242, 187)),
                Bar(100, 150, 50, 600, (178, 242, 187)),
                Bar(300, 300, 50, 450, (178, 242, 187)),
                Bar(1100, 200, 100, 50, (178, 242, 187)),
                Bar(1050, 150, 50, 600, (178, 242, 187)),
                Bar(850, 300, 50, 450, (178, 242, 187)),
                Bar(400, 350, 400, 50, (178, 242, 187)),
                Bar(100, 800, 1000, 50, (255, 201, 201)),
                Bar(200, 200, 50, 50, (178, 242, 187)),
                Bar(950, 200, 50, 50, (178, 242, 187)),
                Bar(450, 450, 50, 50, (178, 242, 187)),
                Bar(450, 650, 50, 50, (178, 242, 187)),
                Bar(700, 450, 50, 50, (178, 242, 187)),
                Bar(700, 650, 50, 50, (178, 242, 187)),
                Bar(575, 550, 50, 50, (178, 242, 187)),
                Bar(575, 750, 50, 50, (178, 242, 187)),
                Bar(575, 100, 50, 50, (178, 242, 187)),
                Bar(300, 0, 50, 50, (178, 242, 187)),
                Bar(850, 0, 50, 50, (178, 242, 187)),
                Bar(0, 850, 50, 50, (255, 0, 0), Bar.TYPE_DANGER),
                Bar(1150, 850, 50, 50, (255, 0, 0), Bar.TYPE_DANGER),
                ]

    def restart(self, player):
        super().restart(player)
        player.player_x = 0
        player.player_y = 0
        player.player_gravity = False

    # def get_next_level(self):
    #     level3 = Level3()
    #     return level3