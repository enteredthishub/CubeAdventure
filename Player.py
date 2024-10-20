import time

import pygame

from Bar import Bar
from Game import Game


class Player:
    CONTROL_TYPE_KEYBOARD = 0
    CONTROL_TYPE_MOUSE = 1
    CONTROL_TYPE_INTERNET = 2
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
    weapon_list = None
    selected_weapon = 0
    is_collided_x = False
    is_collided_y = False
    health_now = HEALTH_POINTS
    spawn_index = -1                            #WTF

    score = 200

    def __init__(self, player_x, player_y, player_width, player_height, player_color, control_type, button_gravity, button_left, button_right):
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

    prev_gravity_change_time = 0

    def change_gravity(self):
        if time.time() - self.prev_gravity_change_time > 1:
            self.player_gravity = not self.player_gravity
            self.prev_gravity_change_time = time.time()

    def process_key_events(self, events):
        if self.control_type == Player.CONTROL_TYPE_KEYBOARD:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.change_gravity()
                    if event.key == pygame.K_a:
                        self.player_moving_left = True
                    if event.key == pygame.K_d:
                        self.player_moving_right = True
                    if event.key == pygame.K_SPACE:
                        self.jump()
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

    def draw_player(self, draw_surface):
        pygame.draw.rect(draw_surface, self.player_color, pygame.Rect((self.player_x, self.player_y), (self.player_width, self.player_height)))

    def update_player_position(self):
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

    enter_zone = False
    enter_zone_time = 0
    last_zone_time = 0
    def process_bar_collision(self, bar):
        if bar.bar_type == Bar.TYPE_DANGER:
            Game.curr_level.restart(self)
            return False
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

    def damage(self, damage_points):
        self.health_now -= damage_points
        if self.health_now <= 0:
            Game.curr_level.restart(self)
        print("Player " + str(self.control_type) + " health: " + str(self.health_now))

    def set_spawn_index(self, player_spawn_index):
        self.spawn_index = player_spawn_index
