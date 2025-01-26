import random

from Bar import Bar
from CaptureZone import CaptureZone
from Game import Game
from Levels.Level import Level
from Levels.Level2 import Level2
from PistolTheWeapon import PistolTheWeapon
from Player import Player


class Level1(Level):
    levelNumber = 0
    bar_list = [Bar(0, 300, 150, 50, (200, 155, 0)),
                Bar(100, 100, 50, 200, (0, 200, 0)),
                Bar(200, 0, 50, 50, (0, 200, 0)),
                #Bar(150, 150, 200, 50, (40, 160, 0)),
                Bar(0, 650, 400, 50, (40, 160, 0)),
                Bar(350, 150, 300, 50, (40, 160, 100)),
                Bar(450, 0, 50, 50, (100, 160, 255)),
                Bar(550, 300, 250, 50, (20, 0, 195)),
                Bar(900, 300, 200, 50, (20, 0, 195)),
                Bar(975, 100, 50, 50, (20, 0, 195)),
                Bar(750, 0, 50, 300, (20, 0, 195)),
                #Bar(0, 500, 200, 50, (20, 50, 15)),
                Bar(400, 400, 100, 400, (20, 80, 195)),
                Bar(600, 400, 100, 200, (20, 100, 195)),
                Bar(800, 650, 100, 200, (20, 100, 195)),
                Bar(150, 0, 50, 50, (200, 0, 0), Bar.TYPE_DANGER),
                Bar(900, 500, 50, 50, (100, 100, 0), Bar.TYPE_SPHERE),
                Bar(550, 50, 200, 50, (20, 100, 195)),
                Bar(600, 850, 50, 50, (200, 0, 0), Bar.TYPE_DANGER),
                Bar(1150, 0, 50, 900, (20, 50, 15)),
                Bar(150, 500, 50, 50, (20, 123, 150)),
                Bar(210, 350, 50, 50, (200, 0, 0), Bar.TYPE_DANGER),
                Bar(0, -50, Game.SCREEN_WIDTH, 50, (5, 50, 150)),
                Bar(0, Game.SCREEN_HEIGHT, Game.SCREEN_WIDTH, 50, (5, 50, 150)),
                Bar(-50, 0, 50, Game.SCREEN_HEIGHT, (5, 50, 150)),
                Bar(Game.SCREEN_WIDTH, 0, 50, Game.SCREEN_HEIGHT, (5, 50, 150)),
                Bar(1000, 600, 50, 50, (5, 50, 150)),
                Bar(50, 400, 50, 50, (5, 50, 150))
                ]

    zone_list = [CaptureZone([
                Bar(75, 425, 200, 200, (0, 0, 0), Bar.TYPE_ZONE)
    ], (100, 100, 100, 145)),
        CaptureZone([
            Bar(900, 25, 200, 200, (0, 0, 0), Bar.TYPE_ZONE)
        ], (100, 100, 100, 145))]

    #turret_list = [Player(300, 500, 50, 50, (0, 0, 0), Player.CONTROL_TYPE_TURRET)]

    def restart(self, player):
        super().restart(player)
        spawns_list = self.get_spawns_list()
        spawn_index = random.randint(0, len(spawns_list) - 1)
        spawn = spawns_list[spawn_index]  # [700, 0]
        player.player_x = spawn[0]
        player.player_y = spawn[1]
        player.player_gravity = False

    #def __init__(self):
        #self.turret_list[0].weapon_list.append(PistolTheWeapon(self.turret_list[0]))
        #Game.players += self.turret_list

    def get_next_level(self):
        level2 = Level2()
        return level2

    def get_spawns_list(self):
        self.spawns_list = [[0, 0], [700, 0], [0, 550]]
        return self.spawns_list

