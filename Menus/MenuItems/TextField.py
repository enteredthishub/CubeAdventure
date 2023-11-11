import pygame

from Menus.MenuItems.MenuItem import MenuItem


class TextField(MenuItem):
    text_x = 0
    text_y = 0
    text_color = (0, 0, 0)
    font_name = 'dejavuserif'
    font_size = 30
    text = 'text'

    def __init__(self, text, text_x, text_y, text_color=(0, 0, 0), font_name='dejavuserif', font_size=30):
        self.text = text
        self.text_x = text_x
        self.text_y = text_y
        self.text_color = text_color
        self.font_name = font_name
        self.font_size = font_size

    def draw(self, screen):
        smallfont = pygame.font.SysFont(self.font_name, self.font_size)
        textRender = smallfont.render(self.text, True, self.text_color)
        screen.blit(textRender, (self.text_x, self.text_y))

    def handle_input(self, ev):
        pass
