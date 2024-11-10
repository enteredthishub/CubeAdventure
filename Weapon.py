import math
import time

from Game import Game


class Weapon:
    PISTOL = 0
    MACHINE_GUN = 1
    RPG = 2
    SHOTGUN = 3
    SNIPER_RIFLE = 4

    STATE_READY = 0
    STATE_RELOADING = 1

    player = None
    weapon_bullet_speed = 20
    weapon_action = 0
    weapon_shoot_delay = 0
    weapon_type = 0
    weapon_last_shoot_time = 0
    current_ammo = 0
    weapon_ammo = 0
    reload_time = 0
    weapon_reload_start_time = 0
    weapon_state = STATE_READY

    def __init__(self, player, weapon_bullet_speed, weapon_action, weapon_shoot_delay, weapon_type):
        self.player = player
        self.weapon_bullet_speed = weapon_bullet_speed
        self.weapon_action = weapon_action
        self.weapon_shoot_delay = weapon_shoot_delay
        self.weapon_type = weapon_type
        self.weapon_last_shoot_time = 0

    def shoot(self, weapon_target_x, weapon_target_y):
        if self.weapon_state != Weapon.STATE_READY:
            if self.weapon_state == Weapon.STATE_RELOADING:
                if time.time() - self.weapon_reload_start_time > self.reload_time:
                    self.current_ammo = self.weapon_ammo
                    self.weapon_state = Weapon.STATE_READY
                else:
                    return False
        if time.time() - self.weapon_last_shoot_time < self.weapon_shoot_delay:
            return False
        self.weapon_last_shoot_time = time.time()

        self.current_ammo -= 1
        if self.current_ammo == 0:
            self.weapon_state = Weapon.STATE_RELOADING
            self.weapon_reload_start_time = time.time()
        return True

    def perform_weapon_action(self, player, bullet_x, bullet_y, damage):
        player.damage(damage)
