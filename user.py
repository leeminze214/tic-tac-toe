import pygame
import time
import backend
import user
import bot

class User:
    def __init__(self):
        self.score = 0
        self.first_turn = True
        self.turn = True
        self.symbol = "X"

Bob = User()
