import pygame
import time
import backend
import user
import bot
#will have difficulty levels
class Bot:
    def __init__(self):
        self.score = 0
        self.first_turn = False
        self.turn = False
        self.symbol = "O"
robot = Bot()