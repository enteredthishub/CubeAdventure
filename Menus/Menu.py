import pygame

from Game import Game


class Menu:
    menu_items_list = None
    def get_menu_items_list(self):
        pass

    screen = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))

    color_background = (255, 255, 255)
    break_draw_cycle = False

    def close_menu(self):
        self.break_draw_cycle = True

    def draw_menu(self):
        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()

                for menu_item in self.get_menu_items_list():
                    menu_item.handle_input(ev)

            self.screen.fill(self.color_background)

            for menu_item in self.get_menu_items_list():
                menu_item.draw(self.screen)

            pygame.display.update()
            if self.break_draw_cycle:
                break
