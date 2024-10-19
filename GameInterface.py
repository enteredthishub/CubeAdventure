import pygame

from Game import Game
from Menus.MenuItems.MenuItem import MenuItem
from Menus.MenuItems.TextField import TextField


class GameInterface:
    player1_score_textfield = None
    player2_score_textfield = None


    def __init__(self):
        self.player1_score_textfield = TextField("", 500, 50, (255, 0 ,0))
        self.player2_score_textfield = TextField("", 650, 50, (0, 0, 255))

    def draw(self, screen):
        if len(Game.players) > 0:
            self.player1_score_textfield.text = str(Game.players[0].score)
            self.player1_score_textfield.text_color = Game.players[0].player_color
            self.player1_score_textfield.draw(screen)
        if len(Game.players) > 1:
            self.player2_score_textfield.text = str(Game.players[1].score)
            self.player2_score_textfield.text_color = Game.players[1].player_color
            self.player2_score_textfield.draw(screen)


