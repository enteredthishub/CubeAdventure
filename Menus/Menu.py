import pygame

from Game import Game


class Menu:
    def get_button_list(self):
        pass

    screen = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))

    color_background = (255, 255, 255)

    def draw_menu(self):
        while True:
            mouse = pygame.mouse.get_pos()
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()

                if ev.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.get_button_list():
                        if button.button_x <= mouse[0] <= button.button_x + button.button_width and button.button_y <= mouse[1] <= button.button_y + button.button_height:
                            button.press_function()

            self.screen.fill(self.color_background)

            for button in self.get_button_list():
                if button.button_x <= mouse[0] <= button.button_x + button.button_width and button.button_y <= mouse[1] <= button.button_y + button.button_height:
                    pygame.draw.rect(self.screen, button.color_light, [button.button_x, button.button_y, button.button_width, button.button_height])
                else:
                    pygame.draw.rect(self.screen, button.color_dark, [button.button_x, button.button_y, button.button_width, button.button_height])
                smallfont = pygame.font.SysFont(button.font_name, button.font_size)
                textRender = smallfont.render(button.text, True, button.text_color)

                self.screen.blit(textRender, (button.button_x + (button.button_width - textRender.get_width()) / 2, button.button_y + (button.button_height - textRender.get_height()) / 2))

            pygame.display.update()
