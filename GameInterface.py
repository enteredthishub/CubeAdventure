from Game import Game
from Menus.MenuItems.TextField import TextField
from Player import Player


class GameInterface:
    player1_score_textfield = None
    player2_score_textfield = None
    HP_textfield = None
    gravity_textfield = None
    gameover_textfield = None
    gameover_player = None
    kills_textfield = None
    killstreak_textfield = None


    def __init__(self):
        self.player1_score_textfield = TextField("", 500, 50, (255, 0 ,0))
        self.player2_score_textfield = TextField("", 650, 50, (0, 0, 255))
        self.HP_textfield = TextField("", 1000, 50, (0, 0, 255))
        self.gravity_textfield = TextField("", 1000, 100, (0, 0, 255))
        self.gameover_textfield = TextField("", 450, 200, (100, 100, 100), 45)
        self.kills_textfield = TextField("", 1050, 150, (255, 0 , 0))
        self.killstreak_textfield = TextField("", 950, 10, (255, 0, 0))

    def draw(self, screen):
        if len(Game.real_players) > 0:
            self.gravity_textfield.text = 'Gravity:' + str(Game.real_players[0].current_acceleration)
            self.gravity_textfield.text_color = Game.real_players[0].player_color
            self.gravity_textfield.draw(screen)
        if len(Game.real_players) > 0:
            self.HP_textfield.text = 'HP:' + str(Game.real_players[0].health_now)
            self.HP_textfield.text_color = Game.real_players[0].player_color
            self.HP_textfield.draw(screen)
        if len(Game.real_players) > 0:
            self.kills_textfield.text = 'Kills:' + str(Game.real_players[0].kills)
            self.kills_textfield.text_color = Game.real_players[0].player_color
            self.kills_textfield.draw(screen)
        if len(Game.real_players) > 0:
            self.killstreak_textfield.text = 'Killstreak:' + str(Game.real_players[0].kills_streak)
            self.killstreak_textfield.text_color = Game.real_players[0].player_color
            self.killstreak_textfield.draw(screen)
        if len(Game.real_players) > 0:
            self.player1_score_textfield.text = str(Game.real_players[0].score)
            self.player1_score_textfield.text_color = Game.real_players[0].player_color
            self.player1_score_textfield.draw(screen)
        if len(Game.real_players) > 1:
            self.player2_score_textfield.text = str(Game.real_players[1].score)
            self.player2_score_textfield.text_color = Game.real_players[1].player_color
            self.player2_score_textfield.draw(screen)
        if self.gameover_player != None:
            self.gameover_textfield.text_color = self.gameover_player.player_color
            self.gameover_textfield.text = "Game over"
            self.gameover_textfield.draw(screen)


    def gameover(self, player):
        self.gameover_player = player

