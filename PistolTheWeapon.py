import math

from Game import Game
from Weapon import Weapon

#His name is Weapon
class PistoTheWeapon(Weapon):

    def __init__(self):
        self.weapon_bullet_speed = 15
        self.weapon_action = None
        self.weapon_shoot_delay = 0.5
        self.weapon_type = Weapon.PISTOL
        super().__init__(self.weapon_bullet_speed, self.weapon_action, self.weapon_shoot_delay, self.weapon_type)

    def shoot(self, weapon_target_x, weapon_target_y):
        pass


