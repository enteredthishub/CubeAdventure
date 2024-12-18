import time
import random
from logging.config import listen

import pygame

from Bar import Bar
from Game import Game
from MachineGunTheWeapon import MachineGunTheWeapon
from PistolTheWeapon import PistolTheWeapon
from RPGTheWeapon import RPGTheWeapon
from ShotgunTheWeapon import ShotgunTheWeapon
from SniperRifleTheWeapon import SniperRifleTheWeapon


class Player:
    CONTROL_TYPE_KEYBOARD = 0
    CONTROL_TYPE_MOUSE = 1
    CONTROL_TYPE_INTERNET = 2
    CONTROL_TYPE_TURRET = 3
    CONTROL_TYPE_AI = 4

    ACCELERATION = 0.8
    X_SPEED = 6
    JUMP_SPEED = 10
    HEALTH_POINTS = 100

    player_color = (0, 0, 0)
    player_width = 0
    player_height = 0
    player_x = 0
    player_y = 0

    # Controls
    control_type = CONTROL_TYPE_KEYBOARD
    button_gravity = 0
    button_left = 0
    button_right = 0

    # Dynamics
    player_y_speed = 0
    player_moving_left = False
    player_moving_right = False
    player_gravity = False

    bullet_list = None
    prev_bullet = None
    weapon_list = None
    selected_weapon = 0
    is_collided_x = False
    is_collided_y = False
    health_now = HEALTH_POINTS
    spawn_index = -1                            #WTF
    kills = 0
    kills_streak = 0

    score = 200

    #Explosion
    push_force_x = 0
    push_force_y = 0
    reduction_rate = 0

    def __init__(self, player_x, player_y, player_width, player_height, player_color, control_type, button_gravity=None, button_left=None, button_right=None):
        self.player_x = player_x
        self.player_y = player_y
        self.player_width = player_width
        self.player_height = player_height
        self.player_color = player_color
        self.control_type = control_type
        self.button_gravity = button_gravity
        self.button_left = button_left
        self.button_right = button_right
        self.bullet_list = []
        self.weapon_list = []
        self.selected_weapon = 0
        self.weapon_list.append(PistolTheWeapon(self))
        self.weapon_list.append(MachineGunTheWeapon(self))
        self.weapon_list.append(ShotgunTheWeapon(self))
        self.weapon_list.append(RPGTheWeapon(self))
        self.weapon_list.append(SniperRifleTheWeapon(self))

    prev_gravity_change_time = 0
    spawn_time = 0

    def change_gravity(self):
        self.ACCELERATION = 0.8
        if time.time() - self.prev_gravity_change_time > 1:
            self.player_gravity = not self.player_gravity
            self.prev_gravity_change_time = time.time()

    def respawn(self):
        self.spawn_time = time.time()
        if self.control_type == Player.CONTROL_TYPE_TURRET:
            self.player_color = (100, 100, 100)

    def process_key_events(self, events):
        if self.control_type == Player.CONTROL_TYPE_KEYBOARD:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.player_moving_left = True
                    if event.key == pygame.K_d:
                        self.player_moving_right = True
                    if event.key == pygame.K_SPACE:
                        self.jump()
                    if event.key == pygame.K_s:
                        self.ACCELERATION -= 0.1
                    if event.key == pygame.K_w:
                        self.ACCELERATION += 0.1
                    if event.key == pygame.K_1:
                        self.selected_weapon = 0
                    if event.key == pygame.K_2:
                        if len(self.weapon_list) >= 2:
                            self.selected_weapon = 1
                    if event.key == pygame.K_3:
                        if len(self.weapon_list) >= 3:
                            self.selected_weapon = 2
                    if event.key == pygame.K_4:
                        if len(self.weapon_list) >= 4:
                            self.selected_weapon = 3
                    if event.key == pygame.K_5:
                        if len(self.weapon_list) >= 5:
                            self.selected_weapon = 4


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.player_moving_left = False
                    if event.key == pygame.K_d:
                        self.player_moving_right = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    self.shoot(mouse[0], mouse[1])
        elif self.control_type == Player.CONTROL_TYPE_MOUSE:
            mouse = pygame.mouse.get_pos()
            if mouse[0] > self.player_x + 25:
                self.player_moving_right = True
                self.player_moving_left = False
            if mouse[0] < self.player_x + 25:
                self.player_moving_left = True
                self.player_moving_right = False
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.change_gravity()
        #print(pygame.mouse.get_pos())

    def shoot(self, x, y):
        weapon = self.weapon_list[self.selected_weapon]
        weapon.shoot(x, y)

    def jump(self):
        self.player_y_speed = -Player.JUMP_SPEED
        
    def process_hit(self):
        #self.player_y_speed = self.player_y_speed - 2
        #self.player_y_speed = -self.player_y_speed
        self.player_y_speed = 0

    lol = 0

    def draw_player(self, draw_surface):
        if self.kills_streak >= 3 and self.kills_streak < 10:
            self.draw_aura(draw_surface, (200, 50, 0, 100))
        if self.kills_streak >= 10 and self.kills_streak < 30:
            self.draw_aura(draw_surface, (250, 0, 0, 100))
        if self.kills_streak >= 30 and self.kills_streak < 45:
            self.draw_aura(draw_surface, (30, 30, 30, 100))
        if self.kills_streak >= 45 and self.kills_streak < 70:
                self.draw_aura(draw_surface, (100, 50, 50, 100))
            #pygame.draw.rect(draw_surface, (200, 50, 0, 100), pygame.Rect((self.player_x - 25, self.player_y - 25), (self.player_width + 50, self.player_height + 50)))
        pygame.draw.rect(draw_surface, self.player_color, pygame.Rect((self.player_x, self.player_y), (self.player_width, self.player_height)))
        if self.kills_streak >= 70 and self.kills_streak < 100:
            self.draw_aura(draw_surface, (250, 0, 0, 200))
        if self.kills_streak >= 100 and self.kills_streak < 300:
            self.draw_aura(draw_surface, (224, 210, 0, 200))

    def draw_aura(self, draw_surface, aura_color):
        s = pygame.Surface((self.player_width + 50, self.player_height + 50), pygame.SRCALPHA)  # per-pixel alpha
        s.fill(aura_color)  # notice the alpha value in the color
        draw_surface.blit(s, (self.player_x - 25, self.player_y - 25))

    def update_turret(self):
        target = -1
        while target == -1 or Game.players[target].control_type == Player.CONTROL_TYPE_TURRET:
            target = random.randint(0, len(Game.players) - 1)
        target_player = Game.players[target]
        if time.time() - self.spawn_time > 10:
            self.player_color = (0, 0, 0)
            self.shoot(target_player.player_x, target_player.player_y)


    prev_collide = 0
    prev_jump_time = 0
    def update_ai(self):
        target = -1
        #if self.player_moving_left:
            #delta_x = -self.X_SPEED
        #if self.player_moving_right:
            #delta_x = self.X_SPEED
        while target == -1 or Game.players[target].control_type == Player.CONTROL_TYPE_TURRET and Player.CONTROL_TYPE_AI:
            target = random.randint(0, len(Game.players) - 1)
        target_player = Game.players[target]
        self.shoot(target_player.player_x, target_player.player_y)
        if target_player.player_x > self.player_x + 100:
            self.player_moving_right = True
            self.player_moving_left = False
        if target_player.player_x < self.player_x - 100:
            self.player_moving_right = False
            self.player_moving_left = True
        if target_player.player_y < self.player_y:
            if time.time() - self.prev_jump_time > 0.2:
                self.prev_jump_time = time.time()
                self.jump()
        if time.time() - self.prev_collide > 2:
            self.prev_collide = time.time()
            if time.time() - self.prev_jump_time > 0.2:
                self.prev_jump_time = time.time()
                self.jump()

    enter_zone = False
    enter_zone_time = 0
    last_zone_time = 0

    def process_bar_collision(self, bar):
        if bar.bar_type == Bar.TYPE_DANGER:
            self.kills_streak = 0
            pygame.mixer.music.stop()
            self.X_SPEED = 6
            Game.curr_level.restart(self)
        if bar.bar_type == Bar.TYPE_SPHERE:
            self.player_y_speed = self.player_y_speed * 1.5
            if self.player_y_speed > 10:
                self.player_y_speed = 10
            if self.player_y_speed < -10:
                self.player_y_speed = -10
            return True
        if bar.bar_type == Bar.TYPE_BLUE_SPHERE:
            self.change_gravity()
            return True
        if bar.bar_type == Bar.TYPE_PORTAL_1:
            self.player_x = bar.teleport_to.bar_x
            self.player_y = bar.teleport_to.bar_y
            return False
        if bar.bar_type == Bar.TYPE_FINISH:
            Game.curr_level = Game.curr_level.get_next_level()
            Game.curr_level.restartAll()
            return False
        if bar.bar_type == Bar.TYPE_SPAWN_0 and self.spawn_index == 0:
            return False
        if bar.bar_type == Bar.TYPE_SPAWN_1 and self.spawn_index == 1:
            return False
        if bar.bar_type == Bar.TYPE_ZONE:
            if time.time() - self.last_zone_time > 0.5:
                self.enter_zone = False
                print('BRUUUUH')
            self.last_zone_time = time.time()
            if not self.enter_zone:
                self.enter_zone_time = time.time()
                self.enter_zone = True
            if time.time() - self.enter_zone_time > 5:
                print('LMAO LOOOOOOOL')
                bar.capture_zone.zone_color = (self.player_color[0], self.player_color[1], self.player_color[2], 145)
                bar.capture_zone.capture_player = self

            return False

        return True
    phase_5_time = 0
    phase_5_time_time = 0
    def damage(self, damage_points, bullet_originator):
        self.health_now -= damage_points
        if self.health_now <= 0:
            Game.curr_level.restart(self)
            bullet_originator.kills += 1
            bullet_originator.kills_streak += 1
            bullet_originator.X_SPEED += 0.3
            self.kills_streak = 0
            self.X_SPEED = 6

            if bullet_originator.kills_streak == 3:
                Game.play_music('Music/undertale_080. Finale.mp3')
                bullet_originator.health_now = 125
                bullet_originator.X_SPEED += 2
            if bullet_originator.kills_streak == 10:
                bullet_originator.health_now = 150
                bullet_originator.X_SPEED += 2
                Game.play_music('Music/793091_Scourge-of-The-Universe.mp3')
            if bullet_originator.kills_streak == 30:
                bullet_originator.health_now = 175
                bullet_originator.X_SPEED += 2
                Game.play_music('Music/Goukisan - Betrayal_of_Fear.ogg')
            if bullet_originator.kills_streak == 45:
                bullet_originator.health_now = 100
                bullet_originator.X_SPEED -= 36
                Game.play_music('Music/792912_The-Filthy-Mind-ft-Sixteen.mp3')
                if bullet_originator.X_SPEED < 10:
                    bullet_originator.X_SPEED = 10
            if bullet_originator.kills_streak == 70:
                bullet_originator.health_now = 225
                bullet_originator.X_SPEED = 10
                Game.play_music('Music/1278993_Stained-Brutal-Calamity-Re.mp3')
            if bullet_originator.kills_streak == 100:
                bullet_originator.health_now = 300
                bullet_originator.X_SPEED = 40
                Game.play_music('Music/1278993_Stained-Brutal-Calamity-Re.mp3')


            print("Player " + str(self.control_type) + ", health: " + str(self.health_now) + ', killstreak:' + str(self.kills_streak))

    prev_regen_time = 0
    def regen(self):
        if time.time() - self.prev_regen_time > 4:
            self.prev_regen_time = time.time()
            self.health_now += 5
            if self.kills_streak < 3:
                if self.health_now >= 100:
                    self.health_now = 100
            if self.kills_streak >= 3 and self.kills_streak < 10:
                if self.health_now >= 125:
                    self.health_now = 125
            if self.kills_streak >= 10 and self.kills_streak < 30:
                if self.health_now >= 150:
                    self.health_now = 150
            if self.kills_streak >= 30 and self.kills_streak < 45:
                if self.health_now >= 175:
                    self.health_now = 175
            if self.kills_streak >= 45:
                if self.health_now >= 200:
                    self.health_now = 200

    def set_spawn_index(self, player_spawn_index):
        self.spawn_index = player_spawn_index
        print('sus')

    def set_push_force(self, push_force_x, push_force_y, reduction_rate):
        self.push_force_x = push_force_x
        self.push_force_y = push_force_y
        self.reduction_rate = reduction_rate


    def update_player_position(self):
        self.regen()
        if self.control_type == Player.CONTROL_TYPE_TURRET:
            self.update_turret()
            return
        if self.control_type == Player.CONTROL_TYPE_AI:
            self.update_ai()
            #return
        if self.control_type == Player.CONTROL_TYPE_INTERNET:
            return
        delta_x = 0
        delta_y = 0
        if self.player_moving_left:
            delta_x = -self.X_SPEED
        if self.player_moving_right:
            delta_x = self.X_SPEED

        if self.player_gravity:
            delta_y = -self.player_y_speed
        else:
            delta_y = self.player_y_speed

        if self.reduction_rate != 0:
            delta_x += self.push_force_x
            delta_y += self.push_force_y
            self.push_force_x -= self.reduction_rate
            self.push_force_y -= self.reduction_rate
            if self.push_force_x <= 0 or self.push_force_y <= 0:
                self.reduction_rate = 0
                self.push_force_x = 0
                self.push_force_y = 0


        self.player_x = self.player_x + delta_x
        for b1 in Game.curr_level.bar_list:
            self.is_collided_x = b1.bar_x - self.player_width < self.player_x < b1.bar_x + b1.bar_width and b1.bar_y - self.player_height < self.player_y < b1.bar_y + b1.bar_height
            if self.is_collided_x:
                if self.process_bar_collision(b1):
                    if delta_x > 0:
                        self.player_x = b1.bar_x - self.player_width
                    if delta_x < 0:
                        self.player_x = b1.bar_x + b1.bar_width

        for zone in Game.curr_level.zone_list:
            for b1 in zone.bar_list:
                self.is_collided_x = b1.bar_x - self.player_width < self.player_x < b1.bar_x + b1.bar_width and b1.bar_y - self.player_height < self.player_y < b1.bar_y + b1.bar_height
                if self.is_collided_x:
                    self.process_bar_collision(b1)

        self.player_y = self.player_y + delta_y
        for b1 in Game.curr_level.bar_list:
            self.is_collided_y = b1.bar_x - self.player_width < self.player_x < b1.bar_x + b1.bar_width and b1.bar_y - self.player_height < self.player_y < b1.bar_y + b1.bar_height
            if self.is_collided_y:
                if self.process_bar_collision(b1):
                    if delta_y > 0:
                        self.player_y = b1.bar_y - self.player_height
                        self.process_hit()
                    if delta_y < 0:
                        self.player_y = b1.bar_y + b1.bar_height
                        self.process_hit()

        for zone in Game.curr_level.zone_list:
            for b1 in zone.bar_list:
                self.is_collided_y = b1.bar_x - self.player_width < self.player_x < b1.bar_x + b1.bar_width and b1.bar_y - self.player_height < self.player_y < b1.bar_y + b1.bar_height
                if self.is_collided_y:
                    self.process_bar_collision(b1)

        self.player_y_speed = self.player_y_speed + self.ACCELERATION

        # Hit bottom
        if self.player_y + self.player_height > Game.SCREEN_HEIGHT:
            self.player_y = Game.SCREEN_HEIGHT - self.player_height
            self.process_hit()

        # Hit ceiling
        if self.player_y < 0:
            self.player_y = 0
            self.process_hit()

        # Limit right
        if self.player_x + self.player_width > Game.SCREEN_WIDTH:
            self.player_x = Game.SCREEN_WIDTH - self.player_width

        # Limit left
        if self.player_x < 0:
            self.player_x = 0

        # print(str(time.time()) + ": " + str(int(self.player_x)) + ", " + str(int(self.player_y)) + ", " + str(int(self.player_y_speed)))

