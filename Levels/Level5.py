import random

from Bar import Bar
from CaptureZone import CaptureZone
from Game import Game
from Levels.Level import Level
from MachineGunTheWeapon import MachineGunTheWeapon
from PistolTheWeapon import PistolTheWeapon
from Player import Player


class Level5(Level):
    levelNumber = 4

    bar_list = [Bar(0, 200, 100, 50, (200, 162, 157)),
                Bar(100, 150, 50, 450, (150, 162, 107)),
                Bar(300, 200, 50, 250, (98, 162, 107)),
                Bar(1100, 200, 100, 50, (150, 162, 107)),
                Bar(1050, 150, 50, 450, (150, 162, 107)),
                Bar(850, 200, 50, 250, (98, 162, 107)),
                Bar(450, 300, 300, 50, (150, 162, 107)),
                Bar(150, 850, 900, 50, (150, 162, 107)),
                Bar(575, 500, 50, 300, (150, 162, 107)),
                Bar(450, 250, 50, 50, (255, 0, 0), Bar.TYPE_DANGER),
                Bar(850, 800, 50, 50, (255, 0, 0), Bar.TYPE_DANGER),
                Bar(575, 0, 50, 50, (255, 0, 0), Bar.TYPE_DANGER),
                Bar(700, 250, 50, 50, (255, 0, 0), Bar.TYPE_DANGER),
                Bar(300, 800, 50, 50, (255, 0, 0), Bar.TYPE_DANGER),
                Bar(100, 650, 50, 50, (150, 162, 107)),
                Bar(300, 650, 50, 50, (150, 162, 107)),
                Bar(525, 650, 50, 50, (150, 162, 107)),
                Bar(625, 650, 50, 50, (150, 162, 107)),
                Bar(850, 650, 50, 50, (150, 162, 107)),
                Bar(1050, 650, 50, 50, (150, 162, 107)),
                Bar(400, 100, 50, 50, (150, 162, 107)),
                Bar(575, 100, 50, 50, (150, 162, 107)),
                Bar(750, 100, 50, 50, (150, 162, 107)),
                Bar(200, 200, 50, 50, (150, 162, 107)),
                Bar(950, 200, 50, 50, (150, 162, 107)),
                Bar(0, 750, 50, 50, (150, 162, 107)),
                Bar(1150, 750, 50, 50, (150, 162, 107)),
                # #Bar(100, 800, 1000, 50, (255, 201, 201)),
                # Bar(200, 200, 50, 50, (150, 162, 107)),
                # Bar(950, 200, 50, 50, (98, 162, 107)),
                # Bar(450, 450, 50, 50, (150, 162, 255)),
                # Bar(450, 650, 50, 50, (150, 162, 107)),
                # Bar(700, 450, 50, 50, (98, 162, 107)),
                # Bar(700, 650, 50, 50, (150, 162, 107)),
                # Bar(575, 550, 50, 50, (150, 162, 255)),
                # #Bar(575, 750, 50, 50, (150, 162, 107)),
                # Bar(575, 100, 50, 50, (150, 162, 107)),
                # Bar(300, 0, 50, 50, (150, 162, 107)),
                # Bar(850, 0, 50, 50, (150, 162, 107)),
                # Bar(0, 850, 50, 50, (255, 0, 0), Bar.TYPE_DANGER),
                # Bar(1150, 850, 50, 50, (255, 0, 0), Bar.TYPE_DANGER),
                # Bar(100, 750, 25, 50, (0, 0, 0), Bar.TYPE_SPAWN_1),
                # Bar(1075, 750, 25, 50, (255, 0, 0), Bar.TYPE_SPAWN_0),
                ]

    zone_list = [CaptureZone([
                Bar(0, 650, 150, 150, (0, 0, 0), Bar.TYPE_ZONE)
    ], (100, 100, 100, 145)),
        CaptureZone([
            Bar(1050, 650, 150, 150, (0, 0, 0), Bar.TYPE_ZONE)
        ], (100, 100, 100, 145))
    ]
    turret_list = [Player(400, 500, 50, 50, (100, 100, 100), Player.CONTROL_TYPE_TURRET),
                   Player(750, 500, 50, 50, (100, 100, 100), Player.CONTROL_TYPE_TURRET)
    ]


    def restart(self, player):
        super().restart(player)
        if player.control_type != Player.CONTROL_TYPE_TURRET:
            spawns_list = self.get_spawns_list()
            spawn_index = random.randint(0, len(spawns_list) - 1)
            spawn = spawns_list[spawn_index]  # [700, 0]
            player.player_x = spawn[0]
            player.player_y = spawn[1]
            player.player_gravity = False
            player.set_spawn_index(spawn_index)

    def start(self):
        self.turret_list[0].weapon_list.append(PistolTheWeapon(self.turret_list[0]))
        Game.players += self.turret_list
        self.turret_list[1].weapon_list.append(PistolTheWeapon(self.turret_list[1]))
        Game.players += self.turret_list

    def get_spawns_list(self):
        self.spawns_list = [[0, 0], [1150, 0],]
        return self.spawns_list

    #def __init__(self):


    # def get_next_level(self):
    #     level3 = Level3()
    #     return level3
    #
    #

    #Turret:
    #Don't fire at WALLS
    #DO IT NOT SO STUPID
    #Edit it spawn
