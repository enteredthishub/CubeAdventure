class Bar:
    TYPE_NORMAL = 0
    TYPE_DANGER = 1
    TYPE_SPHERE = 2
    TYPE_BLUE_SPHERE = 3
    bar_x = 0
    bar_y = 0
    bar_width = 0
    bar_height = 0
    bar_color = (200, 0, 0)
    bar_type = TYPE_NORMAL

    def __init__(self, bar_x, bar_y, bar_width, bar_height, bar_color, bar_type=TYPE_NORMAL):
        self.bar_x = bar_x
        self.bar_y = bar_y
        self.bar_width = bar_width
        self.bar_height = bar_height
        self.bar_color = bar_color
        self.bar_type = bar_type