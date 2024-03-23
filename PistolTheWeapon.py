import math
import time

from Bullet import Bullet
from Game import Game
from Weapon import Weapon

#His name is Pistol
class PistolTheWeapon(Weapon):

    weapon_last_shoot_time = 0

    def __init__(self, player):
        self.weapon_bullet_speed = 15
        self.weapon_action = None
        self.weapon_shoot_delay = 0.5
        self.weapon_type = Weapon.PISTOL
        self.ammo = 17
        self.reload_time = 3
        super().__init__(player, self.weapon_bullet_speed, self.weapon_action, self.weapon_shoot_delay, self.weapon_type)

    def shoot(self, weapon_target_x, weapon_target_y):

        if self.weapon_state != Weapon.STATE_READY:
            if self.weapon_state == Weapon.STATE_RELOADING:
                if time.time() - self.weapon_reload_start_time > self.reload_time:
                    self.ammo = 17
                    self.weapon_state = Weapon.STATE_READY
                else:
                    return
        if time.time() - self.weapon_last_shoot_time < self.weapon_shoot_delay:
            return
        self.weapon_last_shoot_time = time.time()
        bullet = Bullet(bullet_originator=self.player, bullet_x=self.player.player_x, bullet_y=self.player.player_y, bullet_target_x=weapon_target_x, bullet_target_y=weapon_target_y, bullet_speed=self.weapon_bullet_speed, bullet_color=self.player.player_color)
        Game.curr_level.bullet_list.append(bullet)
        self.player.bullet_list.append(bullet)
        self.ammo -= 1
        if self.ammo == 0:
            self.weapon_state = Weapon.STATE_RELOADING
            self.weapon_reload_start_time = time.time()





