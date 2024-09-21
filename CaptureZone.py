import time
import pygame

class CaptureZone:
    capture_player = None
    bar_list = []
    zone_color = (0, 0, 0)

    def __init__(self, bar_list, zone_color):
        self.bar_list = bar_list
        self.zone_color = zone_color
        for b in self.bar_list:
            b.capture_zone = self
