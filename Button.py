class Button:
    button_width = 270
    button_height = 50
    button_x = 0
    button_y = 0
    text_color = (0, 0, 0)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    font_name = 'dejavuserif'
    font_size = 30
    text = 'button'
    press_function = None

    def __init__(self, text, button_x, button_y, button_width, press_function, button_height=50, text_color=(0, 0, 0), color_light=(170, 170, 170), color_dark=(100, 100, 100), font_name='dejavuserif', font_size=30):
        self.text = text
        self.button_x = button_x
        self.button_y = button_y
        self.button_width = button_width
        self.press_function = press_function
        self.button_height = button_height
        self.text_color = text_color
        self.color_light = color_light
        self.color_dark = color_dark
        self.font_name = font_name
        self.font_size = font_size

