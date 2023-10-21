import time

import pygame

from Bar import Bar
from Game import Game


class Player:
    CONTROL_TYPE_KEYBOARD = 0
    CONTROL_TYPE_MOUSE = 1
    ACCELERATION = 0.2
    X_SPEED = 5

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

    prev_gravity_change_time = 0

    def change_gravity(self):
        if time.time() - self.prev_gravity_change_time > 1:
            self.player_gravity = not self.player_gravity
            self.prev_gravity_change_time = time.time()

    def process_key_events(self, events):
        if self.control_type == Player.CONTROL_TYPE_KEYBOARD:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == self.button_gravity:
                        self.change_gravity()
                    if event.key == self.button_left:
                        self.player_moving_left = True
                    if event.key == self.button_right:
                        self.player_moving_right = True
                if event.type == pygame.KEYUP:
                    if event.key == self.button_left:
                        self.player_moving_left = False
                    if event.key == self.button_right:
                        self.player_moving_right = False
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

    def process_hit(self):
        self.player_y_speed = self.player_y_speed - 2
        self.player_y_speed = -self.player_y_speed

    def draw_player(self, draw_surface):
        pygame.draw.rect(draw_surface, self.player_color, pygame.Rect((self.player_x, self.player_y), (self.player_width, self.player_height)))

    def update_player_position(self):
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
            is_collided = b1.bar_x - self.player_width < self.player_x < b1.bar_x + b1.bar_width and b1.bar_y - self.player_height < self.player_y < b1.bar_y + b1.bar_height
            if is_collided:
                if delta_x > 0:
                    self.player_x = b1.bar_x - self.player_width
                if delta_x < 0:
                    self.player_x = b1.bar_x + b1.bar_width
                self.process_bar_collision(b1)

        self.player_y = self.player_y + delta_y
        for b1 in Game.curr_level.bar_list:
            is_collided = b1.bar_x - self.player_width < self.player_x < b1.bar_x + b1.bar_width and b1.bar_y - self.player_height < self.player_y < b1.bar_y + b1.bar_height
            if is_collided:
                if delta_y > 0:
                    self.player_y = b1.bar_y - self.player_height
                    self.process_hit()
                if delta_y < 0:
                    self.player_y = b1.bar_y + b1.bar_height
                    self.process_hit()
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

        if self.player_y == 550 and self.player_x == 750:
            Game.curr_level = Game.curr_level.get_next_level()
            Game.curr_level.restartAll()

    def process_bar_collision(self, bar):
        if bar.bar_type == Bar.TYPE_DANGER:
            Game.curr_level.restart(self)
        if bar.bar_type == Bar.TYPE_SPHERE:
            self.player_y_speed = self.player_y_speed * 1.5
            if self.player_y_speed > 10:
                self.player_y_speed = 10
            if self.player_y_speed < -10:
                self.player_y_speed = -10
        if bar.bar_type == Bar.TYPE_BLUE_SPHERE:
            self.change_gravity()
        if bar.bar_type == Bar.TYPE_PORTAL_1:
            self.player_x = bar.teleport_to.bar_x
            self.player_y = bar.teleport_to.bar_y
