from Menus.MenuItems.MenuItem import MenuItem
import pygame


class InputBox(MenuItem):
    color_inactive = pygame.Color('grey')
    color_active = pygame.Color('black')
    font_name = 'dejavuserif'
    font_size = 30
    font = None

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = self.color_inactive
        self.text = text
        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.active = False

    def handle_input(self, ev):
        if ev.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(ev.pos):
                # Toggle the active variable.
                self.active = True
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.color_active if self.active else self.color_inactive
        if ev.type == pygame.KEYDOWN:
            if self.active:
                if ev.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif ev.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += ev.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
