import math

from Game import Game


class Weapon:
    PISTOL = 0
    MACHINE_GUN = 1
    RPG = 2
    SHOTGUN = 3

    weapon_target_x = 0
    weapon_target_y = 0
    weapon_bullet_speed = 20
    weapon_action = 0
    weapon_shoot_delay = 0
    weapon_type = 0

    def __init__(self, weapon_bullet_speed, weapon_action, weapon_shoot_delay, weapon_type):
        self.weapon_bullet_speed = weapon_bullet_speed
        self.weapon_action = weapon_action
        self.weapon_shoot_delay = weapon_shoot_delay
        self.weapon_type = weapon_type

    def shoot(self, weapon_target_x, weapon_target_y):
        pass


