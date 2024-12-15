import pygame


class Game:
    # Screen: 1920x1200
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 900
    BACKGROUND_COLOR = (200, 200, 200)
    curr_level = None
    players = None
    real_players = None
    game_interface = None
    gameover = False
    # TODO: Form teams if in the lobby we have a lot of players

    def play_music(file_name):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play()
        pygame.event.wait()

