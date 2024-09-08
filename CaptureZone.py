import time
import pygame

class CaptureZone:
    capture_player = None
    bar_list = []
    #TODO: Add zone color
    def __init__(self, bar_list):
        self.bar_list = bar_list

