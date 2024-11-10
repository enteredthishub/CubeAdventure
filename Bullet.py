import math

from Game import Game


class Bullet:
    BULLET_ACTION_GRAVITY = 0
    bullet_originator = None
    bullet_weapon = None
    bullet_x = 0.0
    bullet_y = 0.0
    bullet_radius = 0
    bullet_color = (200, 0, 0)
    bullet_action = 0
    bullet_target_x = 0
    bullet_target_y = 0
    bullet_speed = 20
    bullet_damage = 0

    def __init__(self, bullet_originator, bullet_weapon, bullet_x, bullet_y, bullet_target_x, bullet_target_y, bullet_speed, bullet_color, bullet_radius=5, bullet_action=BULLET_ACTION_GRAVITY, bullet_damage=10):
        self.bullet_originator = bullet_originator
        self.bullet_weapon = bullet_weapon
        self.bullet_x = bullet_x
        self.bullet_y = bullet_y
        self.bullet_color = bullet_color
        self.bullet_radius = bullet_radius
        self.bullet_action = bullet_action
        self.bullet_target_x = bullet_target_x
        self.bullet_target_y = bullet_target_y
        self.bullet_speed = bullet_speed
        self.bullet_damage = bullet_damage

        if self.bullet_x < 0:
            self.bullet_x = 0
        if self.bullet_y < 0:
            self.bullet_y = 0
        if self.bullet_target_x < 0:
            self.bullet_target_x = 0
        if self.bullet_target_y < 0:
            self.bullet_target_y = 0

    x_diff = 1.0
    y_diff = -1.0
    def draw_bullet(self, pygame, surface):
        if self.y_diff == -1.0:
            bullet_x_diff = self.bullet_target_x - self.bullet_x
            if bullet_x_diff == 0:
                return
            self.y_diff = (self.bullet_target_y - self.bullet_y)/bullet_x_diff
            # FIXME: self.y_diff = (self.bullet_target_y - self.bullet_y)/(self.bullet_target_x - self.bullet_x)
            # ZeroDivisionError: division by zero
            c = math.sqrt(self.x_diff*self.x_diff + self.y_diff*self.y_diff)
            proportion = self.bullet_speed/c
            self.x_diff *= proportion
            self.y_diff *= proportion
            if self.bullet_target_x < self.bullet_x:
                self.x_diff *= -1
                self.y_diff *= -1
        self.bullet_x += self.x_diff
        self.bullet_y += self.y_diff
        pygame.draw.circle(surface, self.bullet_color, (self.bullet_x, self.bullet_y), self.bullet_radius)
        self.process_collisions()


    def process_collisions(self):
        for p in Game.players:
            if p == self.bullet_originator:
                continue
            is_collided = p.player_x - (self.bullet_radius *2) < self.bullet_x < p.player_x + p.player_width and p.player_y - (self.bullet_radius * 2) < self.bullet_y < p.player_y + p.player_height
            if is_collided:
                #print('Get ' + str(p.player_color))
                if self in Game.curr_level.bullet_list:
                    Game.curr_level.bullet_list.remove(self)
                #self.bullet_originator.bullet_list.remove(self)
                self.bullet_weapon.perform_weapon_action(p, self.bullet_x, self.bullet_y, self.bullet_damage)

        for b in Game.curr_level.bar_list:
            is_collided = b.bar_x - (self.bullet_radius * 2) < self.bullet_x < b.bar_x + b.bar_width and b.bar_y - (self.bullet_radius * 2) < self.bullet_y < b.bar_y + b.bar_height
            if is_collided:
                if self in Game.curr_level.bullet_list:
                    Game.curr_level.bullet_list.remove(self)



