class Bar:
    TYPE_NORMAL = 0
    TYPE_DANGER = 1
    TYPE_SPHERE = 2
    TYPE_BLUE_SPHERE = 3
    TYPE_PORTAL_1 = 4
    TYPE_PORTAL_2 = 5
    TYPE_FINISH = 6
    TYPE_SPAWN_0 = 7
    TYPE_SPAWN_1 = 8
    TYPE_ZONE = 9
    bar_x = 0
    bar_y = 0
    bar_width = 0
    bar_height = 0
    bar_color = (200, 0, 0)
    bar_type = TYPE_NORMAL
    teleport_to = None
    capture_zone = None

    def __init__(self, bar_x, bar_y, bar_width, bar_height, bar_color, bar_type=TYPE_NORMAL, teleport_to=None):
        self.bar_x = bar_x
        self.bar_y = bar_y
        self.bar_width = bar_width
        self.bar_height = bar_height
        self.bar_color = bar_color
        self.bar_type = bar_type
        self.teleport_to = teleport_to
