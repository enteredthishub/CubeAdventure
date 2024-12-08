import time

from Game import Game

class CaptureZone:
    capture_player = None
    bar_list = []
    zone_color = (0, 0, 0, 0)

    def __init__(self, bar_list, zone_color):
        self.bar_list = bar_list
        self.zone_color = zone_color
        for b in self.bar_list:
            b.capture_zone = self

    prev_time = 0
    def update(self):
        if not Game.gameover and time.time() - self.prev_time > 1:
            self.prev_time = time.time()
            for p in Game.real_players:
                if p != self.capture_player and self.capture_player != None  :
                    p.score -= 1
                    if p.score == 0:
                        Game.game_interface.gameover(p)
                        Game.gameover = True
