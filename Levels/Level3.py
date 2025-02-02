from Bar import Bar
from CaptureZone import CaptureZone
from Game import Game
from Levels.Level import Level


class Level3(Level):
    levelNumber = 2

    teleport_to1 = Bar(750, 400, 50, 50, (100, 75, 255), Bar.TYPE_PORTAL_2)
    bar_list = [Bar(0, 300, 150, 50, (200, 155, 200)),
                Bar(0, 550, 700, 50, (200, 0, 0), Bar.TYPE_DANGER),
                Bar(250, 300, 50, 50, (0, 0, 255), Bar.TYPE_BLUE_SPHERE),
                Bar(100, 0, 800, 50, (200, 0, 0), Bar.TYPE_DANGER),
                Bar(350, 100, 50, 50, (0, 0, 255), Bar.TYPE_BLUE_SPHERE),
                Bar(450, 300, 50, 50, (0, 0, 255), Bar.TYPE_BLUE_SPHERE),
                Bar(550, 300, 200, 50, (255, 100, 255)),
                Bar(650, 200, 50, 50, (20, 125, 255), Bar.TYPE_PORTAL_1, teleport_to=teleport_to1),
                teleport_to1,
                Bar(750, 50, 50, 300, (105, 104, 153)),
                Bar(0, -50, Game.SCREEN_WIDTH, 50, (5, 50, 150)),
                Bar(0, Game.SCREEN_HEIGHT, Game.SCREEN_WIDTH, 50, (5, 50, 150)),
                Bar(-50, 0, 50, Game.SCREEN_HEIGHT, (5, 50, 150)),
                Bar(Game.SCREEN_WIDTH, 0, 50, Game.SCREEN_HEIGHT, (5, 50, 150)),
                ]


    def restart(self, player):
        super().restart(player)
        player.player_x = 0
        player.player_y = 0
        player.player_gravity = False

    # def get_next_level(self):
    #     level3 = Level3()
    #     return level3