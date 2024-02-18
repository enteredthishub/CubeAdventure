import math

from Game import Game
from Weapon import Weapon

#His name is Pistol
class PistolTheWeapon(Weapon):

    def __init__(self, player):
        self.weapon_bullet_speed = 15
        self.weapon_action = None
        self.weapon_shoot_delay = 0.5
        self.weapon_type = Weapon.PISTOL
        super().__init__(player, self.weapon_bullet_speed, self.weapon_action, self.weapon_shoot_delay, self.weapon_type)

    def shoot(self, weapon_target_x, weapon_target_y):
        pass


