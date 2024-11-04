import random

from Bar import Bar
from CaptureZone import CaptureZone
from Game import Game
from Levels.Level import Level
from MachineGunTheWeapon import MachineGunTheWeapon
from PistolTheWeapon import PistolTheWeapon
from Player import Player


class Level6(Level):
    levelNumber = 5

    bar_list = []

    zone_list = []
    turret_list = [Player(750, 500, 50, 50, (0, 0, 0), Player.CONTROL_TYPE_TURRET)]

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

    #def __init__(self):
        #self.turret_list[0].weapon_list.append(MachineGunTheWeapon(self.turret_list[0]))
        #Game.players += self.turret_list
        #self.turret_list[1].weapon_list.append(PistolTheWeapon(self.turret_list[1]))
        #Game.players += self.turret_list

    # def get_next_level(self):
    #     level3 = Level3()
    #     return level3
    #
    #


