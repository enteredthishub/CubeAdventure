import math
import time

from Bullet import Bullet
from Game import Game
from Weapon import Weapon

#His name is Pistol
class RPGTheWeapon(Weapon):


    def __init__(self, player):
        self.weapon_bullet_speed = 6
        self.weapon_action = None
        self.weapon_shoot_delay = 1
        self.weapon_type = Weapon.RPG
        self.weapon_ammo = 1
        self.current_ammo = self.weapon_ammo
        self.reload_time = 5
        super().__init__(player, self.weapon_bullet_speed, self.weapon_action, self.weapon_shoot_delay, self.weapon_type)

    def shoot(self, weapon_target_x, weapon_target_y):
        shooting_allowed = super().shoot(weapon_target_x, weapon_target_y)
        if not shooting_allowed:
            return
        bullet = Bullet(bullet_originator=self.player, bullet_weapon=self, bullet_x=self.player.player_x, bullet_y=self.player.player_y, bullet_target_x=weapon_target_x, bullet_target_y=weapon_target_y, bullet_speed=self.weapon_bullet_speed, bullet_color=self.player.player_color, bullet_radius=20, bullet_damage=100)
        Game.curr_level.bullet_list.append(bullet)
        self.player.bullet_list.append(bullet)

        #TODO: Do a shrapnel explosive for RPG

    def perform_weapon_action(self, player, bullet_originator, bullet_x, bullet_y, damage):
        print('sus')


