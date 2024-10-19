import time
import pygame

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

    def update(self):
        for p in Game.players:
            if p != self.capture_player and self.capture_player != None  :
                p.score -= 1
