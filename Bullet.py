import math


class Bullet:
    BULLET_ACTION_GRAVITY = 0
    bullet_x = 0.0
    bullet_y = 0.0
    bullet_radius = 0
    bullet_color = (200, 0, 0)
    bullet_action = 0
    bullet_target_x = 0
    bullet_target_y = 0
    bullet_speed = 20

    def __init__(self, bullet_x, bullet_y, bullet_target_x, bullet_target_y, bullet_speed, bullet_color, bullet_radius=5, bullet_action=BULLET_ACTION_GRAVITY):
        self.bullet_x = bullet_x
        self.bullet_y = bullet_y
        self.bullet_color = bullet_color
        self.bullet_radius = bullet_radius
        self.bullet_action = bullet_action
        self.bullet_target_x = bullet_target_x
        self.bullet_target_y = bullet_target_y
        self.bullet_speed = bullet_speed

    x_diff = 1.0
    y_diff = -1.0
    def draw_bullet(self, pygame, surface):
        if self.y_diff == -1.0:
            self.y_diff = (self.bullet_target_y - self.bullet_y)/(self.bullet_target_x - self.bullet_x)
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
