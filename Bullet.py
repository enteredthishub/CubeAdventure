class Bullet:
    BULLET_ACTION_GRAVITY = 0
    bullet_x = 0
    bullet_y = 0
    bullet_width = 0
    bullet_height = 0
    bullet_color = (200, 0, 0)
    bullet_action = 0
    bullet_target_x = 0
    bullet_target_y = 0
    bullet_speed = 20

    def __init__(self, bullet_x, bullet_y, bullet_color, bullet_width=5, bullet_height=10, bullet_action=BULLET_ACTION_GRAVITY):
        self.bullet_x = bullet_x
        self.bullet_y = bullet_y
        self.bullet_color = bullet_color
        self.bullet_width = bullet_width
        self.bullet_height = bullet_height
        self.bullet_action = bullet_action
