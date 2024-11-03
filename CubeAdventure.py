import time
import pygame

from Bar import Bar
from Game import Game
from GameInterface import GameInterface
from Levels.Level1 import Level1
from Levels.Level2 import Level2
from Levels.Level3 import Level3
from Levels.Level4 import Level4
from Levels.Level5 import Level5
from MachineGunTheWeapon import MachineGunTheWeapon
from PistolTheWeapon import PistolTheWeapon
from Player import Player
from RPGTheWeapon import RPGTheWeapon
from ShotgunTheWeapon import ShotgunTheWeapon


class CubeAdventure:
    levels = None
    def start_game(self):
        pygame.init()

        Game.game_interface = GameInterface()

        player1 = Player(0, 0, 50, 50, (50, 50, 200), Player.CONTROL_TYPE_KEYBOARD, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT)
        player1.weapon_list.append(PistolTheWeapon(player1))
        player1.weapon_list.append(MachineGunTheWeapon(player1))
        player1.weapon_list.append(ShotgunTheWeapon(player1))
        player1.weapon_list.append(RPGTheWeapon(player1))
        #player2 = Player(0, 0, 50, 50, (0, 0, 200), Player.CONTROL_TYPE_KEYBOARD, pygame.K_w, pygame.K_a, pygame.K_d)
        #player3 = Player(0, 0, 50, 50, (200, 0, 0), pygame.K_u, pygame.K_h, pygame.K_k)
        Game.players = [player1]#, player2]
        self.levels = [Level1(), Level2(), Level3(), Level4(), Level5()]
        Game.curr_level = self.levels[4]
        Game.curr_level.restart(player1)


        frames = 0
        surface = pygame.display.set_mode([Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT])
        while True:
            surface.fill(Game.BACKGROUND_COLOR)

            # Draw players
            for p in Game.players:
                p.draw_player(surface)

            # Draw bars
            for b in Game.curr_level.bar_list:
                pygame.draw.rect(surface, b.bar_color, pygame.Rect((b.bar_x, b.bar_y), (b.bar_width, b.bar_height)))

            for zone in Game.curr_level.zone_list:
                for b in zone.bar_list:
                    s = pygame.Surface((b.bar_width, b.bar_height), pygame.SRCALPHA)  # per-pixel alpha
                    s.fill(zone.zone_color)  # notice the alpha value in the color
                    surface.blit(s, (b.bar_x, b.bar_y))
                zone.update()

            if Game.gameover == False:
                # Draw bullet
                for b in Game.curr_level.bullet_list:
                    b.draw_bullet(pygame, surface)

                # Update players
                events = pygame.event.get()
                for p in Game.players:
                    p.process_key_events(events)
                    p.update_player_position()

            Game.game_interface.draw(surface)

            pygame.display.flip()
            time.sleep(1 / 60)
            frames = frames + 1
