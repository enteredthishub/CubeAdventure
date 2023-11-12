import pygame
from pygame import mouse

from Menus.MenuItems.MenuItem import MenuItem


class Button(MenuItem):
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

    def draw(self, screen):
        if self.button_x <= mouse.get_pos()[0] <= self.button_x + self.button_width and self.button_y <= mouse.get_pos()[1] <= self.button_y + self.button_height:
            pygame.draw.rect(screen, self.color_light, [self.button_x, self.button_y, self.button_width, self.button_height])
        else:
            pygame.draw.rect(screen, self.color_dark, [self.button_x, self.button_y, self.button_width, self.button_height])
        smallfont = pygame.font.SysFont(self.font_name, self.font_size)
        textRender = smallfont.render(self.text, True, self.text_color)
        screen.blit(textRender, (self.button_x + (self.button_width - textRender.get_width()) / 2, self.button_y + (self.button_height - textRender.get_height()) / 2))

    def handle_input(self, ev):
        input_handled = False
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if self.button_x <= mouse.get_pos()[0] <= self.button_x + self.button_width and self.button_y <= mouse.get_pos()[1] <= self.button_y + self.button_height:
                self.press_function()
                input_handled = True
        return input_handled
    