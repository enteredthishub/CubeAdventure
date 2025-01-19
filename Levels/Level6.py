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

    bar_list = [Bar(600, 0, 50, 1000, (255, 0, 0),)]

    zone_list = []
    #turret_list = [Player(750, 500, 50, 50, (0, 0, 0), Player.CONTROL_TYPE_TURRET)]
    ai_list = [Player(750, 500, 50, 50, (0, 0, 0), Player.CONTROL_TYPE_AI)]

    def restart(self, player):
        super().restart(player)
        spawns_list = self.get_spawns_list()
        spawn_index = random.randint(0, len(spawns_list) - 1)
        spawn = spawns_list[spawn_index]  # [700, 0]
        player.player_x = spawn[0]
        player.player_y = spawn[1]
        player.player_gravity = False
        player.set_spawn_index(spawn_index)


    def start(self):
        #self.ai_list[0].weapon_list.append(MachineGunTheWeapon(self.ai_list[0]))
        self.ai_list[0].selected_weapon = 0
        Game.players += self.ai_list

    def get_spawns_list(self):
        self.spawns_list = [[0, 0],]
        return self.spawns_list

    #def __init__(self):
        #self.ai_list[0].weapon_list.append(PistolTheWeapon(self.ai_list[0]))
        #Game.players += self.ai_list


    # def get_next_level(self):
    #     level3 = Level3()
    #     return level3
    #
    #


