import math
import time

from pygame import Color

from Bullet import Bullet
from Game import Game
from Weapon import Weapon

#His name is MachineGun
class MachineGunTheWeapon(Weapon):

    weapon_last_shoot_time = 0

    def __init__(self, player):
        self.weapon_bullet_speed = 15
        self.weapon_action = None
        self.weapon_shoot_delay = 0.0001
        self.weapon_type = Weapon.MACHINE_GUN
        self.weapon_ammo = 120
        self.current_ammo = self.weapon_ammo
        self.reload_time = 3
        super().__init__(player, self.weapon_bullet_speed, self.weapon_action, self.weapon_shoot_delay, self.weapon_type)

    def shoot(self, weapon_target_x, weapon_target_y):
        shooting_allowed = super().shoot(weapon_target_x, weapon_target_y)
        if not shooting_allowed:
            return

        bullet = Bullet(bullet_originator=self.player, bullet_x=self.player.player_x, bullet_y=self.player.player_y, bullet_target_x=weapon_target_x, bullet_target_y=weapon_target_y, bullet_speed=self.weapon_bullet_speed, bullet_color=(200, 0, 10), bullet_radius=4, bullet_damage=5)
        Game.curr_level.bullet_list.append(bullet)
        self.player.bullet_list.append(bullet)



